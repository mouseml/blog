import pandas as pd
from manim import *

from scripts.posts.trees.utils import set_defaults, set_config


Point = tuple[float, float]
LineConfig = tuple[Point, Point]
PolygonConfig = tuple[list[Point], ManimColor]


def get_axes(x_label: str, y_label: str) -> VGroup:
    """Return axes."""
    axes = Axes(
        x_range=[1, 9.99],
        y_range=[1, 9.99],
        x_length=6,
        y_length=6,
    )
    labels = axes.get_axis_labels(x_label=Text(x_label), y_label=Text(y_label))
    x_tick_labels = [Text(str(x)).move_to(axes.c2p(x, 0.5)) for x in range(1, 10)]
    y_tick_labels = [Text(str(x)).move_to(axes.c2p(0.5, x)) for x in range(1, 10)]
    return VGroup(axes, labels, VGroup(*x_tick_labels), VGroup(*y_tick_labels))


def get_axes_dots(
    data: pd.DataFrame, axes: Axes, x: str, y: str, color: str
) -> list[Dot]:
    """Return axes dots."""
    return [
        Dot(
            axes.c2p(data.iloc[i][x], data.iloc[i][y]),
            color=data.iloc[i][color],
            z_index=-1,
        )
        for i in range(len(data))
    ]


def get_axes_line(axes: Axes, x1: Point, x2: Point) -> Line:
    """Return axes line."""
    return Line(axes.c2p(*x1), axes.c2p(*x2), stroke_width=1, z_index=-10)


def get_axes_polygon(axes: Axes, points: list[Point], color: ManimColor) -> Polygon:
    """Return axes polygon."""
    return Polygon(
        *(axes.c2p(*x) for x in points),
        fill_color=color,
        stroke_width=0,
        fill_opacity=0.25,
        z_index=-10,
    )


class Chart(Scene):
    def __init__(
        self,
        data_path: str,
        lines: list[LineConfig],
        polygons: list[PolygonConfig],
        x_column: str,
        y_column: str,
        color_column: str,
        colors: dict[str | int, ManimColor],
    ) -> None:
        super().__init__()
        self._data_path = data_path
        self._lines = lines
        self._polygons = polygons
        self._x_column = x_column
        self._y_column = y_column
        self._color_column = color_column
        self._colors = colors

    def construct(self) -> None:
        data = pd.read_csv(self._data_path)
        data[self._color_column] = data[self._color_column].replace(self._colors)

        axes = get_axes(self._x_column, self._y_column)
        dots = get_axes_dots(
            data, axes[0], x=self._x_column, y=self._y_column, color=self._color_column
        )

        lines = [
            get_axes_line(axes[0], line_start, line_end)
            for line_start, line_end in self._lines
        ]
        polygons = [
            get_axes_polygon(axes[0], points, color) for points, color in self._polygons
        ]

        self.add(axes, *dots, *lines, *polygons)


if __name__ == "__main__":
    set_defaults()

    set_config("chart1")
    Chart(
        "data/data1.csv",
        lines=[],
        polygons=[],
        x_column="Лекции",
        y_column="Семинары",
        color_column="Зачет",
        colors={"да": BLUE, "нет": RED},
    ).render()

    lines = [
        ((3, 1), (3, 9)),
        ((4, 1), (4, 9)),
        ((7, 1), (7, 9)),
        ((8, 1), (8, 9)),
        ((1, 3), (9, 3)),
        ((1, 5), (9, 5)),
        ((1, 7), (9, 7)),
        ((1, 8), (9, 8)),
    ]
    set_config("chart1_options")
    Chart(
        "data/data1.csv",
        lines=lines,
        polygons=[],
        x_column="Лекции",
        y_column="Семинары",
        color_column="Зачет",
        colors={"да": BLUE, "нет": RED},
    ).render()

    lines = [((4, 1), (4, 9))]
    polygons = [
        ([(1, 1), (4, 1), (4, 9), (1, 9)], RED),
        ([(4, 1), (9, 1), (9, 9), (4, 9)], BLUE),
    ]
    set_config("chart1_solution")
    Chart(
        "data/data1.csv",
        lines=lines,
        polygons=polygons,
        x_column="Лекции",
        y_column="Семинары",
        color_column="Зачет",
        colors={"да": BLUE, "нет": RED},
    ).render()

    lines = [((4, 1), (4, 9)), ((4, 3), (9, 3))]
    polygons = [
        ([(1, 1), (4, 1), (4, 9), (1, 9)], RED),
        ([(4, 1), (9, 1), (9, 3), (4, 3)], RED),
        ([(4, 3), (9, 3), (9, 9), (4, 9)], BLUE),
    ]
    set_config("chart2_solution")
    Chart(
        "data/data2.csv",
        lines=lines,
        polygons=polygons,
        x_column="Лекции",
        y_column="Семинары",
        color_column="Зачет",
        colors={"да": BLUE, "нет": RED},
    ).render()

    lines = [
        ((1, 4), (9, 4)),
        ((6, 1), (6, 9)),
        ((3, 1), (3, 9)),
        ((3, 6), (6, 6)),
        ((3, 3), (6, 3)),
        ((4, 1), (4, 4)),
    ]
    polygons = [
        ([(1, 1), (3, 1), (3, 4), (1, 4)], RED),
        ([(3, 3), (4, 3), (4, 4), (3, 4)], RED),
        ([(3, 1), (4, 1), (4, 3), (3, 3)], BLUE),
        ([(4, 1), (6, 1), (6, 3), (4, 3)], RED),
        ([(4, 3), (6, 3), (6, 4), (4, 4)], BLUE),
        ([(6, 1), (9, 1), (9, 4), (6, 4)], RED),
        ([(1, 4), (3, 4), (3, 9), (1, 9)], BLUE),
        ([(3, 4), (6, 4), (6, 6), (3, 6)], BLUE),
        ([(3, 6), (6, 6), (6, 9), (3, 9)], RED),
        ([(6, 4), (9, 4), (9, 9), (6, 9)], BLUE),
    ]
    set_config("chart3_solution")
    Chart(
        "data/data3.csv",
        lines=lines,
        polygons=polygons,
        x_column="Лекции",
        y_column="Семинары",
        color_column="Зачет",
        colors={"да": BLUE, "нет": RED},
    ).render()

    lines = [((1, 5), (9, 5)), ((5, 1), (5, 9))]
    polygons = [
        ([(1, 1), (5, 1), (5, 5), (1, 5)], RED),
        ([(5, 5), (9, 5), (9, 9), (5, 9)], RED),
        ([(1, 5), (5, 5), (5, 9), (1, 9)], BLUE),
        ([(5, 1), (9, 1), (9, 5), (5, 5)], BLUE),
    ]
    set_config("chart_xor_good_solution")
    Chart(
        "data/data_xor.csv",
        lines=lines,
        polygons=polygons,
        x_column="x1",
        y_column="x2",
        color_column="y",
        colors={1: BLUE, 0: RED},
    ).render()

    lines = [((2, 1), (2, 9)), ((7, 1), (7, 9))]
    polygons = [
        ([(1, 1), (2, 1), (2, 9), (1, 9)], RED),
        ([(7, 1), (9, 1), (9, 9), (7, 9)], RED),
    ]
    set_config("chart_xor_solution")
    Chart(
        "data/data_xor.csv",
        lines=lines,
        polygons=polygons,
        x_column="x1",
        y_column="x2",
        color_column="y",
        colors={1: BLUE, 0: RED},
    ).render()
