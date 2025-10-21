"""
Gradient Descent Animation
Visualizing gradient descent optimization algorithm.
"""

from manim import *


class GradientDescentScene(Scene):
    """Animation showing gradient descent on a 2D function."""
    
    def construct(self):
        # Title
        title = Text("Gradient Descent Optimization", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Create 2D axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 10, 2],
            x_length=8,
            y_length=5,
            axis_config={"include_numbers": True, "font_size": 24},
        )
        axes.shift(DOWN * 0.5)
        
        # Labels
        x_label = axes.get_x_axis_label("θ (parameter)")
        y_label = axes.get_y_axis_label("Loss J(θ)", edge=LEFT, direction=LEFT)
        
        # Loss function (quadratic)
        def loss_function(x):
            return (x - 1) ** 2 + 1
        
        loss_curve = axes.plot(
            loss_function,
            color=BLUE,
            x_range=[-3, 3]
        )
        
        # Show setup
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(loss_curve), run_time=2)
        self.wait(0.5)
        
        # Starting point
        start_x = -2.5
        current_x = start_x
        learning_rate = 0.4
        
        # Create dot and tangent line
        dot = Dot(color=RED, radius=0.08)
        dot.move_to(axes.c2p(current_x, loss_function(current_x)))
        
        self.play(Create(dot))
        
        # Add formula
        formula = MathTex(
            r"\theta_{new} = \theta_{old} - \alpha \cdot \nabla J(\theta)",
            font_size=32
        )
        formula.to_edge(DOWN)
        self.play(Write(formula))
        self.wait(1)
        
        # Perform gradient descent steps
        for step in range(8):
            # Calculate gradient (derivative)
            gradient = 2 * (current_x - 1)
            
            # Create tangent line
            tangent_slope = gradient
            x_offset = 0.5
            p1 = axes.c2p(current_x - x_offset, 
                         loss_function(current_x) - tangent_slope * x_offset)
            p2 = axes.c2p(current_x + x_offset,
                         loss_function(current_x) + tangent_slope * x_offset)
            tangent = Line(p1, p2, color=YELLOW, stroke_width=2)
            
            # Show tangent
            self.play(Create(tangent), run_time=0.5)
            self.wait(0.3)
            
            # Update position
            new_x = current_x - learning_rate * gradient
            new_dot_pos = axes.c2p(new_x, loss_function(new_x))
            
            # Animate movement
            self.play(
                dot.animate.move_to(new_dot_pos),
                FadeOut(tangent),
                run_time=0.7
            )
            
            current_x = new_x
            
            # Break if converged
            if abs(gradient) < 0.1:
                break
            
            self.wait(0.3)
        
        # Highlight minimum
        minimum_text = Text("Minimum Found!", font_size=32, color=GREEN)
        minimum_text.next_to(dot, UP, buff=0.5)
        self.play(
            dot.animate.set_color(GREEN).scale(1.5),
            Write(minimum_text)
        )
        
        self.wait(2)


class GradientDescent3D(ThreeDScene):
    """3D visualization of gradient descent."""
    
    def construct(self):
        # Setup camera
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)
        
        # Title
        title = Text("Gradient Descent in 3D", font_size=48)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        
        # Create 3D axes
        axes = ThreeDAxes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            z_range=[0, 8, 2],
            x_length=6,
            y_length=6,
            z_length=4,
        )
        
        # Surface (paraboloid)
        def surface_func(u, v):
            return axes.c2p(u, v, u**2 + v**2)
        
        surface = Surface(
            surface_func,
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(20, 20),
            fill_opacity=0.7,
            checkerboard_colors=[BLUE_D, BLUE_E]
        )
        
        self.play(Create(axes))
        self.play(Create(surface), run_time=2)
        
        # Starting point
        start_x, start_y = 1.5, 1.5
        
        # Create path
        path_points = []
        x, y = start_x, start_y
        lr = 0.2
        
        for _ in range(15):
            path_points.append(axes.c2p(x, y, x**2 + y**2))
            grad_x = 2 * x
            grad_y = 2 * y
            x -= lr * grad_x
            y -= lr * grad_y
            if x**2 + y**2 < 0.01:
                break
        
        path_points.append(axes.c2p(x, y, x**2 + y**2))
        
        # Create path line
        path = VMobject(color=YELLOW, stroke_width=4)
        path.set_points_as_corners(path_points)
        
        # Dot
        dot = Sphere(radius=0.1, color=RED)
        dot.move_to(path_points[0])
        
        self.play(Create(dot))
        self.wait(0.5)
        
        # Animate path
        self.begin_ambient_camera_rotation(rate=0.2)
        self.play(
            MoveAlongPath(dot, path),
            Create(path),
            run_time=4,
            rate_func=smooth
        )
        
        self.wait(2)
        self.stop_ambient_camera_rotation()
        
        self.wait(2)
