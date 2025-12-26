import pandas as pd
from manim import *

from scripts.posts.trees.utils import get_labeled_cell, get_labeled_arrow
from utils import set_defaults, set_config, get_table, TextAlign

CELL_HEIGHT = 0.5
CELL_WIDTHS = [2.3, 1.5, 1.7, 1.3]


class Table(Scene):
    def __init__(self, data_path: str) -> None:
        super().__init__()
        self._data_path = data_path

    def construct(self):
        data = pd.read_csv(self._data_path)
        table = get_table(
            data,
            cell_height=CELL_HEIGHT,
            cell_width=CELL_WIDTHS,
            text_align=TextAlign.LEFT,
        )
        self.add(table)


class TableSplit(Scene):
    def __init__(self, data_path: str, threshold: int) -> None:
        super().__init__()
        self._data_path = data_path
        self._threshold = threshold

    def construct(self) -> None:
        data = pd.read_csv(self._data_path)

        threshold = self._threshold
        data1 = data[data["Лекции"] <= threshold]
        data2 = data[data["Лекции"] > threshold]

        table1 = get_table(
            data1,
            cell_height=CELL_HEIGHT,
            cell_width=CELL_WIDTHS,
            text_align=TextAlign.LEFT,
        ).move_to(0.5 * LEFT + 1.5 * UP, UR)
        table2 = get_table(
            data2,
            cell_height=CELL_HEIGHT,
            cell_width=CELL_WIDTHS,
            text_align=TextAlign.LEFT,
        ).move_to(0.5 * RIGHT + 1.5 * UP, UL)

        rule = get_labeled_cell(
            f"лекции > {threshold}?", width=2.5, height=CELL_HEIGHT
        ).move_to(2.5 * UP, DOWN)

        arrow1 = get_labeled_arrow("нет", rule.get_bottom(), table1.get_top())
        arrow2 = get_labeled_arrow("да", rule.get_bottom(), table2.get_top())

        self.add(table1, table2, rule, arrow1, arrow2)


if __name__ == "__main__":
    set_defaults()

    for filename in ("data1", "data2", "data2_right", "data3"):
        set_config(filename)
        Table(f"data/{filename}.csv").render()

    for threshold in (3, 4, 7):
        set_config(f"data1_split{threshold}")
        TableSplit("data/data1.csv", threshold=threshold).render()

    set_config("data2_split4")
    TableSplit("data/data2.csv", 4).render()
