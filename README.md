# Manim Animations for AI and Mathematics

A collection of beautiful mathematical animations created with [Manim](https://www.manim.community/) focusing on artificial intelligence concepts and mathematical topics.

## Overview

This repository contains ready-to-use Manim animations covering:

- **AI & Machine Learning**: Neural networks, gradient descent, activation functions
- **Linear Algebra**: Matrix transformations, eigenvectors, dot products
- **Calculus**: Derivatives, integrals, limits

## Installation

### Prerequisites

- Python 3.8 or higher
- Manim Community Edition

### Setup

1. Clone this repository:
```bash
git clone https://github.com/jgoth/manim_anims.git
cd manim_anims
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Or install manim directly:
```bash
pip install manim
```

## Usage

To render any animation, use the `manim` command:

```bash
manim -pql animations/ai/neural_network.py NeuralNetworkScene
```

### Command Line Options

- `-p`: Preview the animation after rendering
- `-ql`: Render at low quality (480p, faster)
- `-qm`: Render at medium quality (720p)
- `-qh`: Render at high quality (1080p)
- `-qk`: Render at 4K quality (2160p)

### Examples

#### AI Animations

**Neural Network Visualization:**
```bash
manim -pql animations/ai/neural_network.py NeuralNetworkScene
```

**Neuron Activation Function:**
```bash
manim -pql animations/ai/neural_network.py NeuronActivation
```

**Gradient Descent (2D):**
```bash
manim -pql animations/ai/gradient_descent.py GradientDescentScene
```

**Gradient Descent (3D):**
```bash
manim -pql animations/ai/gradient_descent.py GradientDescent3D
```

#### Linear Algebra Animations

**Matrix Transformations:**
```bash
manim -pql animations/linear_algebra/transformations.py MatrixTransformation
```

**Eigenvalue Visualization:**
```bash
manim -pql animations/linear_algebra/transformations.py EigenvalueVisualization
```

**Dot Product Geometric Interpretation:**
```bash
manim -pql animations/linear_algebra/transformations.py DotProductVisualization
```

#### Calculus Animations

**Derivative Visualization:**
```bash
manim -pql animations/calculus/derivatives_integrals.py DerivativeVisualization
```

**Integral (Riemann Sums):**
```bash
manim -pql animations/calculus/derivatives_integrals.py IntegralVisualization
```

**Limits:**
```bash
manim -pql animations/calculus/derivatives_integrals.py LimitVisualization
```

## Project Structure

```
manim_anims/
├── animations/
│   ├── ai/
│   │   ├── neural_network.py      # Neural network visualizations
│   │   └── gradient_descent.py    # Gradient descent animations
│   ├── linear_algebra/
│   │   └── transformations.py     # Matrix and vector animations
│   └── calculus/
│       └── derivatives_integrals.py # Calculus concepts
├── requirements.txt
├── pyproject.toml
├── LICENSE
└── README.md
```

## Available Animations

### AI & Machine Learning

| Scene Name | Description | File |
|------------|-------------|------|
| `NeuralNetworkScene` | Visualization of a feedforward neural network with signal propagation | `ai/neural_network.py` |
| `NeuronActivation` | Animation of sigmoid activation function | `ai/neural_network.py` |
| `GradientDescentScene` | 2D gradient descent optimization | `ai/gradient_descent.py` |
| `GradientDescent3D` | 3D visualization of gradient descent on a surface | `ai/gradient_descent.py` |

### Linear Algebra

| Scene Name | Description | File |
|------------|-------------|------|
| `MatrixTransformation` | Matrix transformations (rotation, scaling) | `linear_algebra/transformations.py` |
| `EigenvalueVisualization` | Eigenvectors and eigenvalues demonstration | `linear_algebra/transformations.py` |
| `DotProductVisualization` | Geometric interpretation of dot product | `linear_algebra/transformations.py` |

### Calculus

| Scene Name | Description | File |
|------------|-------------|------|
| `DerivativeVisualization` | Concept of derivatives as limits of secant lines | `calculus/derivatives_integrals.py` |
| `IntegralVisualization` | Riemann sums converging to definite integral | `calculus/derivatives_integrals.py` |
| `LimitVisualization` | Limits and removable discontinuities | `calculus/derivatives_integrals.py` |

## Creating Your Own Animations

You can use these animations as templates for your own work. Each animation file contains well-documented classes that you can modify or extend.

Basic structure of a Manim scene:

```python
from manim import *

class MyScene(Scene):
    def construct(self):
        # Your animation code here
        text = Text("Hello, Manim!")
        self.play(Write(text))
        self.wait()
```

## Contributing

Contributions are welcome! Feel free to:

- Add new animations
- Improve existing animations
- Fix bugs
- Improve documentation

## Resources

- [Manim Community Documentation](https://docs.manim.community/)
- [Manim Community Discord](https://discord.gg/mMRrZQW)
- [3Blue1Brown's Original Manim](https://github.com/3b1b/manim)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Manim Community](https://www.manim.community/) for the excellent animation engine
- [3Blue1Brown](https://www.3blue1brown.com/) for inspiring mathematical visualizations
