# Quick Start Guide

## Installation

### 1. Install System Dependencies

Manim requires some system-level dependencies. Install them based on your operating system:

#### Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install -y \
    build-essential \
    python3-dev \
    libcairo2-dev \
    libpango1.0-dev \
    ffmpeg
```

#### macOS:
```bash
brew install cairo pango ffmpeg
```

#### Windows:
Follow the [official Manim installation guide](https://docs.manim.community/en/stable/installation.html) for Windows.

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or install manim directly:
```bash
pip install manim
```

## Running Your First Animation

### Example 1: Neural Network Visualization

```bash
manim -pql animations/ai/neural_network.py NeuralNetworkScene
```

This will:
- Render the animation at low quality (480p)
- Preview the video automatically after rendering (`-p`)
- Save the output in `media/videos/`

### Example 2: Gradient Descent

```bash
manim -pql animations/ai/gradient_descent.py GradientDescentScene
```

### Example 3: Matrix Transformations

```bash
manim -pql animations/linear_algebra/transformations.py MatrixTransformation
```

## Quality Settings

- `-ql`: Low quality (480p, 15 fps) - Fast rendering for testing
- `-qm`: Medium quality (720p, 30 fps) - Good for most purposes
- `-qh`: High quality (1080p, 60 fps) - High quality output
- `-qk`: 4K quality (2160p, 60 fps) - Maximum quality

Example with high quality:
```bash
manim -pqh animations/ai/neural_network.py NeuralNetworkScene
```

## Output Location

By default, animations are saved to:
```
media/
├── videos/
│   └── [filename]/
│       └── [quality]/
│           └── [SceneName].mp4
└── images/
    └── [filename]/
        └── [SceneName].png
```

## Customizing Animations

### Modify Existing Animations

All animation files are well-documented. You can:

1. Open any `.py` file in the `animations/` directory
2. Modify parameters like colors, speeds, positions
3. Re-render to see your changes

### Example Modification

In `animations/ai/neural_network.py`, you can change the neural network structure:

```python
# Original
input_layer = self.create_layer(3, "Input\nLayer")
hidden_layer1 = self.create_layer(4, "Hidden\nLayer 1")

# Modified - larger network
input_layer = self.create_layer(5, "Input\nLayer")
hidden_layer1 = self.create_layer(8, "Hidden\nLayer 1")
```

## Creating New Animations

### Basic Template

Create a new file in `animations/`:

```python
from manim import *

class MyNewScene(Scene):
    def construct(self):
        # Your animation code
        title = Text("My Animation")
        self.play(Write(title))
        self.wait()
```

Render it:
```bash
manim -pql animations/my_new_scene.py MyNewScene
```

## Troubleshooting

### Common Issues

1. **"ModuleNotFoundError: No module named 'manim'"**
   - Solution: Install manim: `pip install manim`

2. **"Package 'pangocairo' was not found"**
   - Solution: Install system dependencies (see Installation section)

3. **"RuntimeError: No such file or directory: 'ffmpeg'"**
   - Solution: Install ffmpeg: `sudo apt-get install ffmpeg` (Ubuntu) or `brew install ffmpeg` (macOS)

4. **Animation renders but doesn't preview**
   - Solution: Remove the `-p` flag or check your video player

### Getting Help

- [Manim Community Documentation](https://docs.manim.community/)
- [Manim Community Discord](https://discord.gg/mMRrZQW)
- [GitHub Issues](https://github.com/jgoth/manim_anims/issues)

## Next Steps

1. Explore all available animations (see README.md)
2. Try different quality settings
3. Modify existing animations
4. Create your own custom animations
5. Share your work!

## Tips

- Start with low quality (`-ql`) for faster iteration
- Use high quality (`-qh`) only for final renders
- Preview animations (`-p`) to see results immediately
- Check the `media/` folder for all rendered outputs
- Use `--save_last_frame` to save a still image instead of video
