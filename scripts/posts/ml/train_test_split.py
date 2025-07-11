import random

from manim import *

config.frame_height = 9
config.frame_width = 16
config.frame_rate = 60
config.frame_size = (1920, 1080)
config.output_file = "train_test_split.png"

random.seed(42)

RADIUS = 0.2
FONT_SIZE = 35


def get_circle() -> Mobject:
    return Circle(RADIUS, stroke_width=0, fill_color=RED, fill_opacity=1)


class TrainTestSplit(Scene):
    def construct(self) -> None:
        self.add(Title("Разбиение выборки"))

        samples = [
            get_circle().shift(2.5 * i * RADIUS * RIGHT)
            for i in range(20)
        ]
        Group(*samples).move_to(0.5 * UP)

        for x in samples:
            if random.random() > 0.6:
                x.set_color(BLUE)

        train_legend = get_circle().shift(2.5 * RIGHT + 1.5 * DOWN)
        train_label = Tex("Обучение", font_size=FONT_SIZE).next_to(train_legend, RIGHT)
        val_legend = get_circle().set_color(BLUE).shift(2.5 * RIGHT + 2.5 * DOWN)
        val_label = Tex("Валидация", font_size=FONT_SIZE).next_to(val_legend, RIGHT)

        self.add(*samples)
        self.add(train_legend, val_legend)
        self.add(train_label, val_label)


if __name__ == "__main__":
    TrainTestSplit().render()
