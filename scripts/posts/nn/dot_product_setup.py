from manim import *

config.frame_height = 9
config.frame_width = 16
config.frame_rate = 60
config.frame_size = (1920, 1080)


class DotProductSetup(Scene):
    def construct(self) -> None:
        self.add(Title("Умножение матриц"))

        x_table = DecimalTable(
            [[0.4, 0.5], [0.9, 0.2], [0.2, 0.0], [0.1, 0.0]],
            include_outer_lines=True,
        ).scale(0.7).move_to(6.8 * LEFT + 0.5 * DOWN, LEFT)
        w_table = DecimalTable(
            [[0.2, 0.5, 1.0], [0.7, 0.4, 0.4]],
            include_outer_lines=True,
        ).scale(0.7).move_to(2.9 * LEFT + 0.5 * DOWN, LEFT)
        y_table = DecimalTable(
            [[0] * 3] * 4,
            element_to_mobject_config={"num_decimal_places": 2},
            include_outer_lines=True,
        ).scale(0.7).move_to(2.4 * RIGHT + 0.5 * DOWN, LEFT)
        for x in y_table.get_entries():
            x.set_fill(opacity=0)
        y_table.add(y_table.get_cell((1, 1), color=WHITE).set_fill(RED, opacity=0.5).set_z_index(-1))

        x_title = MathTex(r"\mathbf{X}").next_to(x_table, UP)
        w_title = MathTex(r"\mathbf{W}").next_to(w_table, UP)

        multiply = MathTex(r"\times").next_to(x_table, RIGHT, buff=0.5)
        equals = MathTex("=").next_to(w_table, RIGHT, buff=0.5)

        self.add(x_table, w_table, y_table)
        self.add(x_title, w_title)
        self.add(multiply, equals)


if __name__ == "__main__":
    DotProductSetup().render()
