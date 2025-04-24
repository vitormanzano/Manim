from manim import *

class BasicAnimations(Scene):
    def construct(self):
        #Criar um círculo e adicionando um rótulo
        circle = Circle()
        circle.set_fill(BLUE,opacity=0.5)
        circle_label = Text('Círculo' , font_size = 24).next_to(circle,DOWN)#Funciona como right, left, upper, down
        #self.add, nao fica animado
        self.play(Create(circle),Write(circle_label))#Mostrando a animação
        self.wait()#delay

        #Cria um quadrado rotacionado e um rótulo

        square = Square().rotate(PI/4)
        square_label = Text('Quadrado',font_size=24).next_to(square,DOWN)

        #Transformar o círculo no quadrado, assim como os seus rótulos

        self.play(ReplacementTransform(circle,square),ReplacementTransform(circle_label,square_label))

        self.wait()
        
        self.play(FadeOut(square), FadeOut(square_label))

        triangle = Triangle()
        triangle.set_fill(BLUE,opacity=0.5)
        triangle_label = Text('Triângulo',font_size = 24).next_to(triangle,DOWN)

        self.play(FadeIn(triangle),Write(triangle_label))

        self.wait()

        finalizacao = Text('Terminei minha primeira animação', font_size = 36).next_to(triangle,2*UP)
        self.play(Write(finalizacao))

        self.wait()
