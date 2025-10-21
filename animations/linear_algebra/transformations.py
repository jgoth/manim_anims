"""
Linear Algebra Animations
Visualizations of matrix transformations and linear operations.
"""

from manim import *


class MatrixTransformation(LinearTransformationScene):
    """Animation showing matrix transformations of vectors."""
    
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_basis_vectors=True,
            show_coordinates=True,
            leave_ghost_vectors=True,
        )
    
    def construct(self):
        # Title
        title = Text("Matrix Transformations", font_size=48)
        title.to_edge(UP)
        title.fix_in_frame()
        self.add_foreground_mobject(title)
        self.play(Write(title))
        self.wait()
        
        # Show initial vectors
        vector = Vector([2, 1], color=YELLOW)
        vector_label = MathTex(r"\vec{v}", color=YELLOW)
        vector_label.next_to(vector.get_end(), RIGHT)
        
        self.add_vector(vector)
        self.play(Write(vector_label))
        self.wait()
        
        # Rotation matrix
        rotation_matrix = [[np.cos(PI/4), -np.sin(PI/4)],
                          [np.sin(PI/4), np.cos(PI/4)]]
        
        matrix_text = MathTex(
            r"R = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}",
            font_size=32
        )
        matrix_text.to_corner(UR)
        matrix_text.fix_in_frame()
        self.play(Write(matrix_text))
        self.wait()
        
        # Apply transformation
        self.apply_matrix(rotation_matrix)
        self.wait(2)
        
        # Reset
        self.play(FadeOut(matrix_text))
        
        # Scaling matrix
        scaling_matrix = [[2, 0], [0, 0.5]]
        
        scale_text = MathTex(
            r"S = \begin{bmatrix} 2 & 0 \\ 0 & 0.5 \end{bmatrix}",
            font_size=32
        )
        scale_text.to_corner(UR)
        scale_text.fix_in_frame()
        self.play(Write(scale_text))
        self.wait()
        
        self.apply_matrix(scaling_matrix)
        self.wait(2)


class EigenvalueVisualization(Scene):
    """Visualization of eigenvectors and eigenvalues."""
    
    def construct(self):
        # Title
        title = Text("Eigenvectors and Eigenvalues", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Explanation
        explanation = Text(
            "Eigenvectors maintain their direction under transformation",
            font_size=28
        )
        explanation.next_to(title, DOWN)
        self.play(Write(explanation))
        self.wait(1)
        
        # Create plane
        plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        )
        self.play(Create(plane))
        
        # Original vectors
        v1 = Arrow(ORIGIN, [2, 1, 0], color=YELLOW, buff=0)
        v2 = Arrow(ORIGIN, [1, -2, 0], color=GREEN, buff=0)
        eigenvector = Arrow(ORIGIN, [2, 2, 0], color=RED, buff=0)
        
        v1_label = MathTex(r"\vec{v}_1", color=YELLOW).next_to(v1.get_end(), RIGHT)
        v2_label = MathTex(r"\vec{v}_2", color=GREEN).next_to(v2.get_end(), DOWN)
        eigen_label = MathTex(r"\vec{e}", color=RED).next_to(eigenvector.get_end(), RIGHT)
        
        self.play(
            Create(v1), Create(v2), Create(eigenvector),
            Write(v1_label), Write(v2_label), Write(eigen_label)
        )
        self.wait(1)
        
        # Transformation matrix (has eigenvalue 2 for direction [1,1])
        matrix = [[1.5, 0.5], [0.5, 1.5]]
        
        matrix_tex = MathTex(
            r"A = \begin{bmatrix} 1.5 & 0.5 \\ 0.5 & 1.5 \end{bmatrix}",
            font_size=32
        )
        matrix_tex.to_corner(UL)
        self.play(Write(matrix_tex))
        self.wait()
        
        # Apply transformation
        def transform_vector(vec):
            x, y = vec[0], vec[1]
            new_x = matrix[0][0] * x + matrix[0][1] * y
            new_y = matrix[1][0] * x + matrix[1][1] * y
            return [new_x, new_y, 0]
        
        new_v1 = Arrow(ORIGIN, transform_vector([2, 1, 0]), color=YELLOW, buff=0)
        new_v2 = Arrow(ORIGIN, transform_vector([1, -2, 0]), color=GREEN, buff=0)
        new_eigenvector = Arrow(ORIGIN, transform_vector([2, 2, 0]), color=RED, buff=0)
        
        self.play(
            Transform(v1, new_v1),
            Transform(v2, new_v2),
            Transform(eigenvector, new_eigenvector),
            run_time=2
        )
        self.wait(1)
        
        # Highlight that eigenvector kept direction
        note = Text(
            "Eigenvector only scaled (λ = 2)",
            font_size=28,
            color=RED
        )
        note.to_edge(DOWN)
        self.play(Write(note))
        
        self.wait(2)


class DotProductVisualization(Scene):
    """Visualization of dot product geometric interpretation."""
    
    def construct(self):
        # Title
        title = Text("Dot Product Geometric Interpretation", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Create axes
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 5, 1],
            x_length=7,
            y_length=7,
            axis_config={"include_numbers": True, "font_size": 24},
        )
        axes.shift(DOWN * 0.3)
        
        self.play(Create(axes))
        
        # Vectors
        v1_coords = [3, 1, 0]
        v2_coords = [2, 3, 0]
        
        v1 = Arrow(axes.c2p(0, 0), axes.c2p(v1_coords[0], v1_coords[1]), 
                   color=YELLOW, buff=0, stroke_width=6)
        v2 = Arrow(axes.c2p(0, 0), axes.c2p(v2_coords[0], v2_coords[1]), 
                   color=GREEN, buff=0, stroke_width=6)
        
        v1_label = MathTex(r"\vec{a}", color=YELLOW, font_size=36)
        v1_label.next_to(v1.get_end(), DOWN)
        v2_label = MathTex(r"\vec{b}", color=GREEN, font_size=36)
        v2_label.next_to(v2.get_end(), UP)
        
        self.play(Create(v1), Create(v2))
        self.play(Write(v1_label), Write(v2_label))
        self.wait(1)
        
        # Show angle
        angle = Angle(v1, v2, radius=0.5, color=WHITE)
        angle_label = MathTex(r"\theta", font_size=32)
        angle_label.next_to(angle, RIGHT, buff=0.1)
        
        self.play(Create(angle), Write(angle_label))
        self.wait(1)
        
        # Projection
        v1_unit = v1_coords / np.linalg.norm(v1_coords)
        projection_length = np.dot(v2_coords, v1_unit)
        proj_point = projection_length * v1_unit
        
        proj_line = DashedLine(
            axes.c2p(v2_coords[0], v2_coords[1]),
            axes.c2p(proj_point[0], proj_point[1]),
            color=BLUE
        )
        
        proj_vector = Arrow(
            axes.c2p(0, 0),
            axes.c2p(proj_point[0], proj_point[1]),
            color=BLUE,
            buff=0,
            stroke_width=6
        )
        
        proj_label = Text("projection", font_size=24, color=BLUE)
        proj_label.next_to(proj_vector, DOWN, buff=0.1)
        
        self.play(Create(proj_line))
        self.play(Create(proj_vector), Write(proj_label))
        self.wait(1)
        
        # Formula
        dot_product = np.dot(v1_coords[:2], v2_coords[:2])
        formula = MathTex(
            r"\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta = " + f"{dot_product:.1f}",
            font_size=32
        )
        formula.to_edge(DOWN)
        self.play(Write(formula))
        
        self.wait(2)
