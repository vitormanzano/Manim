from manim import *

class Exercise1(Scene):
    def construct(self):
        circle = Circle().set_fill(PURPLE,opacity=0.5)
        circle.set_stroke(WHITE,width=4)
        
        triangle = Triangle().set_fill(RED,opacity=0.5).next_to(circle,RIGHT,buff=1)
        triangle.set_stroke(WHITE,width =4)
        
        square = Square().set_fill(BLUE,opacity=0.5).next_to(circle,LEFT,buff = 1)
        square.set_stroke(WHITE,width=4)

        objetos = VGroup(square,circle,triangle).arrange(RIGHT,buff=1)

        self.play(Create(square),Create(circle),Create(triangle))
        self.wait()

        self.play(circle.animate.shift(3*UP))
        self.wait()

        line = Line(square.get_center(),circle.get_center(),color = YELLOW)
        
        self.play(Create(line))
        self.wait()
        self.play(Uncreate(line))

        self.play(square.animate.shift(3*DOWN))
        
        self.wait()
        self.play(FadeOut(square),FadeOut(circle),FadeOut(triangle))
        self.wait()

        mensagem = Text('Formas reposicionadas!',font_size = 40)
        self.play(Write(mensagem))

class Exercise2(Scene):
    def construct(self):
        triangle = Triangle().set_fill(RED,opacity=0.5)
        
        self.play(Create(triangle))
        self.wait()
        
        self.play(Rotate(triangle,angle=PI/2))

        self.play(triangle.animate.scale(1.5))

        circle = Circle().set_fill(ORANGE,opacity=0.5)
        circle.set_stroke(WHITE,width=4)

        self.play(ReplacementTransform(triangle,circle))
        self.wait()
        
        self.play(circle.animate.shift(3*RIGHT))
        self.wait()
        

        square = Square().set_fill(YELLOW,opacity=0.5)
        square.set_stroke(WHITE,width=4)
        

        self.play(ReplacementTransform(circle,square))
        self.wait()

        self.play(square.animate.move_to(ORIGIN))

        mensagem = Text('Transformações completas!',font_size  = 30).next_to(square,DOWN)

        self.play(Write(mensagem))

        
        

    

        
