from manim import *

config.frame_height = 9
config.frame_width = 16
config.frame_rate = 60
config.frame_size = (1920, 1080)


class IrisOverview(Scene):
    def construct(self):
        self.add(Title("Классификация ирисов"))

        iris1 = ImageMobject("images/iris-setosa.jpg").scale_to_fit_width(4).shift(5 * LEFT + 0.8 * DOWN)
        iris2 = ImageMobject("images/iris-versicolor.jpg").scale_to_fit_width(4).shift(5 * RIGHT + 0.8 * DOWN)
        iris3 = ImageMobject("images/iris-virginica.jpg").scale_to_fit_width(4).shift(0.8 * DOWN)

        label1 = Tex("Щетинистый (setósa)", font_size=35).next_to(iris1, UP)
        label2 = Tex("Разноцветный (versicolor)", font_size=35).next_to(iris3, UP)
        label3 = Tex("Виргинский (virginica)", font_size=35).next_to(iris2, UP)

        self.add(iris1, iris2, iris3)
        self.add(label1, label2, label3)


if __name__ == "__main__":
    IrisOverview().render()
