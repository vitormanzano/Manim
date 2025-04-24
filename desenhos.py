from manim import *
#import numpy as np

class Geometry(Scene):
    def construct(self):
        circle = Circle(radius=2)
        circle.set_fill(PURPLE, opacity=0.5)
        circle.set_stroke(color = WHITE, width=8)
        circle_label  = Text('Círculo',font_size = 48).next_to(circle,DOWN)

        self.play(Create(circle),Write(circle_label))
        self.wait()

        square = Square(side_length=4)
        square.set_fill(BLUE,opacity=0.5)
        square_label = Text('Quadrado',font_size=48).next_to(square,DOWN)

        self.play(ReplacementTransform(circle,square),ReplacementTransform(circle_label,square_label))
        self.wait()

        triangle = Triangle()
        triangle.set_fill(RED,opacity=0.7)
        triangle.set_stroke(WHITE,width=2.5)
        triangle.scale(2)
        triangle_label = Text('Triângulo',font_size=48).next_to(triangle,DOWN)

        self.play(ReplacementTransform(square,triangle),ReplacementTransform(square_label,triangle_label))
        self.wait()

        pentagon = RegularPolygon(n=5)
        pentagon.set_fill(GREEN,opacity=0.5)
        pentagon.set_stroke(color =WHITE,width=3)
        pentagon.scale(2)
        pentagon.rotate(PI/6)
        pentagon_label = Text('Pentágono',font_size=48).next_to(pentagon,DOWN)

        self.play(ReplacementTransform(triangle,pentagon),ReplacementTransform(triangle_label,pentagon_label))
        self.wait()

        #para formar um hexágono por exemplo, mudamos apenas o n, n = 6, n = 7,...,n = m

        finalziaao = Text('Progredindo na geometria!',color = YELLOW,font_size=47).next_to(pentagon,2* UP)
        #para ver apenas a ultima parte da animacao
        #manim - ps - r 1080,1920 desenhos.py Geometry

class LinesAndArrows(Scene):
    def construct(self):
        #Vai da esquerda até a direita, ordem abaixo
        generic_line = Line(2*LEFT,2*RIGHT, color = WHITE)
        generic_line_label =Text('Linha genérica', font_size=24).next_to(generic_line,UP)
        #vai de 6 blocos acima até 2 blocos acima, ordem abaixo
        generic_arrow = Arrow(6*UP, 2*UP, color = YELLOW)
        generic_arrow_label = Text('Seta genérica', font_size=24).next_to(generic_line,RIGHT)

        self.play(Create(generic_line),Create(generic_line_label))
        self.play(Create(generic_arrow),Create(generic_arrow_label))

        
        #numpy, lista
        point_a = np.array([-5,2,0])
        point_b = np.array([-1,-3,0])
        point_c = np.array([4,3,0])
        point_d = np.array([6,-2, 0])

        dot_A = Dot(point_a,color =RED)
        dot_B = Dot(point_b,color = BLUE)
        dot_C= Dot(point_c,color = GREEN)
        dot_D = Dot(point_c,color = ORANGE)

        label_A = Text('A',font_size=24).next_to(dot_A,UP)
        label_B= Text('B',font_size=24).next_to(dot_B,DOWN)
        label_C = Text('C',font_size=24).next_to(dot_C,UP)
        label_D = Text('D',font_size=24).next_to(dot_D,RIGHT)

        self.play(Create(dot_A),Write(label_A))
        self.play(Create(dot_B),Write(label_B))
        self.play(Create(dot_C),Write(label_C))
        self.play(Create(dot_D),Write(label_D))

        self.wait()

        line_AB= Line(point_a,point_b,color = WHITE)
        arrow_BC = Arrow(point_b,point_c,color = BLUE)
        arrow_CD = Arrow(point_c,point_d,color = RED)
       
        label_AB = Text('Linha AB', font_size = 24).next_to(line_AB.get_center(),2*LEFT)
        label_BC = Text('Linha BC',font_size = 24).next_to(arrow_BC.get_center(),RIGHT+2*DOWN)
        label_CD  = Text('Linha CD', font_size = 24).next_to(arrow_CD.get_center(),2*LEFT)

        self.play(Create(line_AB),Write(label_AB))
        self.play(Create(arrow_BC),Write(label_BC))
        self.play(Create(arrow_CD),Write(label_CD))
        self.wait()

        final_message = Text('Linhas e setas!',color = PURPLE,font_size  =36).shift(3* DOWN + 2 * RIGHT)


