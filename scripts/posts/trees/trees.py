from manim import *
from manim.typing import Vector3D

from scripts.posts.trees.utils import (
    set_defaults,
    set_config,
    get_labeled_cell,
    get_labeled_arrow,
)

BLOCK_HEIGHT = 0.5
BLOCK_WIDTH = 2.5


def get_tree_block(label: str) -> VGroup:
    return get_labeled_cell(label, height=BLOCK_HEIGHT, width=BLOCK_WIDTH)


class Tree(Scene):
    def __init__(
        self, blocks: list[tuple[str, Vector3D]], arrows: list[tuple[str, int, int]]
    ) -> None:
        super().__init__()
        self._blocks = blocks
        self._arrows = arrows

    def construct(self) -> None:
        blocks = [
            get_tree_block(label).move_to(position, DL)
            for label, position in self._blocks
        ]
        arrows = [
            get_labeled_arrow(
                label, start=blocks[i].get_bottom(), end=blocks[j].get_top()
            )
            for label, i, j in self._arrows
        ]
        self.add(*blocks, *arrows)


if __name__ == "__main__":
    set_defaults()

    blocks = [
        ("лекции > 4?", 0.5 * UP + 1.25 * LEFT),
        ("незачет", DOWN + 3 * LEFT),
        ("зачет", DOWN + 0.5 * RIGHT),
    ]
    arrows = [("нет", 0, 1), ("да", 0, 2)]
    set_config("tree1")
    Tree(blocks=blocks, arrows=arrows).render()

    blocks = [
        ("лекции > 4?", 0.5 * UP + 1.25 * LEFT),
        ("незачет (100%)", DOWN + 3 * LEFT),
        ("зачет (67%)", DOWN + 0.5 * RIGHT),
    ]
    arrows = [("нет", 0, 1), ("да", 0, 2)]
    set_config("tree2")
    Tree(blocks=blocks, arrows=arrows).render()

    blocks = [
        ("лекции > 4?", 0.5 * UP + 1.25 * LEFT),
        ("незачет (100%)", DOWN + 3 * LEFT),
        ("семинары > 3?", DOWN + 0.5 * RIGHT),
        ("незачет (100%)", 2.5 * DOWN + LEFT),
        ("зачет (100%)", 2.5 * DOWN + 2.5 * RIGHT),
    ]
    arrows = [("нет", 0, 1), ("да", 0, 2), ("нет", 2, 3), ("да", 2, 4)]
    set_config("tree2_full")
    Tree(blocks=blocks, arrows=arrows).render()

    blocks = [
        ("семинары > 4?", -1.25 * RIGHT + 3.5 * UP),
        ("лекции > 3?", -6 * RIGHT + 2.0 * UP),
        ("лекции > 6?", 3.5 * RIGHT + 2.0 * UP),
        ("незачет (100%)", -7.5 * RIGHT + 0.5 * UP),
        ("лекции > 6?", -4.5 * RIGHT + 0.5 * UP),
        ("лекции > 3?", 2 * RIGHT + 0.5 * UP),
        ("зачет (100%)", 5 * RIGHT + 0.5 * UP),
        ("семинары > 3?", -6 * RIGHT + DOWN),
        ("незачет (100%)", -3 * RIGHT + DOWN),
        ("зачет (100%)", 0.5 * RIGHT + DOWN),
        ("семинары > 6?", 3.5 * RIGHT + DOWN),
        ("зачет (100%)", -7.5 * RIGHT + 2.5 * DOWN),
        ("лекции > 4?", -4.5 * RIGHT + 2.5 * DOWN),
        ("зачет (100%)", 2 * RIGHT + 2.5 * DOWN),
        ("незачет (100%)", 5 * RIGHT + 2.5 * DOWN),
        ("незачет (100%)", -6 * RIGHT + 4.0 * DOWN),
        ("зачет (100%)", -3 * RIGHT + 4.0 * DOWN),
    ]
    arrows = [
        ("нет", 0, 1),
        ("да", 0, 2),
        ("нет", 1, 3),
        ("да", 1, 4),
        ("нет", 2, 5),
        ("да", 2, 6),
        ("нет", 4, 7),
        ("да", 4, 8),
        ("нет", 5, 9),
        ("да", 5, 10),
        ("нет", 7, 11),
        ("да", 7, 12),
        ("нет", 10, 13),
        ("да", 10, 14),
        ("нет", 12, 15),
        ("да", 12, 16),
    ]
    set_config("tree3_overfit")
    Tree(blocks=blocks, arrows=arrows).render()

    blocks = [
        ("семинары > 4?", -1.25 * RIGHT + UP),
        ("лекции > 3?", 4.5 * LEFT + 0.5 * DOWN),
        ("лекции > 6?", 2 * RIGHT + 0.5 * DOWN),
        ("незачет (100%)", 6 * LEFT + 2 * DOWN),
        ("незачет (60%)", 3 * LEFT + 2 * DOWN),
        ("зачет (50%)", 0.5 * RIGHT + 2 * DOWN),
        ("зачет (100%)", 3.5 * RIGHT + 2 * DOWN),
    ]
    arrows = [
        ("нет", 0, 1),
        ("да", 0, 2),
        ("нет", 1, 3),
        ("да", 1, 4),
        ("нет", 2, 5),
        ("да", 2, 6),
    ]
    set_config("tree3_max_depth")
    Tree(blocks=blocks, arrows=arrows).render()

    blocks = [
        ("семинары > 4?", -1.25 * RIGHT + 0.5 * UP),
        ("незачет (67%)", 3 * LEFT + DOWN),
        ("зачет (67%)", 0.5 * RIGHT + DOWN),
    ]
    arrows = [
        ("нет", 0, 1),
        ("да", 0, 2),
    ]
    set_config("tree3_min_samples_leaf")
    Tree(blocks=blocks, arrows=arrows).render()
