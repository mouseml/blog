import random

from manim import *

config.frame_height = 9
config.frame_width = 16
config.frame_rate = 30
config.frame_size = (1920, 1080)
config.output_file = "standard_scaler"


def get_axes() -> Axes:
    return Axes(
        x_range=[-5, 5, 1],
        y_range=[0, 2, 1],
        x_length=6,
        y_length=1.75,
    )


def get_bin(width: float, height: float) -> Mobject:
    return Rectangle(width=width, height=height, fill_color=RED, fill_opacity=0.5, stroke_width=0, z_index=-1)


def get_bins(values: list[float], x_min: float, x_max: float, axes: Axes) -> VGroup:
    step = (x_max - x_min) / len(values)
    bin_width = float((axes.c2p(step, 0) - axes.c2p(0, 0))[0])
    bins = []
    for i, value in enumerate(values):
        height = float((axes.c2p(0, value) - axes.c2p(0, 0))[1])
        point = axes.c2p(x_min + i * step, 0)
        bins.append(get_bin(width=bin_width, height=height).move_to(point, DL))
    return VGroup(*bins)



class StandardScaler(Scene):
    def construct(self) -> None:
        self.add(Title("Нормализация"))
        generator = random.Random(0)

        labels = ["a", "b", "c"]
        offsets = [0.25, -2, -4.25]
        ranges1 = [(-5, 3), (0, 4), (-3, -1)]
        ranges2 = [(-3, 3), (-3, 3), (-3, 3)]
        titles = ["До", "После"]
        values = [
            [generator.uniform(0.5, 1.5) for _ in range(24)],
            [generator.uniform(0.5, 1.5) for _ in range(16)],
            [generator.uniform(0.5, 1.5) for _ in range(8)],
        ]

        axes1 = [get_axes().move_to(7 * LEFT + x * UP, DL) for x in offsets]
        labels1 = [x.get_axis_labels(y, "") for x, y in zip(axes1, labels)]
        axes2 = [get_axes().move_to(0.75 * RIGHT + x * UP, DL) for x in offsets]
        labels2 = [x.get_axis_labels(y, "") for x, y in zip(axes2, labels)]
        bins1 = [get_bins(x[0], x_min=x[1][0], x_max=x[1][1], axes=x[2]) for x in zip(values, ranges1, axes1)]
        bins2 = [get_bins(x[0], x_min=x[1][0], x_max=x[1][1], axes=x[2]) for x in zip(values, ranges2, axes2)]
        titles = [Text(x[0], font_size=30).next_to(x[1][0], UP) for x in zip(titles, (axes1, axes2))]

        self.add(*axes1, *axes2, *labels1, *labels2, *bins1, *bins2, *titles)


if __name__ == "__main__":
    StandardScaler().render()
