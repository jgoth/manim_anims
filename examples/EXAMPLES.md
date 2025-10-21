# Animation Examples

This document provides visual descriptions and usage examples for all animations in this repository.

## AI & Machine Learning Animations

### Neural Network Scene

**File:** `animations/ai/neural_network.py`  
**Scene:** `NeuralNetworkScene`

**Description:**
Visualizes a multi-layer feedforward neural network with:
- Input layer (3 neurons)
- Two hidden layers (4 neurons each)
- Output layer (2 neurons)
- Animated signal propagation through the network

**Command:**
```bash
manim -pql animations/ai/neural_network.py NeuralNetworkScene
```

**Key Features:**
- Layer-by-layer construction
- Connection visualization between neurons
- Signal propagation animation showing data flow
- Color-coded activation states

**Customization Options:**
- Modify `create_layer(num_neurons, label)` to change network architecture
- Adjust neuron colors in the activation animation
- Change animation speed with `run_time` parameter

---

### Neuron Activation

**File:** `animations/ai/neural_network.py`  
**Scene:** `NeuronActivation`

**Description:**
Demonstrates the sigmoid activation function with:
- Mathematical formula: σ(x) = 1/(1+e⁻ˣ)
- Plotted curve showing the S-shape
- Animated point moving along the curve

**Command:**
```bash
manim -pql animations/ai/neural_network.py NeuronActivation
```

**Key Features:**
- Labeled axes showing input and output ranges
- Smooth curve plotting
- Interactive point showing function behavior

---

### Gradient Descent 2D

**File:** `animations/ai/gradient_descent.py`  
**Scene:** `GradientDescentScene`

**Description:**
Visualizes the gradient descent optimization algorithm on a quadratic loss function.

**Command:**
```bash
manim -pql animations/ai/gradient_descent.py GradientDescentScene
```

**Key Features:**
- Loss function visualization (parabola)
- Tangent lines showing gradients
- Step-by-step parameter updates
- Formula: θₙₑw = θₒₗd - α·∇J(θ)
- Convergence to minimum

**Parameters:**
- Learning rate: 0.4 (adjustable)
- Starting point: x = -2.5
- Number of iterations: Up to 8 steps

---

### Gradient Descent 3D

**File:** `animations/ai/gradient_descent.py`  
**Scene:** `GradientDescent3D`

**Description:**
3D visualization of gradient descent on a paraboloid surface.

**Command:**
```bash
manim -pql animations/ai/gradient_descent.py GradientDescent3D
```

**Key Features:**
- Interactive 3D surface (z = x² + y²)
- Optimization path visualization
- Camera rotation for better viewing
- Red sphere tracking the descent path

---

## Linear Algebra Animations

### Matrix Transformations

**File:** `animations/linear_algebra/transformations.py`  
**Scene:** `MatrixTransformation`

**Description:**
Shows how matrices transform the coordinate plane through rotation and scaling.

**Command:**
```bash
manim -pql animations/linear_algebra/transformations.py MatrixTransformation
```

**Key Features:**
- Grid transformation visualization
- Rotation matrix (45-degree rotation)
- Scaling matrix (2x horizontal, 0.5x vertical)
- Basis vector tracking
- Ghost vectors showing original positions

---

### Eigenvalue Visualization

**File:** `animations/linear_algebra/transformations.py`  
**Scene:** `EigenvalueVisualization`

**Description:**
Demonstrates eigenvectors and eigenvalues - vectors that maintain their direction under transformation.

**Command:**
```bash
manim -pql animations/linear_algebra/transformations.py EigenvalueVisualization
```

**Key Features:**
- Multiple test vectors
- One eigenvector (direction preserved)
- Matrix transformation application
- Clear distinction between eigenvectors and regular vectors

**Matrix Used:**
```
A = [1.5  0.5]
    [0.5  1.5]
```
Eigenvalue: λ = 2 for eigenvector [1, 1]

---

### Dot Product Visualization

**File:** `animations/linear_algebra/transformations.py`  
**Scene:** `DotProductVisualization`

**Description:**
Geometric interpretation of the dot product between two vectors.

**Command:**
```bash
manim -pql animations/linear_algebra/transformations.py DotProductVisualization
```

**Key Features:**
- Two vectors in 2D space
- Angle between vectors
- Projection visualization
- Formula: a⃗·b⃗ = |a⃗||b⃗|cosθ

---

## Calculus Animations

### Derivative Visualization

**File:** `animations/calculus/derivatives_integrals.py`  
**Scene:** `DerivativeVisualization`

**Description:**
Shows how derivatives arise as limits of secant lines becoming tangent lines.

**Command:**
```bash
manim -pql animations/calculus/derivatives_integrals.py DerivativeVisualization
```

**Key Features:**
- Function: f(x) = x²
- Secant lines with decreasing h values
- Convergence to tangent line
- Derivative formula: f'(x) = 2x

**Educational Concepts:**
- Slope of secant line: (f(x+h) - f(x)) / h
- Limit as h → 0
- Instantaneous rate of change

---

### Integral Visualization

**File:** `animations/calculus/derivatives_integrals.py`  
**Scene:** `IntegralVisualization`

**Description:**
Demonstrates Riemann sums approximating the definite integral.

**Command:**
```bash
manim -pql animations/calculus/derivatives_integrals.py IntegralVisualization
```

**Key Features:**
- Function: f(x) = ½x² + 1
- Increasing number of rectangles (4, 8, 16, 32)
- Area approximation improving with more rectangles
- Limit formula displayed

**Integration Bounds:** [0.5, 3]

---

### Limit Visualization

**File:** `animations/calculus/derivatives_integrals.py`  
**Scene:** `LimitVisualization`

**Description:**
Visualizes limits and removable discontinuities.

**Command:**
```bash
manim -pql animations/calculus/derivatives_integrals.py LimitVisualization
```

**Key Features:**
- Function: f(x) = (x² - 4)/(x - 2)
- Removable discontinuity at x = 2
- Left and right limit approach
- Both limits converge to same value (4)

---

## Creating Custom Animations

### Using These as Templates

All animations are designed to be:
- Easy to understand and modify
- Well-documented with comments
- Parameterized for easy customization

### Example: Modify Neural Network

```python
# Change network architecture
input_layer = self.create_layer(5, "Input")      # 5 inputs instead of 3
hidden_layer1 = self.create_layer(10, "Hidden")  # 10 neurons instead of 4

# Change colors
neuron = Circle(radius=0.2, color=GREEN, fill_color=PURPLE)

# Change animation speed
self.play(Create(neurons), run_time=3)  # Slower animation
```

### Example: Modify Gradient Descent

```python
# Different loss function
def loss_function(x):
    return x**4 - 3*x**2 + 2  # More complex function

# Adjust learning rate
learning_rate = 0.1  # Smaller steps

# Different starting point
start_x = -1.5
```

## Tips for Best Results

1. **Start with low quality (`-ql`)** for quick iteration
2. **Use high quality (`-qh`)** for presentations
3. **Adjust `run_time`** parameter to control animation speed
4. **Modify colors** to match your theme or preferences
5. **Add custom text** for specific teaching points
6. **Combine scenes** to create longer presentations

## Advanced Usage

### Generate GIF Instead of MP4

```bash
manim -ql --format=gif animations/ai/neural_network.py NeuralNetworkScene
```

### Save Only Last Frame (Image)

```bash
manim -qh --save_last_frame animations/ai/neural_network.py NeuralNetworkScene
```

### Custom Resolution

```bash
manim --resolution 1920,1080 animations/ai/neural_network.py NeuralNetworkScene
```

### Transparent Background

```bash
manim -ql --transparent animations/ai/neural_network.py NeuralNetworkScene
```
