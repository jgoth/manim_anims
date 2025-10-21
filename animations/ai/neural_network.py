"""
Neural Network Visualization Animation
A simple visualization of a feedforward neural network with manim.
"""

from manim import *


class NeuralNetworkScene(Scene):
    """Animated visualization of a neural network structure."""
    
    def construct(self):
        # Title
        title = Text("Neural Network", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Create layers
        input_layer = self.create_layer(3, "Input\nLayer")
        hidden_layer1 = self.create_layer(4, "Hidden\nLayer 1")
        hidden_layer2 = self.create_layer(4, "Hidden\nLayer 2")
        output_layer = self.create_layer(2, "Output\nLayer")
        
        # Position layers
        input_layer.shift(LEFT * 4)
        hidden_layer1.shift(LEFT * 1.5)
        hidden_layer2.shift(RIGHT * 1.5)
        output_layer.shift(RIGHT * 4)
        
        layers = VGroup(input_layer, hidden_layer1, hidden_layer2, output_layer)
        layers.shift(DOWN * 0.5)
        
        # Create connections
        connections = VGroup()
        layer_pairs = [
            (input_layer, hidden_layer1),
            (hidden_layer1, hidden_layer2),
            (hidden_layer2, output_layer)
        ]
        
        for layer1, layer2 in layer_pairs:
            neurons1 = layer1[0]
            neurons2 = layer2[0]
            for n1 in neurons1:
                for n2 in neurons2:
                    line = Line(
                        n1.get_center(),
                        n2.get_center(),
                        stroke_width=1,
                        stroke_opacity=0.3,
                        color=BLUE
                    )
                    connections.add(line)
        
        # Animate creation
        self.play(Create(connections), run_time=2)
        self.play(LaggedStart(*[Create(layer) for layer in layers], lag_ratio=0.3))
        self.wait(1)
        
        # Animate signal propagation
        self.animate_signal_propagation(layers, connections)
        
        self.wait(2)
    
    def create_layer(self, num_neurons, label_text):
        """Create a layer of neurons with a label."""
        neurons = VGroup()
        for i in range(num_neurons):
            neuron = Circle(radius=0.2, color=WHITE, fill_opacity=0.8, fill_color=BLUE)
            neurons.add(neuron)
        
        neurons.arrange(DOWN, buff=0.5)
        
        label = Text(label_text, font_size=20)
        label.next_to(neurons, DOWN, buff=0.3)
        
        return VGroup(neurons, label)
    
    def animate_signal_propagation(self, layers, connections):
        """Animate signal propagation through the network."""
        # Highlight input neurons
        input_neurons = layers[0][0]
        self.play(*[neuron.animate.set_fill(YELLOW, opacity=1) for neuron in input_neurons])
        self.wait(0.3)
        
        # Propagate through each layer
        for i in range(len(layers) - 1):
            current_layer = layers[i][0]
            next_layer = layers[i + 1][0]
            
            # Pulse connections
            relevant_connections = VGroup()
            for conn in connections:
                start = conn.get_start()
                for neuron in current_layer:
                    if np.allclose(start, neuron.get_center(), atol=0.01):
                        relevant_connections.add(conn)
                        break
            
            self.play(
                *[conn.animate.set_stroke(YELLOW, width=2, opacity=0.8) 
                  for conn in relevant_connections],
                run_time=0.5
            )
            
            # Activate next layer
            self.play(
                *[neuron.animate.set_fill(YELLOW, opacity=1) for neuron in next_layer],
                run_time=0.5
            )
            
            # Reset current layer and connections
            self.play(
                *[neuron.animate.set_fill(BLUE, opacity=0.8) for neuron in current_layer],
                *[conn.animate.set_stroke(BLUE, width=1, opacity=0.3) 
                  for conn in relevant_connections],
                run_time=0.3
            )
        
        # Keep output layer highlighted
        self.wait(1)


class NeuronActivation(Scene):
    """Animation showing neuron activation function."""
    
    def construct(self):
        title = Text("Neuron Activation", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create axes for activation function
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-0.2, 1.2, 0.2],
            x_length=8,
            y_length=4,
            axis_config={"include_numbers": True, "font_size": 24},
        )
        axes.shift(DOWN * 0.5)
        
        # Labels
        x_label = axes.get_x_axis_label("Input (x)")
        y_label = axes.get_y_axis_label("Output", edge=LEFT, direction=LEFT)
        
        # Sigmoid function
        sigmoid = axes.plot(
            lambda x: 1 / (1 + np.exp(-x)),
            color=YELLOW,
            x_range=[-5, 5]
        )
        
        sigmoid_label = Text("Sigmoid: σ(x) = 1/(1+e⁻ˣ)", font_size=30)
        sigmoid_label.next_to(axes, DOWN, buff=0.5)
        
        # Animate
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)
        self.play(Create(sigmoid), run_time=2)
        self.play(Write(sigmoid_label))
        
        # Show point moving along curve
        dot = Dot(color=RED)
        dot.move_to(axes.c2p(-5, 1 / (1 + np.exp(5))))
        
        self.play(Create(dot))
        self.play(
            MoveAlongPath(dot, sigmoid),
            run_time=4,
            rate_func=linear
        )
        
        self.wait(2)
