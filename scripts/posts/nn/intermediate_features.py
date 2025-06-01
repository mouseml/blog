from itertools import product

from manim import *

config.frame_height = 9
config.frame_width = 16
config.frame_rate = 60
config.frame_size = (1920, 1080)

HEIGHT = 0.8
WIDTH = 2.0


def get_block(label: str, shift) -> tuple[Mobject, Mobject]:
    block = Rectangle(height=HEIGHT, width=WIDTH, fill_color=BLACK)
    label = Tex(label, font_size=35).move_to(block.get_center())
    Group(block, label).move_to(shift)
    return block, label


def get_blocks(labels: list[str], shift) -> list[Mobject]:
    blocks = []
    for i, label in enumerate(labels):
        block = get_block(label, 1.2 * i * WIDTH * RIGHT)
        blocks += list(block)
    Group(*blocks).move_to(shift)
    return blocks


def get_connection(x: Mobject, y: Mobject) -> Mobject:
    return Line(x.get_bottom(), y.get_top(), stroke_width=2, buff=0)


def get_connections(l1: list[Mobject], l2: list[Mobject]) -> list[Mobject]:
    return [get_connection(x, y) for x, y in product(l1[::2], l2[::2])]


class IntermediateFeatures(Scene):
    def construct(self) -> None:
        self.add(Title("Промежуточные признаки"))

        features1 = get_blocks(["Возраст", "Вес", "Пол", "Курение", "Алкоголь", "Работа"], 2.5 * UP)
        features2 = get_blocks(["Фактор 1", "Фактор 2", "...", "Фактор N"], 0.5 * DOWN)
        features3 = get_blocks(["Инфаркт"], 3.5 * DOWN)

        layer1 = get_blocks(["Linear"], 1 * UP)
        layer2 = get_blocks(["Linear"], 2 * DOWN)

        connections1 = get_connections(features1, layer1)
        connections2 = get_connections(layer1, features2)
        connections3 = get_connections(features2, layer2)
        connections4 = get_connections(layer2, features3)

        self.add(*features1, *features2, *features3)
        self.add(*layer1, *layer2)
        self.add(*connections1, *connections2, *connections3, *connections4)


if __name__ == "__main__":
    IntermediateFeatures().render()
