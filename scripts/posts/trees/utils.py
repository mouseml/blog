from pathlib import Path
from typing import Any

import pandas as pd
from manim import *
from enum import StrEnum

from manim.typing import Point3DLike

DOT_RADIUS = 0.1
STROKE_WIDTH = 2
FONT_SIZE = 18
FONT = "JetBrains Mono NL"
APPEND_CHARS = "Ăğ"


class TextAlign(StrEnum):
    """Text alignment."""

    LEFT = "LEFT"
    CENTER = "CENTER"
    RIGHT = "RIGHT"


def set_defaults() -> None:
    """Set default values."""
    Text.set_default(font=FONT, font_size=FONT_SIZE)
    Rectangle.set_default(stroke_width=STROKE_WIDTH)
    Dot.set_default(radius=DOT_RADIUS)
    Line.set_default(stroke_width=STROKE_WIDTH)
    Axes.set_default(
        axis_config={"tip_width": 0.15, "tip_height": 0.15, "tick_size": 0.1}
    )
    Arrow.set_default(
        buff=0, stroke_width=STROKE_WIDTH, tip_length=0.25, tip_style={"width": 0.15}
    )


def set_config(output_filename: str) -> None:
    """Set configuration."""
    config.frame_height = 9
    config.frame_width = 16
    config.frame_rate = 60
    config.frame_size = (1920, 1080)
    config.output_file = Path(output_filename).stem


def get_labeled_cell(
    label_text: Any,
    height: float,
    width: float,
    text_align: TextAlign = TextAlign.CENTER,
) -> VGroup:
    """Return labeled cell."""
    cell = Rectangle(
        width=width, height=height, fill_color=BLACK, fill_opacity=1, z_index=-3
    )

    if text_align == TextAlign.LEFT:
        label = Text(str(label_text) + APPEND_CHARS, z_index=-2)
        label[-2:].set_opacity(0)
        label.move_to(cell.get_left() + 0.2 * RIGHT, LEFT)
    elif text_align == TextAlign.CENTER:
        label = Text(APPEND_CHARS[0] + str(label_text) + APPEND_CHARS[1], z_index=-2)
        label[0].set_opacity(0)
        label[-1].set_opacity(0)
    else:
        label = Text(
            APPEND_CHARS + str(label_text),
            t2c={x: BLACK for x in APPEND_CHARS},
            z_index=-2,
        )
        label[:2].set_opacity(0)
        label.move_to(cell.get_right() - 0.2 * RIGHT, RIGHT)

    return VGroup(cell, label)


def get_table_row(
    values: pd.Series,
    cell_height: float,
    cell_width: list[float],
    text_align: TextAlign | list[TextAlign] = TextAlign.CENTER,
) -> VGroup:
    """Return table row."""
    if not isinstance(text_align, list):
        text_align = [text_align] * len(values)
    cells = []
    offset = 0
    for i in range(len(values)):
        cell = get_labeled_cell(
            values.iloc[i],
            height=cell_height,
            width=cell_width[i],
            text_align=text_align[i],
        )
        offset += cell_width[i]
        cell.move_to(offset * RIGHT, RIGHT)
        cells.append(cell)
    return VGroup(*cells).move_to(ORIGIN)


def get_table(
    data: pd.DataFrame,
    cell_height: float | list[float],
    cell_width: float | list[float],
    text_align: TextAlign | list[TextAlign] = TextAlign.CENTER,
) -> VGroup:
    """Return table."""
    if not isinstance(cell_height, list):
        cell_height = [cell_height] * (data.shape[0] + 1)
    if not isinstance(cell_width, list):
        cell_width = [cell_width] * data.shape[1]
    rows = [
        get_table_row(
            data.columns.to_series(),
            cell_height=cell_height[0],
            cell_width=cell_width,
            text_align=text_align,
        )
    ]
    for i in range(len(data)):
        row = get_table_row(
            data.iloc[i],
            cell_height=cell_height[i + 1],
            cell_width=cell_width,
            text_align=text_align,
        )
        row.shift((i + 1) * cell_height[i + 1] * DOWN)
        rows.append(row)
    return VGroup(*rows).move_to(ORIGIN)


def get_labeled_arrow(label: Any, start: Point3DLike, end: Point3DLike) -> VGroup:
    """Return labeled arrow."""
    arrow = Arrow(start=start, end=end, z_index=-4)
    label = Text(str(label), z_index=-2)
    label_box = Rectangle(
        width=label.get_width() + 0.1,
        height=label.get_height() + 0.1,
        fill_color=BLACK,
        fill_opacity=1,
        stroke_width=0,
        z_index=-3,
    )
    label_box.move_to(arrow.get_center())
    label.move_to(label_box.get_center())
    return VGroup(arrow, label, label_box)
