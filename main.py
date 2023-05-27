from manim import *
import numpy as np
import scipy.integrate as integrate

# TODO: uninstall manim libs and manim voiceover
# TODO: checkout replacement transform

description_text = """
For $0 \\leq t \\leq \Pi$, a particle is moving along the curve shown so that its position at time
$t$ is ($x(t)$,$y(t)$), where $x(t)$ is not explicitly given and $y(t)$ = $2sin t$. It is
known that $\\frac{dx}{dt}$ = $e^{cos(t)}$. At time $t$ = 0, the particle is at position (1, 0)
"""

conclusion_text = """
In conclusion, the various problems which we solved have shown us how calculus can be applied to
a wide range of problems to find meaningful solutions. For that, I consider calculus to be the art
of solving problems with respect to change, and applying those solutions in their respective contexts
to gain a further understanding of the issue at hand.
"""

problem_texts = [
    "1. Find the acceleration vector of the particle at time $t$ = 1.",
    "2. For $0 \\leq t \\leq \Pi$, find the first time $t$ at which the speed of the particle is 1.5.",
    "3. Find the slope of the line tangent to the path of the particle at time $t$ = 1. Find the x-coordinate of the position of the particle at time $t$ = 1.",
    "4. Find the total distance traveled by the particle over the time interval $0 \\leq t \\leq \Pi$.",
]

class Intro(Scene):
    def build_canvas(self, stage):
        problem = Title(problem_texts[stage], font_size=30).to_edge(UP)
        self.play(FadeOut(Group(*self.get_top_level_mobjects())), FadeIn(problem))
        return problem

    def pwait(self, *args):
        self.play(*args)
        self.wait()

    def contents_screen(self):
        description = Tex(description_text).scale(0.6)

        problems = [
            (Tex(problem_texts[0]), 5),
            (Tex(problem_texts[1]), 7),
            (Tex(problem_texts[2]), 9.5),
            (Tex(problem_texts[3]), 7),
        ]

        divider = Line(LEFT, RIGHT)
        divider.next_to(description, DOWN, buff=MED_SMALL_BUFF)
        divider.match_width(description)

        description.to_edge(UP)
        intro_page = Group(description, divider)

        for text, _ in problems:
            text.scale(0.6)
            intro_page.add(text)
        intro_page.arrange(DOWN, buff=0.4)

        self.play(FadeOut(Group(*self.get_top_level_mobjects())), FadeIn(intro_page))
        self.wait()

        self.play(Circumscribe(description, run_time=3, color=BLUE))
        self.wait(25)

        for tex, time in problems:
            self.play(Indicate(tex, color=BLUE), run_time=3)
            self.wait(time - 3)

    def question_one(self):
        accel_equation = Tex("$a(t)$ = $<x''(t), y''(t)>$")
        stage_group = Group()
        base_off = 2.4
        problem = self.build_canvas(0)
        self.wait(5)

        equations = [
            (Tex("$a(t)$ = $<x''(t), y''(t)>$"), 7),
            (Tex("$x'(t)$ = $e^{cos(t)}$, $y(t)$ = $2sin(t)$"), 4),
            (Tex("$x''(t)$ = $-sin(t)e^{cos(t)}$"), 8),
            (Tex("$y'(t)$ = $2cos(t)$, $y''(t)$ = $-2sin(t)$"), 8),
            (Tex("$a(1)$ = $<-sin(1)e^{cos(1)}, -2sin(1)>$"), 6),
            (Tex("$a(1)$ = $<-1.444,-1.683>$"), 5.5),
        ]

        for stage, time in equations[:2]:
            self.pwait(Write(stage))
            self.wait(time)
            self.play(stage.animate.scale(0.5))

            if base_off == 2.4:
                rect = SurroundingRectangle(stage, color=GREEN, buff=0.20).move_to(
                    [5.2, 2.4, 0]
                )
                self.play(
                    Create(rect),
                    stage.animate.shift([5.2, 2.4, 0]),
                )
                base_off -= rect.height + 0.30
            else:
                rect = SurroundingRectangle(stage, color=BLUE, buff=0.20).move_to(
                    [5.2, base_off, 0]
                )
                self.play(
                    Create(rect),
                    stage.animate.shift([5.2, base_off, 0]),
                )

        for stage, _ in equations[2:]:
            stage_group.add(stage)

        stage_group.arrange(DOWN, buff=0.8)
        stage_group.next_to(problem, DOWN)
        stage_group.shift(LEFT * 2)

        for stage, time in equations[2:]:
            self.play(Write(stage))
            self.wait(time)

        self.play(ApplyWave(equations[5][0]))
        self.wait(1)

    def question_two(self):
        problem = self.build_canvas(1)
        stage_group = Group()
        base_off = 2.4
        self.wait(7)

        equations = [
            (Tex("$x'(t)$ = $e^{cos(t)}$, $y(t)$ = $2sin(t)$"), 5),
            (Tex("Speed: $\sqrt{(\\frac{dx}{dt})^2 + (\\frac{dy}{dt})^2}$"), 3),
            (Tex("$\sqrt{(e^{cos(t)})^2 + (2sin(t))^2}$ = 1.5"), 3),
            (Tex("$t$ = $1.254$"), 3),
        ]

        for stage, time in equations[:2]:
            self.play(Write(stage))
            self.wait(time)
            self.play(stage.animate.scale(0.5))

            if base_off == 2.4:
                rect = SurroundingRectangle(stage, color=GREEN, buff=0.20).move_to(
                    [5.2, 2.4, 0]
                )
                self.play(
                    Create(rect),
                    stage.animate.shift([5.2, 2.4, 0]),
                )
                base_off -= rect.height + 0.30
            else:
                rect = SurroundingRectangle(stage, color=BLUE, buff=0.20).move_to(
                    [5.2, base_off, 0]
                )
                self.play(
                    Create(rect),
                    stage.animate.shift([5.2, base_off, 0]),
                )

        for stage, _ in equations[2:]:
            stage_group.add(stage)

        stage_group.arrange(DOWN, buff=0.8)
        stage_group.next_to(problem, DOWN)
        stage_group.shift(LEFT * 2)

        direction_arrow = Arrow(start=UP, end=DOWN).next_to(
            equations[2][0], DOWN, buff=0.35
        )

        self.pwait(AddTextWordByWord(equations[2][0], run_time=equations[2][1]))
        self.pwait(GrowArrow(direction_arrow))
        equations[3][0].next_to(direction_arrow, DOWN, buff=0.50)
        self.pwait(AddTextWordByWord(equations[3][0], run_time=equations[3][1]))
        self.pwait(Indicate(equations[3][0], color=BLUE))

    def question_three(self):
        problem = self.build_canvas(2)
        self.wait(9.5)

        equations = [
            (Tex("$\\frac{dy}{dx} = \\cfrac{\\frac{dy}{dt}}{\\frac{dx}{dt}}$"), 5),
            (Tex("$\\frac{dy}{dt}|_{t=1} = 2cos(1)$"), 4.5),
            (Tex("$\\frac{dy}{dx}|_{t=1} = 0.630$"), 5),
            (Tex("$x(0) + \int_{0}^{1} x'(t) \,dt = x(1)$"), 6),
            (Tex("$1 + \int_{0}^{1} e^{cos(t)} \,dt = 3.342$"), 4),
        ]

        equations[1][0].next_to(problem, DOWN)
        equations[3][0].next_to(problem, DOWN)
        direction_arrow = Arrow(start=UP, end=DOWN).next_to(
            equations[1][0], DOWN, buff=0.35
        )
        equations[2][0].next_to(direction_arrow, DOWN)

        self.play(Write(equations[0][0]))
        self.wait(equations[0][1])
        self.play(equations[0][0].animate.scale(0.5))

        rect = SurroundingRectangle(equations[0][0], color=GREEN, buff=0.20).move_to(
            [5.2, 1.8, 0]
        )

        self.pwait(
            Create(rect),
            equations[0][0].animate.shift([5.2, 1.8, 0]),
        )

        self.play(Write(equations[1][0]))
        self.wait(equations[1][1])
        self.pwait(GrowArrow(direction_arrow))
        self.play(Write(equations[2][0]))
        self.wait(equations[2][1])

        self.play(equations[2][0].animate.scale(0.5))
        rect2 = SurroundingRectangle(equations[2][0], color=RED, buff=0.20).move_to(
            [5.2, 1.8 - 1.398, 0]
        )
        self.pwait(
            Create(rect2), equations[2][0].animate.shift([5.2, 1.8 - (1.398 / 2), 0])
        )

        eq_group = VGroup(equations[1][0], direction_arrow)
        direction_arrow2 = Arrow(start=UP, end=DOWN).next_to(
            equations[3][0], DOWN, buff=0.35
        )
        equations[4][0].next_to(direction_arrow2, DOWN)

        self.play(ReplacementTransform(eq_group, equations[3][0]))
        self.wait(equations[3][1])
        self.pwait(GrowArrow(direction_arrow2))
        self.play(Write(equations[4][0]))
        self.wait(equations[4][1])

        to_remove_group = Group(
            rect, rect2, direction_arrow2, equations[3][0], equations[0][0]
        )
        self.pwait(equations[4][0].animate.shift(LEFT * 2), FadeOut(to_remove_group))
        equations[2][0].scale(2)
        self.pwait(
            equations[2][0].animate.next_to(equations[4][0], RIGHT, buff=0.70),
        )

        self.pwait(
            Indicate(equations[2][0], color=BLUE), Indicate(equations[4][0], color=BLUE)
        )

    def question_four(self):
        def dxdt(t):
            return np.exp(np.cos(t))

        def integral(t):
            return integrate.quad(dxdt, 0, t)[0]

        def func(t):
            return np.array([integral(t), np.sin(t) * 2, 0])

        problem = self.build_canvas(3)
        self.wait(5)

        ax = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 3, 1],
            axis_config={"tip_shape": StealthTip, "include_numbers": True},
        )

        param = ax.plot_parametric_curve(func, t_range=[0, PI], color=RED).shift(
            RIGHT * 2
        )

        formula = Tex(
            "$A$ = $\int_{0}^{\Pi} \sqrt{(e^{cos(t)})^2 + (2sin(t))^2} \,dt $"
        )
        formula2 = Tex("$A$ = $6.035$")
        formula.shift(RIGHT * 2)
        formula.shift(RIGHT)
        formula2.shift(RIGHT * 2)
        formula2.shift(RIGHT)

        prop = ValueTracker(0)
        graph = VGroup(ax, param)
        graph.next_to(problem, DOWN)
        graph.scale(0.8)

        self.pwait(Create(ax))
        self.pwait(Create(param))
        self.wait(1)

        self.pwait(graph.animate.scale(0.6))
        self.pwait(graph.animate.to_corner(LEFT))
        self.pwait(graph.animate.shift(UP))

        self.play(Write(formula))
        self.wait(6)

        prop = ValueTracker(0)
        number_display = Tex("$t$ =").next_to(ax, DOWN)
        numbers = DecimalNumber(0).next_to(number_display, RIGHT)
        numbers.add_updater(lambda m: m.set_value(prop.get_value()))

        dot = always_redraw(lambda: Dot(param.point_from_proportion(prop.get_value())))
        self.add(numbers, number_display, dot)

        self.play(prop.animate.set_value(1), run_time=4, rate_func=linear)
        self.wait(2)
        self.pwait(ReplacementTransform(formula, formula2))
        self.pwait(Indicate(formula2, color=BLUE))

    def conclusion(self):
        conclusion_obj = Tex(conclusion_text, font_size=27)
        thanks_obj = Text("Special Thanks to...")
        ap_obj = SVGMobject("ap_logo.svg").scale(1.4)
        manim_text = Text("Manim Animation Library")
        ap_text = Text("Advanced Placement")
        banner = ManimBanner()
        manim_text.next_to(banner, DOWN)
        ap_text.next_to(ap_obj, DOWN, buff=0.5)
        the_end = Text("The End!")

        self.play(
            FadeOut(Group(*self.get_top_level_mobjects())),
            FadeIn(conclusion_obj, shift=UP * 1.5),
        )
        self.wait(20)
        self.play(
            FadeOut(conclusion_obj, shift=UP * 1.5), FadeIn(thanks_obj, shift=UP * 1.5)
        )

        self.pwait(
            FadeOut(thanks_obj, shift=UP * 1.5), banner.create(), Write(manim_text)
        )
        self.pwait(banner.expand())
        self.pwait(Unwrite(banner), FadeOut(manim_text, shift=1.5 * DOWN))
        self.pwait(Create(ap_obj), Write(ap_text))
        self.pwait(
            FadeOut(ap_obj, shift=UP * 1.5),
            FadeOut(ap_text, shift=DOWN * 1.5),
            FadeIn(the_end, shift=UP * 1.5),
        )
        self.pwait(Flash(the_end, flash_radius=1.8, color=BLUE, line_length=1.8))
        self.wait(1)

    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT

        banner1 = Tex("Solutions to AP Calculus BC FRQ \#2").scale(1.4)
        banner2 = Tex("A Visual Approach").scale(0.7)
        banner2.next_to(banner1, DOWN)

        stream_lines = StreamLines(func, stroke_width=2, max_anchors_per_line=30)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.play(Write(banner1))
        self.wait()
        self.play(Write(banner2))

        self.contents_screen()
        self.question_one()
        self.question_two()
        self.question_three()
        self.question_four()
        self.conclusion()
