from manim import *

config.frame_height = 9
config.frame_width = 16
config.frame_rate = 60
config.frame_size = (1920, 1080)
config.output_file = "eda_correlation_matrix.png"

FONT_SIZE = 35
SIZE = 1


class EDACorrelationMatrix(Scene):
    def construct(self):
        self.add(Title("Матрица корреляции"))

        cells = [
            Square(SIZE, color=WHITE, z_index=-1).shift(j * SIZE * RIGHT + i * SIZE * DOWN)
            for i in range(5) for j in range(5)
        ]
        Group(*cells).move_to(0.5 * DOWN)

        cells = [x for i, x in enumerate(cells) if i not in {1, 2, 3, 4, 7, 8, 9, 13, 14, 19, 20}]

        labels = []
        for i, value in enumerate(["A", "B", 0.9, "C", -0.8, 0.2, "D", 0.1, 0.1, 0.7, "A", "B", "C", "D"]):
            label = Tex(str(value), font_size=FONT_SIZE)
            label.move_to(cells[i].get_center())
            labels.append(label)

        cells[2].set_fill(RED, opacity=0.5)
        cells[4].set_fill(BLUE, opacity=0.5)
        cells[9].set_fill(RED, opacity=0.5)

        self.add(*cells, *labels)


if __name__ == "__main__":
    EDACorrelationMatrix().render()
