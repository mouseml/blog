from manim import *

config.frame_height = 9
config.frame_width = 16
config.frame_rate = 60
config.frame_size = (1920, 1080)


def loss(x: float) -> float:
    return (x - 3) ** 2 + 1


class GradientDescentDummy(Scene):
    def construct(self) -> None:
        self.add(Title("Градиентный спуск"))

        start = 1.1
        step = 0.3
        steps = 8

        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 6, 1],
            x_length=6,
            y_length=6,
        ).shift(1 * DOWN)
        line = axes.plot(loss, x_range=[start, start + (steps - 1) * step])
        x_label = axes.get_x_axis_label(MathTex(r"w_1"))
        y_label = axes.get_y_axis_label(MathTex(r"\mathcal{L}(\mathbf{X}, \mathbf{y}; w_1)"))

        markers = []
        dots = []

        for i in range(steps):
            x = start + i * step
            point = axes.c2p(x, loss(x))
            markers.append(axes.get_line_from_axis_to_point(0, point))
            dots.append(Dot(point, color=RED, z_index=1))

        self.add(axes, line, x_label, y_label, *markers, dots[-1])


if __name__ == "__main__":
    GradientDescentDummy().render()
