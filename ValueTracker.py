from manim import *

class CenaValueTracker(Scene):
    def construct(self):
        circle_radius = ValueTracker(1)
        circle = Circle(radius = circle_radius.get_value()).set_fill(PINK, opacity = 0.5)
        circle.add_updater(lambda m: m.become(Circle(radius = circle_radius.get_value()).set_fill(PINK, opacity = 0.5))) #Torna ele um objeto atualizavel

        radius_label = MathTex('r = 1.00')
        radius_label.add_updater(lambda m: m.become(MathTex(f'r = {circle_radius.get_value():.2f}')))
        radius_label.next_to(circle, UP)

        self.play(Create(circle), Create(radius_label))
        self.play(circle_radius.animate.set_value(2), run_time = 2, rate_func = there_and_back)
        self.play(circle_radius.animate.set_value(0.5), run_time = 2, rate_func = smooth)
        self.wait()

class CenaMoveAlongPath(Scene):
    def construct(self):
        path = Ellipse(width = 4, height = 2, color = BLUE)
        self.play(Create(path))

        dot = Dot(color = RED).move_to(path.get_center())

        self.play(MoveAlongPath(dot, path), run_time = 4, rate_func = linear)
        self.wait()