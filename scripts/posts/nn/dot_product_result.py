from manim import *

config.frame_height = 9
config.frame_width = 16
config.frame_rate = 60
config.frame_size = (1920, 1080)


class DotProductResult(Scene):
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
            [[0.43, 0.4, 0.6], [0.32, 0.53, 0.98], [0.04, 0.1, 0.2], [0.02, 0.05, 0.1]],
            element_to_mobject_config={"num_decimal_places": 2},
            include_outer_lines=True,
        ).scale(0.7).move_to(2.4 * RIGHT + 0.5 * DOWN, LEFT)

        x_table.add(x_table.get_cell((1, 1), color=WHITE).set_fill(RED, opacity=0.5).set_z_index(-1))
        x_table.add(x_table.get_cell((1, 2), color=WHITE).set_fill(RED, opacity=0.5).set_z_index(-1))
        w_table.add(w_table.get_cell((1, 1), color=WHITE).set_fill(RED, opacity=0.5).set_z_index(-1))
        w_table.add(w_table.get_cell((2, 1), color=WHITE).set_fill(RED, opacity=0.5).set_z_index(-1))
        y_table.add(y_table.get_cell((1, 1), color=WHITE).set_fill(RED, opacity=0.5).set_z_index(-1))

        x_title = MathTex(r"\mathbf{X}").next_to(x_table, UP)
        w_title = MathTex(r"\mathbf{W}").next_to(w_table, UP)

        multiply = MathTex(r"\times").next_to(x_table, RIGHT, buff=0.5)
        equals = MathTex("=").next_to(w_table, RIGHT, buff=0.5)

        self.add(x_table, w_table, y_table)
        self.add(x_title, w_title)
        self.add(multiply, equals)


if __name__ == "__main__":
    DotProductResult().render()
