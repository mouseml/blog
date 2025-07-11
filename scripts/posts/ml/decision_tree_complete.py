from manim import *

config.frame_height = 9
config.frame_width = 16
config.frame_rate = 60
config.frame_size = (1920, 1080)
config.output_file = "decision_tree_complete.png"

WIDTH = 3.5
HEIGHT = 1.1
FONT_SIZE = 35


def get_leaf_label(area: int, distance: int, price: int) -> Mobject:
    return Tex(f"{area} м$^2$ {distance} км \n\n {price} млн", font_size=FONT_SIZE)


class DecisionTreeComplete(Scene):
    def construct(self) -> None:
        self.add(Title("Дерево решений"))

        root_label1 = Tex(r"Дальность $\le$ 2 км", font_size=FONT_SIZE).move_to(2 * UP)
        root_box1 = Rectangle(width=3.5, height=1.0).move_to(root_label1)
        root_label2 = Tex(r"Площадь $\le$ 60 м$^2$", font_size=FONT_SIZE).move_to(3.35 * LEFT)
        root_box2 = Rectangle(width=3.5, height=1.0).move_to(root_label2)
        leaf_labels = [
            Tex("15 млн", font_size=FONT_SIZE).shift(4.7 * LEFT + 3 * DOWN),
            Tex("25 млн", font_size=FONT_SIZE).shift(0.5 * LEFT + 2 * DOWN),
            Tex("10 млн", font_size=FONT_SIZE).move_to(3.35 * RIGHT),
        ]
        leaf_boxes = [Rectangle(width=2.5, height=1.0).move_to(x.get_center()) for x in leaf_labels]
        arrows = [
            Arrow(root_box1.get_corner(DL), root_box2.get_top() + 0.1 * UP, buff=0),
            Arrow(root_box1.get_corner(DR), leaf_boxes[2].get_top() + 0.1 * UP, buff=0),
            Arrow(root_box2.get_bottom(), leaf_boxes[0].get_top() + 0.1 * UP, buff=0),
            Arrow(root_box2.get_right(), leaf_boxes[1].get_top() + 0.1 * UP, buff=0),
        ]
        arrow_labels = [
            Tex("Да", font_size=FONT_SIZE).shift(3 * LEFT + 1.5 * UP),
            Tex("Нет", font_size=FONT_SIZE).shift(3 * RIGHT + 1.5 * UP),
            Tex("Да", font_size=FONT_SIZE).shift(5 * LEFT + 1.5 * DOWN),
            Tex("Нет", font_size=FONT_SIZE).shift(0.5 * LEFT + 0.5 * DOWN),
        ]

        self.add(root_label1, root_label2)
        self.add(root_box1, root_box2)
        self.add(*arrows, *arrow_labels)
        self.add(*leaf_labels, *leaf_boxes)


if __name__ == "__main__":
    DecisionTreeComplete().render()
