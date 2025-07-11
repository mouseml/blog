import random
from manim import *

config.frame_height = 9
config.frame_width = 16
config.frame_size = (1920, 1080)
config.output_file = "train_test_split"

SIDE = 0.4


def get_cell() -> Mobject:
    return Square(side_length=SIDE, color=WHITE, fill_color=BLACK, fill_opacity=1, stroke_width=1)


def get_vector(size: int) -> Mobject:
    cells = [get_cell().shift(i * SIDE * RIGHT) for i in range(size)]
    return VGroup(*cells)


def get_matrix(rows: int, cols: int) -> Mobject:
    rows = [get_vector(cols).shift(SIDE * i * DOWN) for i in range(rows)]
    return VGroup(*rows)


def get_label(str_: str) -> Mobject:
    return Text(str_, font_size=20)


class TrainTestSplit(Scene):
    def construct(self) -> None:
        self.add(Title("Разбиение"))
        matrix = get_matrix(17, 11).move_to(0.6 * DOWN)
        numbers = [get_label(str(i + 1)).next_to(matrix[i], LEFT) for i in range(17)]
        legend = [
            get_cell().set_fill(RED, opacity=1).move_to(4 * RIGHT + 2 * DOWN),
            get_cell().set_fill(BLUE, opacity=1).move_to(4 * RIGHT + 3 * DOWN),
        ]
        legend_labels = [
            get_label("Обучение").next_to(legend[0], RIGHT),
            get_label("Валидация").next_to(legend[1], RIGHT),
        ]

        generator = random.Random(5)
        for i in range(len(matrix)):
            row_color = RED if generator.random() > 0.5 else BLUE
            matrix[i].set_fill(row_color, opacity=1)

        self.add(matrix, *numbers, *legend, *legend_labels)


if __name__ == "__main__":
    TrainTestSplit().render()
