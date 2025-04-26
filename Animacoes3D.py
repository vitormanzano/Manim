from manim import *

class Basic3DShapes(ThreeDScene):  # precisa herdar de ThreeDScene para cenas 3D
    def construct(self):
        # Define orientação inicial da câmera
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)

        # Cria uma esfera azul
        sphere = Sphere(resolution=(24, 24)).set_color(BLUE)  # 'center' não é argumento aceito diretamente

        # Cria um cubo vermelho deslocado para a esquerda
        cube = Cube().set_color(RED)
        cube.shift(2 * LEFT)

        # Corrige 'pkay' para 'play'
        self.play(Create(sphere))
        self.play(Rotate(sphere, angle=PI/2, axis=UP))
        self.wait()

        # Transforma esfera em cubo
        self.play(Transform(sphere, cube))

        # Para rotação e finaliza
        self.stop_ambient_camera_rotation()
        self.wait()

class ParametricCurve3DExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)

        axes = ThreeDAxes()
        curve = ParametricFunction(
            lambda t: np.array([
                np.cos(t),
                np.sin(t),
                t / 2
            ]),
            t_range = np.array([0, 4 * PI, 0.01]),
            color = YELLOW
        ).set_color_by_gradient(BLUE, PURPLE)

        self.add(axes)
        self.play(Create(curve), run_time = 2)

        self.wait(3)

class ParametricSurface3DExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)

        parametric_surface = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cosh(v),
                1.5 * np.sin(u) * np.cosh(v),
                1.5 * np.sinh(v)
            ]),
            u_range = [0, TAU],
            v_range = [-1, 1],
            checkerboard_colors= [RED_D, RED_E],
            resolution = (24, 24)
        )

        self.play(Create(parametric_surface), run_time = 2)
        self.wait(5)