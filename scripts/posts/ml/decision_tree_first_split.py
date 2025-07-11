from manim import *

config.frame_height = 9
config.frame_width = 16
config.frame_rate = 60
config.frame_size = (1920, 1080)
config.output_file = "decision_tree_first_split.png"

WIDTH = 3.5
HEIGHT = 1.1
FONT_SIZE = 35


def get_leaf_label(area: int, distance: int, price: int) -> Mobject:
    return Tex(f"{area} м$^2$ {distance} км \n\n {price} млн", font_size=FONT_SIZE)


class DecisionTreeFirstSplit(Scene):
    def construct(self) -> None:
        self.add(Title("Дерево решений"))

        root_label = Tex(r"Дальность $\le$ 2 км", font_size=FONT_SIZE).move_to(0.5 * UP)
        root_box = Rectangle(width=3.5, height=1.0).move_to(root_label)
        leaf_labels = [
            get_leaf_label(35, 1, 15).shift(4.7 * LEFT + 1.5 * DOWN),
            get_leaf_label(70, 1, 25).shift(2 * LEFT + 1.5 * DOWN),
            get_leaf_label(45, 5, 8).shift(2 * RIGHT + 1.5 * DOWN),
            get_leaf_label(65, 7, 12).shift(4.7 * RIGHT + 1.5 * DOWN),
        ]
        leaf_boxes = [Rectangle(width=2.5, height=1.0).move_to(x.get_center()) for x in leaf_labels]
        arrows = [
            Arrow(root_box.get_corner(DL), leaf_boxes[0].get_corner(UR) + 0.1 * RIGHT + 0.1 * UP, buff=0),
            Arrow(root_box.get_corner(DR), leaf_boxes[3].get_corner(UL) + 0.1 * LEFT + 0.1 * UP, buff=0),
        ]
        arrow_labels = [
            Tex("Да", font_size=FONT_SIZE).shift(3 * LEFT),
            Tex("Нет", font_size=FONT_SIZE).shift(3 * RIGHT),
        ]

        self.add(root_label, root_box)
        self.add(*arrows, *arrow_labels)
        self.add(*leaf_labels, *leaf_boxes)


if __name__ == "__main__":
    DecisionTreeFirstSplit().render()
