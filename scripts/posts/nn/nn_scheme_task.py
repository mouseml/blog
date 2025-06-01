import random

from manim import *


config.frame_height = 9
config.frame_width = 16
config.frame_rate = 60
config.frame_size = (1920, 1080)

HEIGHT = 0.8


def get_block(label: str) -> Mobject:
    block = Rectangle(height=HEIGHT, width=2.8, fill_color=BLACK)
    label = Tex(label, font_size=35).move_to(block.get_center())
    return Group(block, label)


def get_value() -> float:
    return round(random.random(), 1)


def get_arrow(x: Mobject, y: Mobject) -> Mobject:
    return Arrow(x.get_bottom(), y.get_top(), max_tip_length_to_length_ratio=0.5, buff=0)


def get_model(labels: list[str], shift) -> list[Mobject]:
    blocks = [get_block(x).shift(1.5 * HEIGHT * i * DOWN) for i, x in enumerate(labels)]
    Group(*blocks).move_to(shift, UP)
    arrows = [get_arrow(x, y) for x, y in zip(blocks[:-1], blocks[1:])]
    return blocks + arrows


class NNSchemeTask(Scene):
    def construct(self):
        self.add(Title("Задача"))
        model1 = get_model(["Linear(16)", "ReLU", "Linear(32)", "ReLU", "Linear(5)", "Softmax"], 4.5 * LEFT + 2.8 * UP)
        model2 = get_model(["Linear(32)", "ReLU", "Linear(32)", "ReLU", "Linear(1)"], 2.8 * UP)
        model3 = get_model(["Linear(16)", "ReLU", "Linear(1)", "Sigmoid"], 4.5 * RIGHT + 2.8 * UP)
        self.add(*model1, *model2, *model3)


if __name__ == "__main__":
    NNSchemeTask().render()
