# Contributing to Manim Animations

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:

1. Check if the issue already exists in the [issue tracker](https://github.com/jgoth/manim_anims/issues)
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Your environment (OS, Python version, Manim version)

### Adding New Animations

We welcome new animations! Here's how to add one:

1. **Fork the repository**
2. **Create a new branch** for your animation
   ```bash
   git checkout -b add-new-animation
   ```

3. **Choose the appropriate directory:**
   - `animations/ai/` - AI and machine learning topics
   - `animations/linear_algebra/` - Linear algebra concepts
   - `animations/calculus/` - Calculus visualizations
   - Create a new directory if your topic doesn't fit existing categories

4. **Write your animation:**
   - Follow the existing code style
   - Add docstrings to classes and methods
   - Use meaningful variable names
   - Add comments for complex logic

5. **Test your animation:**
   ```bash
   manim -pql animations/your_category/your_file.py YourScene
   ```

6. **Update documentation:**
   - Add your animation to README.md
   - Add examples to examples/EXAMPLES.md
   - Update `__init__.py` if needed

7. **Commit your changes:**
   ```bash
   git add .
   git commit -m "Add [animation name] visualization"
   ```

8. **Push and create a pull request:**
   ```bash
   git push origin add-new-animation
   ```

### Code Style Guidelines

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to all classes and non-trivial functions
- Keep animations modular and reusable
- Use type hints where appropriate

Example:

```python
"""
Module description.
"""

from manim import *


class MyAnimation(Scene):
    """Brief description of what this animation shows."""
    
    def construct(self):
        """Build and run the animation."""
        # Your code here
        pass
    
    def helper_method(self, param: float) -> Mobject:
        """
        Helper method description.
        
        Args:
            param: Description of parameter
            
        Returns:
            Description of return value
        """
        # Implementation
        pass
```

### Animation Best Practices

1. **Keep it simple:** Focus on one concept per animation
2. **Use colors effectively:** Maintain visual consistency
3. **Add labels:** Help viewers understand what they're seeing
4. **Control pacing:** Use appropriate `run_time` and `wait()` calls
5. **Make it educational:** Animations should teach, not just look pretty

### Improving Existing Animations

Found a way to improve an existing animation? Great!

1. Fork and create a branch
2. Make your improvements
3. Test thoroughly
4. Document what you changed in the commit message
5. Submit a pull request

### Documentation Contributions

Documentation improvements are always welcome:

- Fix typos or unclear explanations
- Add more examples
- Improve installation instructions
- Add troubleshooting tips

## Pull Request Process

1. Ensure your code runs without errors
2. Update relevant documentation
3. Test your changes on different quality settings
4. Provide a clear description of changes in the PR
5. Link any related issues

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome newcomers and beginners
- Provide constructive feedback
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discriminatory language
- Personal attacks
- Publishing others' private information
- Other unethical or unprofessional conduct

## Questions?

Feel free to:
- Open an issue for discussion
- Ask in pull request comments
- Reach out to maintainers

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Attribution

Contributors will be acknowledged in release notes and the project's contributor list.

Thank you for making this project better!
