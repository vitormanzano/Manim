from manim import *

class PositioningObjects(Scene):
    def construct(self):
        circle = Circle().set_fill(PINK,opacity=0.5)
        circle.set_stroke(WHITE,width=4)
        
        square = Square().set_fill(BLUE,opacity=0.5)
        square.set_stroke(WHITE,width=4)
        
        triangle = Triangle().set_fill(GREEN,opacity=0.5)
        triangle.set_stroke(WHITE,width=4)

        square.next_to(circle,RIGHT,buff=0.5)
        triangle.next_to(circle,LEFT,buff=0.5)

        circle_moved = Circle(color=WHITE).move_to(triangle)
        circle_moved.align_to(triangle,DOWN)
        square_aligned = Square(side_length=0.75)
        square_aligned.align_to(circle,UP)

        circle_shifted = Circle().set_fill(ORANGE,opacity=0.5)
        circle_shifted.shift(3*UP)

        line = Line(circle.get_right(),square.get_left(),color=YELLOW)

        self.play(Create(circle),Create(square),Create(triangle))
        self.wait()
        
        self.play(Create(line))
        self.wait()
        
        self.play(Create(circle_moved),Create(square_aligned))
        self.wait()
        self.play(DrawBorderThenFill(circle_shifted))
        
        self.wait(2)

class AnimatedTransformations(Scene):
    def construct(self):
        square = Square().set_fill(BLUE,opacity=0.5)
        square.set_stroke(WHITE,width=4)
        circle = Circle().set_fill(RED,opacity=0.5)
        circle.set_stroke(WHITE,width=4)
        
        self.play(Create(square))
        self.wait()

        self.play(square.animate.rotate(PI/4).scale(1.5))
        self.wait()

        self.play(ReplacementTransform(square,circle))
        self.wait()

        self.play(circle.animate.set_fill(YELLOW,opacity=0.5).set_stroke(RED,width=4).shift(2*UP),run_time =2 )
        self.wait()

        triangle = Triangle().set_fill(GREEN,opacity=0.5)

        self.play(Transform(circle,triangle)) 
        self.play(triangle.animate.shift(2*LEFT).rotate(PI/3))
        
        self.wait()

        final_circle = Circle().set_fill(PINK,opacity=0.5).move_to(triangle)

        triangle.set_z_index(0)
        final_circle.set_z_index(-1)
        
        self.play(ReplacementTransform(triangle,final_circle))
        self.play(final_circle.animate.move_to(ORIGIN))
        self.wait()

        text1 = Text('Hello')
        text2 = Text('World')
        text3 = Text('Manim')

        text_group = VGroup(text1,text2,text3).arrange(RIGHT,buff =0.5)
        
        text_group.to_edge(DOWN)

        self.play(Write(text_group))
        self.wait()
