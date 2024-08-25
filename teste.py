from manim import * 
import numpy as np

class Exercise1(Scene):
    def construct(self):
        square = Square()
        square.set_fill(ORANGE,opacity=1)
        square.set_stroke(color = WHITE,width=6)
        square_label  =Text('Quadrado',font_size =24).next_to(square,DOWN)

        self.play(Create(square),Write(square_label))
        self.wait(2)

        circle = Circle()
        circle.set_stroke(color = WHITE,width= 6)
        circle.set_fill(BLUE,opacity=0.5)
        circle_label = Text('Círculo',font_size=24).next_to(circle,DOWN)

        self.play(ReplacementTransform(square,circle),ReplacementTransform(square_label,circle_label))
        self.wait(2)        

        pentagon = RegularPolygon(n=5)
        pentagon.set_fill(RED,opacity=0.75)
        pentagon.set_stroke(color = WHITE,width=6)
        pentagon_label = Text('Pentágono',font_size = 24).next_to(pentagon,DOWN)

        self.play(ReplacementTransform(circle,pentagon),ReplacementTransform(circle_label,pentagon_label))
        self.wait(2)

        self.play(FadeOut(pentagon),FadeOut(pentagon_label))
        self.wait(0.5)

        finalizacao = Text('Formas geométricas concluídas!',font_size = 36).shift(2*UP)
        self.play(Write(finalizacao))
        self.wait()
        '''

''' 
class Exercise2(Scene):
    def construct(self):
        line1 = Line(3*LEFT,3*RIGHT).shift(UP)

        line2 = Line(3*RIGHT,3*LEFT).shift(DOWN)
        line1label = Text('Linha 1',font_size=24).next_to(line1,UP)
        line2label = Text('Linha 2',font_size=24).next_to(line2,UP)

        self.play(Create(line1),Write(line1label))
        self.play(Create(line2),Write(line2label))
        self.wait(2)

        arrow1 = Arrow(3*LEFT,3*RIGHT).shift(3*UP+3*LEFT)
        arrow2 = Arrow(3*RIGHT,3*LEFT).shift(3*DOWN+3*RIGHT)
        arrow1label = Text('Seta 1',font_size =24).next_to(arrow1,DOWN)
        arrow2label = Text('Seta 2',font_size = 24).next_to(arrow2,DOWN)

        self.play(Create(arrow1),Write(arrow1label))
        self.play(Create(arrow2),Write(arrow2label))
        self.wait(2)

        dot1 = Dot(line1.get_start(),color = PURPLE)
        dot2 = Dot(line2.get_start(),color = BLUE)
        dot3 = Dot(arrow1.get_start(),color = RED)
        dot4 = Dot(arrow2.get_start(),color = YELLOW)

        dot1label = Text('Ponto 1',font_size=24).next_to(dot1,UP)
        dot2label = Text('Ponto 2',font_size = 24).next_to(dot2,DOWN)
        dot3label = Text('Ponto 3',font_size=24).next_to(dot3,UP)
        dot4label = Text('Ponto 4',font_size=24).next_to(dot4,DOWN)

        self.play(Create(dot1),Write(dot1label))
        self.play(Create(dot2),Write(dot2label))
        self.play(Create(dot3),Write(dot3label))
        self.play(Create(dot4),Write(dot4label))

        self.wait(2)

class Exercise3(Scene):
    def construct(self):
        triangle= Triangle()
        triangle.set_fill(ORANGE,opacity=0.75)
        triangle_label = Text('Triângulo',font_size=24).next_to(triangle,DOWN)

        self.play(Create(triangle),Write(triangle_label))
        self.wait()

        hexagon = RegularPolygon(n=6)
        hexagon.set_fill(GREEN,opacity=0.75)
        hexagon_label = Text('Hexágono',font_size=24).next_to(hexagon,DOWN)

        self.play(ReplacementTransform(triangle,hexagon),ReplacementTransform(triangle_label,hexagon_label))
        self.wait(2)

        circle = Circle()
        circle.set_fill(RED,opacity=0.75).shift(5*RIGHT)
        circle_label = Text('Círculo',font_size=24).next_to(circle,DOWN)

        self.play(Create(circle),Write(circle_label))
        self.wait()

        line1 = Line(hexagon.get_end(),circle.get_left(),color = RED)
        lineLabel =  Text('Conexão',font_size=24).next_to(line1,DOWN)

        self.play(Create(line1),Write(lineLabel))
        self.wait(2)
