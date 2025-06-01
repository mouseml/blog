from itertools import product

from manim import *

config.frame_height = 9
config.frame_width = 16
config.frame_rate = 60
config.frame_size = (1920, 1080)

RADIUS = 0.3


def get_neuron() -> Mobject:
    return Circle(radius=RADIUS, stroke_width=0, fill_color=WHITE, fill_opacity=1)


def get_layer(n: int, shift) -> list[Mobject]:
    layer = [get_neuron().shift(2.1 * i * RADIUS * DOWN) for i in range(n)]
    Group(*layer).move_to(shift)
    return layer


def get_connection(x: Mobject, y: Mobject) -> Mobject:
    return Line(x.get_center(), y.get_center(), stroke_width=2, buff=RADIUS)


def get_connections(l1: list[Mobject], l2: list[Mobject]) -> list[Mobject]:
    return [get_connection(x, y) for x, y in product(l1, l2)]


class NNSchemeBad(Scene):
    def construct(self):
        self.add(Title("Нейронная сеть (плохая схема)"))
        layers = [
            get_layer(9, 3 * LEFT + 0.5 * DOWN),
            get_layer(7, 1 * LEFT + 0.5 * DOWN),
            get_layer(7, 1 * RIGHT + 0.5 * DOWN),
            get_layer(3, 3 * RIGHT + 0.5 * DOWN),
        ]
        connections = [
            get_connections(x, y) for x, y in zip(layers[:-1], layers[1:])
        ]
        for x in layers + connections:
            self.add(*x)


if __name__ == "__main__":
    NNSchemeBad().render()
