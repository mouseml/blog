import random

from manim import *

config.frame_height = 9
config.frame_width = 16
config.frame_size = (1920, 1080)
config.output_file = "gradient_descent_idea"


def get_axes() -> Axes:
    return Axes(
        x_range=[0, 2],
        y_range=[0, 2],
        x_length=2.5,
        y_length=2.5,
    )


def get_label(str_: str) -> Mobject:
    return MathTex(str_, font_size=45)


class GradientDescentIdea(Scene):
    def construct(self) -> None:
        self.add(Title("Градиентный спуск"))
        axes = [
            get_axes().move_to(3.25 * LEFT + 0.3 * DOWN, DL),
            get_axes().move_to(0.75 * RIGHT + 0.3 * DOWN, DL),
            get_axes().move_to(3.25 * LEFT + 4.2 * DOWN, DL),
            get_axes().move_to(0.75 * RIGHT + 4.2 * DOWN, DL),
        ]
        labels = [x.get_axis_labels("x", "f(x)") for x in axes]
        dots = [Dot(x.c2p(1, 1), color=RED, z_index=1) for x in axes]
        lines = [
            axes[0].plot(lambda x: 0.2 * x ** 2 + 0.8, x_range=[0.5, 1.5]),
            axes[1].plot(lambda x: 0.2 * (x - 2) ** 2 + 0.8, x_range=[0.5, 1.5]),
            axes[2].plot(lambda x: x ** 2, x_range=[0.7, 1.3]),
            axes[3].plot(lambda x: (x - 2) ** 2, x_range=[0.7, 1.3]),
        ]
        formulas = [
            get_label(r"\frac{\partial f}{\partial x} > 0").next_to(axes[0], LEFT, buff=1),
            get_label(r"\frac{\partial f}{\partial x} < 0").next_to(axes[1], RIGHT, buff=1),
            get_label(r"\frac{\partial f}{\partial x} \gg 0").next_to(axes[2], LEFT, buff=1),
            get_label(r"\frac{\partial f}{\partial x} \ll 0").next_to(axes[3], RIGHT, buff=1),
        ]

        self.add(*axes, *labels, *dots, *lines, *formulas)


if __name__ == "__main__":
    GradientDescentIdea().render()
