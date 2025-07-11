from manim import *

config.frame_height = 9
config.frame_width = 16
config.frame_size = (1920, 1080)
config.output_file = "tensor_types"

SIDE = 1


def get_cell() -> Mobject:
    return Square(side_length=SIDE, color=WHITE, fill_color=BLACK, fill_opacity=1)


def get_scalar() -> Mobject:
    return VGroup(get_cell())


def get_vector() -> Mobject:
    cells = [get_cell().shift(i * SIDE * RIGHT) for i in range(3)]
    return VGroup(*cells)


def get_matrix() -> Mobject:
    rows = [get_vector().shift(SIDE * i * DOWN) for i in range(3)]
    return VGroup(*rows)


def get_tensor() -> Mobject:
    cells = [get_matrix().shift(0.25 * i * (UP + RIGHT)).set_z_index(-i) for i in range(3)]
    return VGroup(*cells)


def get_label(str_: str) -> Mobject:
    return Text(str_, font_size=30)


class TensorTypes(Scene):
    def construct(self) -> None:
        self.add(Title("Тензоры"))

        tensors = [
            get_scalar().move_to(6.5 * LEFT + 1.7 * DOWN, DL),
            get_vector().move_to(4.5 * LEFT + 1.7 * DOWN, DL),
            get_matrix().move_to(0.5 * LEFT + 1.7 * DOWN, DL),
            get_tensor().move_to(3.5 * RIGHT + 1.7 * DOWN, DL),
        ]
        dimensionality = [
            get_label("0 D").next_to(tensors[0], DOWN, buff=0.4),
            get_label("1 D").next_to(tensors[1][1], DOWN, buff=0.4),
            get_label("2 D").next_to(tensors[2][2][1], DOWN, buff=0.4),
            get_label("3 D").next_to(tensors[3][0][2][1], DOWN, buff=0.4),
        ]
        names = [
            get_label("Скаляр").next_to(dimensionality[0], DOWN, buff=0.4),
            get_label("Вектор").next_to(dimensionality[1], DOWN, buff=0.4),
            get_label("Матрица").next_to(dimensionality[2], DOWN, buff=0.4),
            get_label("").next_to(dimensionality[3], DOWN, buff=0.4),
        ]

        self.add(*tensors, *dimensionality, *names)


if __name__ == "__main__":
    TensorTypes().render()
