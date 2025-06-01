import math
import random

from manim import *

config.frame_height = 9
config.frame_width = 16
config.frame_rate = 60
config.frame_size = (1920, 1080)

random.seed(42)


def get_value() -> float:
    return round(random.random() - 0.5, 1)


class ActivationSigmoid(Scene):
    def construct(self) -> None:
        self.add(Title("Sigmoid"))
        axes = Axes(
            x_range=[-7.99, 8, 2],
            y_range=[-0.2, 1.2, 0.5],
            x_length=6,
            y_length=6,
        ).add_coordinates().shift(0.5 * DOWN)
        line = axes.plot(
            lambda x: 1 / (1 + math.exp(-x)),
            color=RED,
            x_range=[-8, 8],
        )
        self.add(axes, line)


if __name__ == "__main__":
    ActivationSigmoid().render()
