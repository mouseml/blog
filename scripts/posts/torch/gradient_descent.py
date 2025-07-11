from manim import *

config.frame_height = 9
config.frame_width = 16
config.frame_size = (1920, 1080)
config.output_file = "gradient_descent"


def loss(x: float) -> float:
    return (x - 3) ** 2 + 1


def d_loss(x: float) -> float:
    return 2 * (x - 3)


class GradientDescent(Scene):
    def construct(self) -> None:
        self.add(Title("Градиентный спуск"))

        start = 1.1
        steps = []
        x = start
        for _ in range(8):
            steps.append(-0.2 * d_loss(x))
            x += steps[-1]

        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 6, 1],
            x_length=6,
            y_length=6,
        ).shift(1 * DOWN)
        line = axes.plot(loss, x_range=[start, start + sum(steps)])
        x_label = axes.get_x_axis_label(MathTex(r"x"))
        y_label = axes.get_y_axis_label(MathTex(r"f(x)"))

        markers = []
        dots = []
        x = start

        for step in steps:
            point = axes.c2p(x, loss(x))
            markers.append(axes.get_line_from_axis_to_point(0, point))
            dots.append(Dot(point, color=RED, z_index=1))
            x += step

        self.add(axes, line, x_label, y_label, *markers, dots[-1])


if __name__ == "__main__":
    GradientDescent().render()
