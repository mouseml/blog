from manim import *

config.frame_height = 9
config.frame_width = 16
config.frame_rate = 60
config.frame_size = (1920, 1080)
config.output_file = "eda_distributions.png"


def get_bin(width: float, height: float) -> Mobject:
    return Rectangle(width=width, height=height, fill_color=RED, fill_opacity=1, stroke_width=0, z_index=-1)


class EDADistributions(Scene):
    def construct(self):
        self.add(Title("Анализ распределения"))

        axes1 = Axes(
            x_range=[0, 999, 200],
            y_range=[0, 49, 10],
            x_length=7,
            y_length=5,
            x_axis_config={"numbers_to_include": [0], "numbers_to_exclude": []},
        ).move_to(1 * DOWN + 6.4 * LEFT, LEFT)
        title1 = Tex("Стоимость билета, USD", font_size=40).move_to(axes1.get_center() + 3.25 * UP)
        axes1.add_coordinates()

        dx = axes1.c2p(1, 0)[0] - axes1.c2p(0, 0)[0]
        dy = axes1.c2p(0, 1)[1] - axes1.c2p(0, 0)[1]
        bins1 = []

        for x, y in enumerate([25, 30, 15, 10, 6, 4, 0, 1, 4]):
            bin = get_bin(100 * dx, y * dy)  # noqa
            bin.move_to(axes1.c2p(100 * x, 0), DL)
            bins1.append(bin)

        axes2 = Axes(
            x_range=[0, 4, 5],
            y_range=[0, 49, 10],
            x_length=5,
            y_length=5,
            x_axis_config={"include_tip": False}
        ).move_to(0.75 * DOWN + 1.6 * RIGHT, LEFT)
        title2 = Tex("Аэропорт прибытия", font_size=40).move_to(axes2.get_center() + 3 * UP)
        axes2.add_coordinates([], None)

        dx = axes2.c2p(1, 0)[0] - axes2.c2p(0, 0)[0]
        dy = axes2.c2p(0, 1)[1] - axes2.c2p(0, 0)[1]
        bins2 = []

        for i, y in enumerate([40, 35, 23, 2]):
            bin = get_bin(0.6 * dx, y * dy)  # noqa
            bin.move_to(axes2.c2p(1 * (i + 0.5), 0), DOWN)
            bins2.append(bin)

        labels = []

        for i, x in enumerate(["SVO", "DME", "VKO", "ZIA"]):
            label = Tex(x, font_size=30)
            label.next_to(axes2.x_axis.number_to_point(i + 0.5), DOWN, buff=axes2.x_axis.line_to_number_buff)
            labels.append(label)

        self.add(axes1, axes2)
        self.add(title1, title2)
        self.add(*bins1, *bins2, *labels)


if __name__ == "__main__":
    EDADistributions().render()
