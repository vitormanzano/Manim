from manim import *

class Exercise(Scene):
    def construct(self):
        circle = Circle()
        #.shift(posição: UP,DOWN ETC)
        circle.set_fill(GREEN,opacity=0.5)
        circle.set_stroke(color = WHITE,width = 8)
        circle_label = Text('Círculo', font_size=40).next_to(circle,DOWN)

        self.play(Create(circle),Write(circle_label))
        self.wait()

        triangle =Triangle()
        triangle.set_fill(RED,opacity=0.5)
        triangle.set_stroke(color = WHITE,width = 8)
        triangle_label = Text('Triângulo',font_size=40).next_to(triangle,DOWN)

        self.play((ReplacementTransform(circle,triangle)),ReplacementTransform(circle_label,triangle_label))
        self.wait()
        self.play(FadeOut(triangle,triangle_label)) 

        self.wait()
        finalizacao = Text('Terminei minha primeira animação!',font_size = 50).shift(2*UP)
        
        self.play(FadeIn(finalizacao))

