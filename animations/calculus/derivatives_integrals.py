"""
Calculus Animations
Visualizations of derivatives, integrals, and limits.
"""

from manim import *


class DerivativeVisualization(Scene):
    """Animation showing the concept of a derivative."""
    
    def construct(self):
        # Title
        title = Text("The Derivative", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Create axes
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 8, 2],
            x_length=8,
            y_length=5,
            axis_config={"include_numbers": True, "font_size": 24},
        )
        axes.shift(DOWN * 0.5)
        
        # Function
        def f(x):
            return x ** 2
        
        curve = axes.plot(f, color=BLUE, x_range=[0, 4])
        function_label = MathTex(r"f(x) = x^2", font_size=36)
        function_label.next_to(axes, RIGHT).shift(UP * 2)
        
        self.play(Create(axes))
        self.play(Create(curve), Write(function_label))
        self.wait(1)
        
        # Point on curve
        x_val = 2
        point = Dot(axes.c2p(x_val, f(x_val)), color=YELLOW)
        point_label = MathTex(r"(x, f(x))", font_size=28)
        point_label.next_to(point, UR, buff=0.2)
        
        self.play(Create(point), Write(point_label))
        self.wait(0.5)
        
        # Secant lines with decreasing h
        h_values = [1.5, 1.0, 0.5, 0.2]
        
        for h in h_values:
            # Second point
            x2 = x_val + h
            point2 = Dot(axes.c2p(x2, f(x2)), color=RED)
            
            # Secant line
            secant = Line(
                axes.c2p(x_val, f(x_val)),
                axes.c2p(x2, f(x2)),
                color=GREEN,
                stroke_width=3
            )
            
            # Show h
            h_brace = BraceBetweenPoints(
                axes.c2p(x_val, 0),
                axes.c2p(x2, 0),
                direction=DOWN
            )
            h_label = MathTex(r"h", font_size=28)
            h_label.next_to(h_brace, DOWN, buff=0.1)
            
            self.play(
                Create(point2),
                Create(secant),
                Create(h_brace),
                Write(h_label)
            )
            self.wait(0.7)
            
            if h != h_values[-1]:
                self.play(
                    FadeOut(point2),
                    FadeOut(secant),
                    FadeOut(h_brace),
                    FadeOut(h_label)
                )
        
        # Tangent line
        slope = 2 * x_val  # derivative of x^2
        tangent_length = 1.5
        tangent = Line(
            axes.c2p(x_val - tangent_length, f(x_val) - slope * tangent_length),
            axes.c2p(x_val + tangent_length, f(x_val) + slope * tangent_length),
            color=YELLOW,
            stroke_width=4
        )
        
        tangent_label = MathTex(r"f'(x) = 2x", font_size=32)
        tangent_label.next_to(tangent, RIGHT)
        
        self.play(
            Transform(secant, tangent),
            FadeOut(point2),
            FadeOut(h_brace),
            FadeOut(h_label)
        )
        self.play(Write(tangent_label))
        
        self.wait(2)


class IntegralVisualization(Scene):
    """Animation showing Riemann sums converging to integral."""
    
    def construct(self):
        # Title
        title = Text("The Definite Integral", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Create axes
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 5, 1],
            x_length=8,
            y_length=5,
            axis_config={"include_numbers": True, "font_size": 24},
        )
        axes.shift(DOWN * 0.5)
        
        # Function
        def f(x):
            return 0.5 * x ** 2 + 1
        
        curve = axes.plot(f, color=BLUE, x_range=[0, 3.5])
        function_label = MathTex(r"f(x) = \frac{1}{2}x^2 + 1", font_size=32)
        function_label.to_corner(UR)
        
        self.play(Create(axes))
        self.play(Create(curve), Write(function_label))
        self.wait(1)
        
        # Integration bounds
        a, b = 0.5, 3
        
        # Riemann sums with increasing rectangles
        n_values = [4, 8, 16, 32]
        
        for n in n_values:
            dx = (b - a) / n
            rectangles = VGroup()
            
            for i in range(n):
                x = a + i * dx
                height = f(x)
                
                rect = Rectangle(
                    width=axes.x_axis.unit_size * dx,
                    height=axes.y_axis.unit_size * height,
                    stroke_width=1,
                    stroke_color=WHITE,
                    fill_color=YELLOW,
                    fill_opacity=0.5
                )
                rect.move_to(axes.c2p(x + dx/2, height/2))
                rectangles.add(rect)
            
            n_label = Text(f"n = {n} rectangles", font_size=28)
            n_label.to_edge(DOWN)
            
            if n == n_values[0]:
                self.play(Create(rectangles), Write(n_label))
            else:
                self.play(
                    Transform(prev_rectangles, rectangles),
                    Transform(prev_label, n_label)
                )
            
            prev_rectangles = rectangles
            prev_label = n_label
            self.wait(1)
        
        # Show integral formula
        integral_formula = MathTex(
            r"\int_{a}^{b} f(x) \, dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i) \Delta x",
            font_size=28
        )
        integral_formula.to_edge(DOWN)
        
        self.play(Transform(prev_label, integral_formula))
        self.wait(2)


class LimitVisualization(Scene):
    """Visualization of limits."""
    
    def construct(self):
        # Title
        title = Text("Limits", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Create axes
        axes = Axes(
            x_range=[-2, 4, 1],
            y_range=[-1, 5, 1],
            x_length=8,
            y_length=5,
            axis_config={"include_numbers": True, "font_size": 24},
        )
        axes.shift(DOWN * 0.5)
        
        self.play(Create(axes))
        
        # Function with removable discontinuity
        def f(x):
            if abs(x - 2) < 0.01:
                return None
            return (x ** 2 - 4) / (x - 2)
        
        # Plot function (avoiding x=2)
        curve1 = axes.plot(lambda x: (x ** 2 - 4) / (x - 2), 
                          color=BLUE, x_range=[-2, 1.95])
        curve2 = axes.plot(lambda x: (x ** 2 - 4) / (x - 2), 
                          color=BLUE, x_range=[2.05, 4])
        
        # Hollow circle at discontinuity
        x_limit = 2
        y_limit = 4  # limit value
        hollow_circle = Circle(radius=0.08, color=BLUE, stroke_width=3)
        hollow_circle.move_to(axes.c2p(x_limit, y_limit))
        
        function_label = MathTex(r"f(x) = \frac{x^2 - 4}{x - 2}", font_size=32)
        function_label.to_corner(UR)
        
        self.play(Create(curve1), Create(curve2), Write(function_label))
        self.play(Create(hollow_circle))
        self.wait(1)
        
        # Approach from left
        dot_left = Dot(color=RED)
        x_vals_left = np.linspace(0, 1.95, 20)
        points_left = [axes.c2p(x, (x**2 - 4)/(x - 2)) for x in x_vals_left]
        
        path_left = VMobject()
        path_left.set_points_as_corners(points_left)
        
        dot_left.move_to(points_left[0])
        self.play(Create(dot_left))
        self.play(MoveAlongPath(dot_left, path_left), run_time=2)
        self.wait(0.5)
        
        # Approach from right
        dot_right = Dot(color=GREEN)
        x_vals_right = np.linspace(3.5, 2.05, 20)
        points_right = [axes.c2p(x, (x**2 - 4)/(x - 2)) for x in x_vals_right]
        
        path_right = VMobject()
        path_right.set_points_as_corners(points_right)
        
        dot_right.move_to(points_right[0])
        self.play(Create(dot_right))
        self.play(MoveAlongPath(dot_right, path_right), run_time=2)
        self.wait(0.5)
        
        # Show limit
        limit_formula = MathTex(
            r"\lim_{x \to 2} \frac{x^2 - 4}{x - 2} = 4",
            font_size=36
        )
        limit_formula.to_edge(DOWN)
        self.play(Write(limit_formula))
        
        # Highlight limit point
        limit_dot = Dot(axes.c2p(x_limit, y_limit), color=YELLOW, radius=0.1)
        self.play(
            Transform(dot_left, limit_dot.copy()),
            Transform(dot_right, limit_dot.copy()),
        )
        
        self.wait(2)
