from manim import *

class triangulo(Scene):
    def construct(self):  
        
        triangle = Triangle()
        triangle_label = Text('Teorema de pitágoras',font_size = 40).next_to(triangle,2*UP)
        triangle_label.set_fill(YELLOW)
        
        self.play(FadeIn(Create(triangle),Write(triangle_label)))
        self.wait(2)
        
        square = Square()
        square.set_fill(RED,OPACITY=0.5)
        self.remove(triangle_label)

        self.play(ReplacementTransform(triangle,square))
        

       


       
