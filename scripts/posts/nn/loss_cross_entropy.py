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


class LossCrossEntropy(Scene):
    def construct(self) -> None:
        self.add(Title("Бинарная кросс-энтропия"))
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[-0.99, 4, 1],
            x_length=6,
            y_length=6,
        ).add_coordinates().shift(0.5 * DOWN)
        line = axes.plot(
            lambda x: - math.log(x),
            x_range=[0.03, 3.5],
            color=RED,
        )
        self.add(axes, line)


if __name__ == "__main__":
    LossCrossEntropy().render()
