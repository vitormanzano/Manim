from manim import *

class BhaskaraProof(Scene):
    def construct(self):
        title = MathTex(r'\text{Demonstração Canônica}',font_size = 70,color = YELLOW)
        title.shift(0.5*UP)
        self.play(Write(title))

        subtitle = MathTex(r'\text{Fórmula de Bhaskara}',font_size=70,color= BLUE)
        subtitle.next_to(title,DOWN,buff=0.5)
        
        self.play(Write(subtitle))
        self.wait()

        self.play(FadeOut(title),FadeOut(subtitle))

        def produtoNotavel():
            
            introducao  = Text('Quadrado perfeito',font_size = 100)
            p1 = MathTex('(X+Y)^2',font_size = 100)
            p2 = MathTex('X^2 + 2XY + Y^2',font_size = 100)
            
            step2 = MathTex(r'x^2 + \frac{b}{a}x = -\frac{c}{a}',font_size = 100)
            deducao = Text('Se temos',font_size=70).shift(2*UP)
            deducao2 = Text('Precisaremos do segundo termo',font_size= 50,color = RED)
            
            p3 = MathTex(r'2XY = \frac{b}{a}X',font_size=100)
            p4 = MathTex(r'Y = \frac{b}{2a}',font_size=100)
            deducao3 = Text('y precisa ser...',font_size = 50).shift(2*UP)
            
    
            self.play(Write(introducao))
            self.wait()
            
            self.play(Uncreate(introducao),Create(p1))
            self.wait(1.5)
            
            self.play(ReplacementTransform(p1,p2))
            self.wait(1.5)
            self.play(Write(deducao),ReplacementTransform(p2,step2))
            self.wait(2)
            self.play(Uncreate(step2))
            self.play(ReplacementTransform(deducao,deducao2))
            
            self.wait(1.5)
            self.play(Uncreate(deducao2))
            self.play(ReplacementTransform(step2,p3))
            self.wait(1.5)
            self.play(Write(deducao3))
            self.wait()
            self.play(ReplacementTransform(p3,p4))
            self.wait(2)
            self.play(Uncreate(deducao3))
            self.play(FadeOut(p4))


        def equations_sequence(initial,equations):
            self.play(Write(initial))
            self.wait()
            for step in equations:
                

                if step == equations[0]:
                    current_step = equations[0]
                    self.play(ReplacementTransform(initial,equations[0]))
                    self.wait(2)
                else:
                    if step==equations[2]:
                        self.play(Uncreate(current_step))
                        produtoNotavel()
                        volta = Text('Voltando a dedução...',color = BLUE,font_size = 100)
                        self.play(Write(volta))
                        self.wait()
                        self.play(Uncreate(volta))

                        self.play(Create(current_step))
                        self.wait(0.5)
                        

                    self.play(ReplacementTransform(current_step,step))
                    self.wait(2)
                    current_step= step
            self.play(Circumscribe(equations[-1],buff = 1.5))
            self.wait()
            


        equation = MathTex('ax^2 + bx + c = 0',font_size = 100)
        step1 = MathTex('ax^2 + bx = -c',font_size = 100)
        step2 = MathTex(r'x^2 + \frac{b}{a}x = -\frac{c}{a}',font_size = 100)
        step3 = MathTex(r'x^2 + \frac{b}{a}x + \frac{b^2}{4a^2} = -\frac{c}{a} + \frac{b^2}{4a^2}',font_size = 100)
        step4 = MathTex(r'\left(x + \frac{b}{2a}\right)^2 = -\frac{4ac}{4a^2} + \frac{b^2}{4a^2}',font_size = 100)
        step5 = MathTex(r'x + \frac{b}{2a} = \pm \frac{\sqrt{b^2 - 4ac}}{2a}',font_size = 100)
        step6 = MathTex(r'x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}',font_size = 100)

        equations = [step1,step2,step3,step4,step5,step6]

        equations_sequence(equation,equations)
        text = Text('Fórmula de Bhaskara provada',font_size=34).next_to(equations[-1],DOWN)
        self.play(Write(text))

        self.play(FadeOut(step6))
        self.play(Uncreate(text))
        self.wait()

        
            





            
            
            







            
