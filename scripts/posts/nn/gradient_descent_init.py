from manim import *

config.frame_height = 9
config.frame_width = 16
config.frame_rate = 60
config.frame_size = (1920, 1080)


def loss(x: float) -> float:
    return (x - 3) ** 2 + 1


class GradientDescentInit(Scene):
    def construct(self) -> None:
        self.add(Title("Градиентный спуск"))
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 6, 1],
            x_length=6,
            y_length=6,
        ).shift(1 * DOWN)
        x_label = axes.get_x_axis_label(MathTex(r"w_1"))
        y_label = axes.get_y_axis_label(MathTex(r"\mathcal{L}(\mathbf{X}, \mathbf{y}; w_1)"))

        start = 1.1
        point = axes.c2p(start, loss(start))
        marker = axes.get_line_from_axis_to_point(0, point)
        dot = Dot(point, color=RED, z_index=1)

        self.add(axes, x_label, y_label, dot, marker)


if __name__ == "__main__":
    GradientDescentInit().render()
