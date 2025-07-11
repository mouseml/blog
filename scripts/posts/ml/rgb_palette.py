from manim import *

config.frame_height = 9
config.frame_width = 16
config.frame_rate = 60
config.frame_size = (1920, 1080)
config.output_file = "rgb_palette.png"

FONT_SIZE = 40


class RGBPalette(Scene):
    def construct(self):
        self.add(Title("Палитра RGB"))
        # self.add(NumberPlane().set_opacity(0.2))

        image = ImageMobject("images/cookie_monster.jpg").scale_to_fit_width(5)
        image.move_to(6 * LEFT + 0.5 * DOWN, LEFT)

        image_r = ImageMobject("images/cookie_monster_r.jpg", z_index=0).scale_to_fit_width(5)
        image_g = ImageMobject("images/cookie_monster_g.jpg", z_index=-1).scale_to_fit_width(5)
        image_b = ImageMobject("images/cookie_monster_b.jpg", z_index=-2).scale_to_fit_width(5)

        image_r.move_to(1.5 * DOWN, LEFT)
        image_g.move_to(1 * RIGHT + 0.5 * DOWN, LEFT)
        image_b.move_to(2 * RIGHT + 0.5 * UP, LEFT)

        label_r = Tex("R", font_size=FONT_SIZE).move_to(image_r.get_corner(UR) + 0.5 * LEFT + 0.5 * DOWN)
        label_g = Tex("G", font_size=FONT_SIZE).move_to(image_g.get_corner(UR) + 0.5 * LEFT + 0.5 * DOWN)
        label_b = Tex("B", font_size=FONT_SIZE).move_to(image_b.get_corner(UR) + 0.5 * LEFT + 0.5 * DOWN)

        self.add(image, image_r, image_g, image_b)
        self.add(label_r, label_g, label_b)


if __name__ == "__main__":
    RGBPalette().render()
