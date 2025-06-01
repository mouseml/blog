import random

from manim import *

config.frame_height = 9
config.frame_width = 16
config.frame_rate = 60
config.frame_size = (1920, 1080)

random.seed(42)


def get_value() -> float:
    return round(random.random() - 0.5, 1)


class ActivationReLU(Scene):
    def construct(self) -> None:
        self.add(Title("ReLU"))
        axes = Axes(
            x_range=[-2.99, 3],
            y_range=[-2.99, 3],
            x_length=6,
            y_length=6,
        ).add_coordinates().shift(0.5 * DOWN)
        line = axes.plot(
            lambda x: 0 if x < 0 else x,
            color=RED,
            x_range=[-3, 2.5],
        )
        self.add(axes, line)


if __name__ == "__main__":
    ActivationReLU().render()
