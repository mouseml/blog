import random

from manim import *

config.frame_height = 9
config.frame_width = 16
config.frame_rate = 30
config.frame_size = (1920, 1080)
config.output_file = "array_storage"

SIDE = 0.5
ROWS = 11
COLS = 10
generator = random.Random(0)


def get_memory_cell(size: int) -> Mobject:
    return Rectangle(height=SIDE, width=size * SIDE, stroke_width=2, color=GRAY, fill_color=BLACK, fill_opacity=1)


def get_memory_row(sizes: list[int]) -> VGroup:
    cells = []
    for i, size in enumerate(sizes):
        cells.append(get_memory_cell(size).move_to(sum(sizes[:i]) * SIDE * RIGHT, LEFT))
    return VGroup(*cells)


def get_random_sizes() -> list[int]:
    result = []
    total = 0
    while total < COLS:
        if generator.random() < 0.7 or COLS - total == 1:
            result.append(1)
            total += 1
        else:
            max_val = min(COLS - total, 3)
            val = generator.randint(2, max_val)
            result.append(val)
            total += val
    return result


def get_memory_table() -> VGroup:
    sizes = [get_random_sizes() for _ in range(5)] + [[1] * COLS] + [get_random_sizes() for _ in range(5)]
    return VGroup(*(get_memory_row(x).shift(i * SIDE * DOWN) for i, x in enumerate(sizes)))


def get_label(str_: str) -> Mobject:
    return Text(str_, font_size=30)


class ArrayStorage(Scene):
    def construct(self) -> None:
        self.add(Title("Хранение в оперативной памяти"))

        memory_tables = [
            get_memory_table().move_to(6 * LEFT + 3 * DOWN, DL),
            get_memory_table().move_to(1 * RIGHT + 3 * DOWN, DL),
        ]
        labels = [
            get_label("Тензоры").next_to(memory_tables[0], DOWN),
            get_label("Списки").next_to(memory_tables[1], DOWN),
        ]
        memory_tables[0][5][1:-2].set_z_index(1).set_color(WHITE).set_fill(RED, opacity=1)
        memory_tables[1][5][1:-2].set_z_index(1).set_color(WHITE).set_fill(GRAY, opacity=1)

        value_cells = [
            memory_tables[1][1][0],
            memory_tables[1][0][1],
            memory_tables[1][2][3],
            memory_tables[1][2][5],
            memory_tables[1][7][1],
            memory_tables[1][8][3],
            memory_tables[1][10][5],
        ]
        for cell in value_cells:
            cell.set_z_index(1).set_color(WHITE).set_fill(RED, opacity=1)
        lines = []
        for array_cell, value_cell in zip(memory_tables[1][5][1:-5], value_cells[:4]):
            lines.append(DashedLine(array_cell.get_top(), value_cell.get_bottom(), buff=0, z_index=1))
        for array_cell, value_cell in zip(memory_tables[1][5][5:8], value_cells[4:]):
            lines.append(DashedLine(array_cell.get_bottom(), value_cell.get_top(), buff=0, z_index=1))

        self.add(*memory_tables, *labels, *lines)


if __name__ == "__main__":
    ArrayStorage().render()
