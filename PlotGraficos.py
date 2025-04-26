from manim import *
import numpy as np

class PlotFunctionExample(Scene):
    def construct(self):
        axes = Axes(
            x_range = [-2, 2, 1], # start, stop, step
            y_range = [-4, 4, 1],
            x_length = 8,
            y_length = 8,
            axis_config = {'color' : BLUE, 'include_ticks' : False},
            tips = True
        )

        #labels

        labels = axes.get_axis_labels(x_label = 'x', y_label = 'y')

        #Plotar a minha função
                                #f    (x)
        quadratic = axes.plot(lambda x: x**2 - 2, color = YELLOW)
        quadratic_label = MathTex('y = x^2 - 2').next_to(quadratic, UP + RIGHT)

        self.add(axes, labels)
        self.play(Create(quadratic))
        self.play(FadeIn(quadratic_label))
        self.wait(2)

class PlotParametricFunctionExample(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-8, 8, 1],  # start, stop, step
            y_range=[-8, 8, 1],
            x_length=8,
            y_length=8,
            axis_config={'color': WHITE, 'tip_shape': StealthTip ,'include_ticks': False},
            tips=True
        )

        labels = axes.get_axis_labels(x_label='x', y_label='y')

        spiral = axes.plot_parametric_curve(
            lambda t: np.array([
                1.5 * np.cos(t) * np.exp(0.2 * t),
                1.5 * np.sin(t) * np.exp(0.2 * t),
                0
            ]),
            t_range = [0, TAU] #Dominio de 0 a 2 * Pi
        )

        gradiente_ciano_roxo = ['#00FFFF', '#FFFFFF', '#7F00FF']

        spiral.set_color_by_gradient(*gradiente_ciano_roxo)
        spiral.stroke_width = 10

        spiral_label = MathTex(r'\Gamma(t) = (1.5e^{0.2t} \cos t, 1.Se^{0.2t} \sin t)', color = PURPLE).shift(3 * DOWN)

        self.add(axes, labels)
        self.play(Create(spiral))
        self.play(FadeIn(spiral_label))
        self.wait(2)