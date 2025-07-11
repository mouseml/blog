import random

from manim import *

config.frame_height = 9
config.frame_width = 16
config.frame_rate = 60
config.frame_size = (1920, 1080)
config.output_file = "decision_tree_overfit"

WIDTH = 0.4
generator = random.Random(3)


def get_block() -> Mobject:
    return Rectangle(width=WIDTH, height=WIDTH / 2, stroke_width=2, color=WHITE, fill_color=BLACK, fill_opacity=1)


def build_with_bounding_box(node, left_bound, right_bound, level, remaining_depth, all_nodes, all_edges):
    if remaining_depth <= 0:
        return

    # Calculate center and boundaries for children
    center = (left_bound + right_bound) / 2
    vertical_spacing = WIDTH * 2

    # Create children
    left_child = get_block()
    right_child = get_block()

    # Position children at centers of their bounding boxes
    left_center = (left_bound + center) / 2
    right_center = (center + right_bound) / 2

    left_child.move_to([left_center, node.get_center()[1] - vertical_spacing, 0])
    right_child.move_to([right_center, node.get_center()[1] - vertical_spacing, 0])

    # Create edges
    left_edge = Line(node.get_bottom(), left_child.get_top(), stroke_width=2)
    right_edge = Line(node.get_bottom(), right_child.get_top(), stroke_width=2)

    # Add to collections
    all_nodes.extend([left_child, right_child])
    all_edges.extend([left_edge, right_edge])

    # Recursively build subtrees with subdivided bounding boxes
    if generator.random() > (0.1 + (level * 0.1)):
        build_with_bounding_box(
            left_child, left_bound, center, level + 1, remaining_depth - 1, all_nodes, all_edges
        )
    if generator.random() > (0.1 + (level * 0.1)):
        build_with_bounding_box(
            right_child, center, right_bound, level + 1, remaining_depth - 1, all_nodes, all_edges
        )


def create_tree_with_bounding_boxes(depth: int) -> VGroup:
    # Calculate total width needed (width for each leaf + some padding)
    num_leaves = 2 ** (depth - 1)
    leaf_width = WIDTH * 1.2  # Width per leaf slot
    total_width = num_leaves * leaf_width

    # Create root node at center with full width bounding box
    root = get_block()

    all_nodes = [root]
    all_edges = []

    # Build tree recursively with bounding boxes
    build_with_bounding_box(
        node=root,
        left_bound=-total_width / 2,
        right_bound=total_width / 2,
        level=0,
        remaining_depth=depth - 1,
        all_nodes=all_nodes,
        all_edges=all_edges
    )

    return VGroup(root, *all_nodes, *all_edges)


class DecisionTreeOverfit(Scene):
    def construct(self) -> None:
        self.add(Title("Переобучение"))

        # Specify the depth of the tree here
        tree_depth = 6

        # Create the tree using bounding box method
        tree = create_tree_with_bounding_boxes(tree_depth).move_to(0.5 * DOWN)

        # Add all nodes and edges to the scene
        self.add(tree)


if __name__ == "__main__":
    DecisionTreeOverfit().render()
