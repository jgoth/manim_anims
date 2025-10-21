#!/usr/bin/env python3
"""
Simple example script showing how to import and use animations.
This demonstrates the animation modules can be imported as Python packages.
"""

# Note: This script requires manim to be installed
# Install with: pip install manim

try:
    from animations.ai.neural_network import NeuralNetworkScene, NeuronActivation
    from animations.ai.gradient_descent import GradientDescentScene, GradientDescent3D
    from animations.linear_algebra.transformations import (
        MatrixTransformation,
        EigenvalueVisualization,
        DotProductVisualization,
    )
    from animations.calculus.derivatives_integrals import (
        DerivativeVisualization,
        IntegralVisualization,
        LimitVisualization,
    )
    
    print("✓ All animation modules imported successfully!")
    print("\nAvailable Scenes:")
    print("\nAI & Machine Learning:")
    print("  - NeuralNetworkScene")
    print("  - NeuronActivation")
    print("  - GradientDescentScene")
    print("  - GradientDescent3D")
    print("\nLinear Algebra:")
    print("  - MatrixTransformation")
    print("  - EigenvalueVisualization")
    print("  - DotProductVisualization")
    print("\nCalculus:")
    print("  - DerivativeVisualization")
    print("  - IntegralVisualization")
    print("  - LimitVisualization")
    print("\nTo render any scene, use:")
    print("  manim -pql animations/[category]/[file].py [SceneName]")
    print("\nExample:")
    print("  manim -pql animations/ai/neural_network.py NeuralNetworkScene")
    
except ImportError as e:
    print(f"✗ Import error: {e}")
    print("\nMake sure manim is installed:")
    print("  pip install manim")
    print("\nFor system dependencies, see QUICKSTART.md")
