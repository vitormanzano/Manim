from manim import *

class ReplacementTransformExample(Scene):
    def construc(self):
        t = Text('ReplacementTransform')
        s = Square(color = RED)
        self.play(Write(t))
        self.wait()
        self.play(ReplacementTransform(t, s))
        self.play(s.animate.scale(2))
        self.wait(2)

class TransformExample(Scene):
    def construct(self):
        t = Text('Transform')
        s = Square(color = RED)
        self.play(Write(t))
        self.wait()
        self.play(Transform(t, s))
        self.play(s.animate.scale(2))
        self.wait(2)

class TransformMatchingShapesExample(Scene):
    def construct(self):
        t1 = Text('TransformMatchingShapes')
        t2 = Text("What are you doing my swamp?")
        self.play(Write(t1))
        self.wait()
        self.play(TransformMatchingShapes(t1, t2))
        self.wait(2)

class WriteUnwriteExample(Scene):
    def construct(self):
        t = Text('I like this one')
        self.play(Write(t))
        self.wait()
        self.play(Unwrite(t))

class SwapExample(Scene):
    def construct(self):
        c = Circle()
        p = RegularPolygon()
        g = VGroup(c, p).arrange(buff = 1)
        self.play(Write(c), Write(p))
        self.wait(1)
        self.play(Swap(c, p))
        self.wait(1)

class RestoreExample(Scene):
    def construct(self):
        c = Circle(color = GREEN, fill_opacity = 1)
        c.save_state()
        self.play(c.animate.scale(6))
        self.play(c.animate.shift(RIGHT*4))
        self.play(FadeToColor(c, RED))
        self.play(Restore(c))
        self.wait()

class CreateUncreateExample(Scene):
    def construct(self):
        c1 = Circle(color = GREEN)
        c2 = Circle(color = RED)
        c3 = Circle(color = BLUE)
        g = VGroup(c1, c2, c3).arrange
        self.play(Create(c1), Create(c2), Create(c3))
        self.wait()
        self.play(Uncreate(g))
        self.wait()

class CircumscribeExample(Scene):
    def construct(self):
        t = Text('Shrek', color = RED, font = 'Sentient').scale(2)
        self.play(Write(t))
        self.play(Circumscribe(t))
        self.wait(0.5)

class RotateExample(Scene):
    def construct(self):
        t = Text('Rotate Animation', color = RED)
        s = Square(color = BLUE, fill_opacity = 1).scale(2)
        self.play(Write(t))
        self.wait()
        self.play(Rotate(s, angle = PI/2))
        self.wait(0.5)
        self.play(Rotate(s, angle = PI, about_point = UP))
        self.wait(0.5)

class IndicateExample(Scene):
    def construct(self):
        t = Text('Shrek', color = RED, font = 'Sentient').scale(2)
        self.play(Write(t))
        self.play(Indicate(t))
        self.wait()

class GrowFromCenterExample(Scene):
    def construct(self):
        s = RoundedRectangle(color = BLUE, stroke_width = 10, corner_radius = 0.5, width = 2, height = 2)
        ss = SurroundingRectangle(s, color = ORANGE, corner_radius = 0.5, buff = 1.5, stroke_width = 10)
        g = VGroup(ss, ss)
        self.play(GrowFromCenter(g))
        self.wait(0.5)

class GrowFromCenterRedSquareExample(Scene):
    def construct(self):
        r = Square(color = BLUE, fill_opacity = 1).scale(2)
        self.play(GrowFromCenter(r, point_color =  RED), run_time = 2)
        self.wait(0.5)

class DrawBorderThenFillTriangleExample(Scene):
    def construct(self):
        t = Triangle(color = RED, fill_opacity = 1).scale(2)
        self.play(DrawBorderThenFill(t))
        self.wait(0.5)

class FadeToColorCircleExample(Scene):
    def construct(self):
        c = Circle(color = RED, stroke_color = WHITE, fill_opacity = 1).scale(2)
        self.play(Write(c))
        self.play(FadeToColor(c, BLUE))
        self.wait(0.5)

class FadeTransformExample(Scene):
    def construct(self):
        c = Circle(color = RED, fill_opacity = 1)
        r = Square(color = BLUE).scale(2)
        self.play(Write(c))
        self.play(FadeTransform(c, r))
        self.wait(0.5)

class CyclicReplaceExample(Scene):
    def construct(self):
        d1 = Dot(color = RED)
        d2 = Dot(color = GREEN)
        d3 = Dot(color = BLUE)
        g = VGroup(d1, d2, d3).arrange().scale(10)
        self.play(Write(g))
        self.play(CyclicReplace(d1, d2))
        self.play(CyclicReplace(d2, d3))
        self.play(CyclicReplace(d1, d3))
        self.play(CyclicReplace(d1, d2, d3))
        self.play(CyclicReplace(d3, d2, d1))
        self.play(Unwrite(g))

class FocusOnExample(Scene):
    def construct(self):
        t1 = Text('Hello', color = RED, font = 'Sentient').scale(2)
        t2 = Text('There', color = RED, font = 'Sentient').scale(2)
        g = VGroup(t1, t2).arrange(buff = 2)
        self.play(Write(g))
        self.play(FocusOn(t2))
        self.wait(0.5)

class SpiralInExample(Scene):
    def construct(self):
        t = Text('Shrek', color = RED, font = 'Sentient').scale(2)
        s = Square()
        self.play(SpiralIn(t))
        self.wait(0.5)
        self.play(Unwrite(t))
        self.wait(0.5)

class ApplyWaveExample(Scene):
    def construct(self):
        t = Text('Shrek', color = RED, font = 'Sentient').scale(2)
        self.play(Write(t))
        self.play(ApplyWave(t))
        self.wait(0.5)

class WiggleExample(Scene):
    def construct(self):
        s = Square(color = RED, fill_opacity = 0.5, fill_color = BLUE)
        self.play(Write(s))
        self.wait(0.5)
        self.play(Wiggle(s))
        self.wait(0.5)
        self.play(Unwrite(s))

class BroadcastExample(Scene):
    def construct(self):
        s = Square(color = RED, fill_opacity = 0.5, fill_color = RED).scale(2)
        self.play(Write(s))
        self.wait(0.5)
        self.play(Broadcast(s))
        self.wait(0.5)
        self.play(Unwrite(s))