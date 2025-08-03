# Contributing to HasHub Vector SDK

We love your input! We want to make contributing to HasHub Vector SDK as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## 🚀 Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

### Pull Requests Process

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code lints
6. Issue that pull request!

### Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/HasHub-vector-sdk.git
cd HasHub-vector-sdk

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=HasHub_vector --cov-report=html

# Run specific test file
pytest tests/test_client.py

# Run specific test
pytest tests/test_client.py::TestHasHubVector::test_vectorize_success
```

### Code Style

We use several tools to maintain code quality:

```bash
# Format code
black hashub_vector/ tests/ examples/

# Sort imports
isort hashub_vector/ tests/ examples/

# Lint code
flake8 hashub_vector/ tests/

# Type checking
mypy hashub_vector/
```

All of these run automatically with pre-commit hooks.

## 🐛 Bug Reports

We use GitHub issues to track public bugs. Report a bug by opening a new issue.

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

**Bug Report Template:**

```markdown
## Bug Description
Brief description of the bug

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- SDK Version: 
- Python Version:
- OS:

## Additional Context
Any other context about the problem
```

## 💡 Feature Requests

We welcome feature requests! Please provide:

- **Use case**: Why do you need this feature?
- **Proposed solution**: How should it work?
- **Alternatives**: What alternatives have you considered?
- **Additional context**: Screenshots, mockups, etc.

## 📋 Development Guidelines

### Code Organization

```
hashub_vector/
├── __init__.py          # Package exports
├── client.py            # Main client class
├── models.py            # Data models and schemas
├── exceptions.py        # Custom exceptions
└── utils.py             # Utility functions (if needed)

tests/
├── __init__.py
├── test_client.py       # Client tests
├── test_models.py       # Model tests
└── test_exceptions.py   # Exception tests

examples/
├── basic_usage.py       # Basic examples
├── langchain_integration.py
└── production_rag.py
```

### Coding Standards

1. **Python Version Compatibility**: Support Python 3.8+
2. **Type Hints**: Use type hints for all public APIs
3. **Docstrings**: Follow Google-style docstrings
4. **Error Handling**: Provide clear, actionable error messages
5. **Async Support**: Provide async versions of I/O operations
6. **Backwards Compatibility**: Don't break existing APIs without major version bump

### Example Code Style

```python
from typing import List, Optional, Dict, Any
import asyncio

class ExampleClass:
    """
    Example class following our coding standards.
    
    Args:
        api_key: The API key for authentication
        model: The model to use for embeddings
        timeout: Request timeout in seconds
    """
    
    def __init__(
        self,
        api_key: str,
        model: str = "e5_base",
        timeout: float = 30.0
    ):
        if not api_key:
            raise ValueError("API key is required")
        
        self.api_key = api_key
        self.model = model
        self.timeout = timeout
    
    def process_text(self, text: str) -> Dict[str, Any]:
        """
        Process a single text.
        
        Args:
            text: The text to process
            
        Returns:
            Processing results
            
        Raises:
            ValueError: If text is empty
        """
        if not text.strip():
            raise ValueError("Text cannot be empty")
        
        # Implementation here
        return {"processed": True}
    
    async def aprocess_text(self, text: str) -> Dict[str, Any]:
        """Async version of process_text."""
        # Async implementation
        return await asyncio.sleep(0.1, {"processed": True})
```

### Testing Guidelines

1. **Test Coverage**: Aim for >90% test coverage
2. **Test Types**: Unit tests, integration tests, and async tests
3. **Mock External Calls**: Use mocks for HTTP requests
4. **Test Edge Cases**: Test error conditions and edge cases
5. **Parameterized Tests**: Use pytest.mark.parametrize for multiple test cases

### Documentation Standards

1. **API Documentation**: Complete docstrings for all public methods
2. **Examples**: Include usage examples in docstrings
3. **README**: Keep README.md up to date
4. **Changelog**: Update CHANGELOG.md for all changes
5. **Type Stubs**: Maintain py.typed file for type checking

## 🔄 Release Process

1. **Version Bumping**: Use semantic versioning (MAJOR.MINOR.PATCH)
2. **Changelog**: Update CHANGELOG.md with new features and fixes
3. **Documentation**: Update documentation for new features
4. **Testing**: Ensure all tests pass
5. **Tagging**: Create git tag for release
6. **PyPI**: Release to PyPI using GitHub Actions

## 🏷️ Versioning

We use [Semantic Versioning](http://semver.org/):

- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality (backwards compatible)
- **PATCH**: Bug fixes (backwards compatible)

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🤝 Code of Conduct

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone.

### Our Standards

Examples of behavior that contributes to creating a positive environment:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team at [support@hashub.dev](mailto:support@hashub.dev).

## 🎯 Areas We Need Help

- **Turkish Language Support**: Improving Turkish text processing
- **Performance Optimization**: Making embeddings faster
- **Integration Examples**: More framework integrations
- **Documentation**: Tutorials and guides
- **Testing**: More comprehensive test coverage
- **Error Handling**: Better error messages and recovery

## 📞 Contact

- **Email**: [support@hashub.dev](mailto:support@hashub.dev)
- **GitHub Issues**: [Issues Page](https://github.com/hashub-ai/hashub-vector-sdk/issues)
- **Discord**: [HasHub Community](https://discord.gg/hashub)

Thank you for contributing to HasHub Vector SDK! 🚀
