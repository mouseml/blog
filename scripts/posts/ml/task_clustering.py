import random

from manim import *

config.frame_height = 9
config.frame_width = 16
config.frame_rate = 60
config.frame_size = (1920, 1080)
config.output_file = "task_clustering.png"

FONT_SIZE = 35


def get_point_cloud(center: tuple[float, float, float], density: float, n: int = 50) -> list[tuple[float, float, float]]:
    spread = 1 / density
    cx, cy, cz = center
    points = []

    for _ in range(n):
        x = random.uniform(cx - spread, cx + spread)
        y = random.uniform(cy - spread, cy + spread)
        z = random.uniform(cz - spread, cz + spread)
        points.append((x, y, z))

    return points


class TaskClustering(ThreeDScene):
    def construct(self):
        self.add_fixed_in_frame_mobjects(Title("Кластеризация"))
        self.set_camera_orientation(phi=75 * DEGREES, theta=20 * DEGREES, focal_distance=1000)
        axes = ThreeDAxes(
            x_range=[0, 10, 10],
            y_range=[0, 10, 10],
            z_range=[0, 10, 10],
            x_length=6,
            y_length=6,
            z_length=4,
        ).shift(2.7 * IN)

        dots1 = [Dot3D(axes.c2p(*x), color=RED) for x in get_point_cloud((4, 0, 1), 0.4)]
        dots2 = [Dot3D(axes.c2p(*x), color=BLUE) for x in get_point_cloud((2, 8, 8), 0.4)]
        dots3 = [Dot3D(axes.c2p(*x), color=GREEN) for x in get_point_cloud((12, 8, 6), 0.4)]

        self.add(axes)
        self.add_fixed_in_frame_mobjects(Tex("Звонки", font_size=FONT_SIZE).move_to(4 * RIGHT + 2.8 * DOWN))
        self.add_fixed_in_frame_mobjects(Tex("Интернет", font_size=FONT_SIZE).move_to(4 * LEFT + 3.7 * DOWN))
        self.add_fixed_in_frame_mobjects(Tex("Возраст", font_size=FONT_SIZE).move_to(3 * LEFT + 2.5 * UP))
        self.add(*dots1, *dots2, *dots3)


if __name__ == "__main__":
    TaskClustering().render()
