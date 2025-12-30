# Contributing to Lorenz Phase Space

Thank you for your interest in contributing to the Lorenz Phase Space project! 

## Development Setup

1. **Clone the repository:**
```bash
git clone https://github.com/daniloceano/lorenz_phase_space.git
cd lorenz_phase_space
```

2. **Install in development mode:**
```bash
pip install -e .
pip install -r requirements.txt
```

3. **Run tests:**
```bash
python -m unittest tests.test_lps -v
```

## Code Style

- Follow PEP 8 guidelines
- Use NumPy-style docstrings for all functions and classes
- Add type hints where appropriate
- Keep line length under 100 characters

## Making Changes

1. **Create a new branch:**
```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes:**
   - Add/modify code
   - Update documentation
   - Add tests for new features

3. **Run tests:**
```bash
python -m unittest tests.test_lps -v
```

4. **Verify visual output:**
```bash
cd tests
python test_lps.py
# Check plots in tests/test_outputs/
```

## Testing Requirements

- All new features must include tests
- Visual changes require manual verification
- Tests must pass before submitting PR
- Maintain or improve code coverage

## Documentation

When adding new features:

1. **Update docstrings** in the code
2. **Update API documentation** (`docs/API_DOCUMENTATION.md`)
3. **Add examples** if applicable
4. **Update CHANGELOG.md**

## Pull Request Process

1. **Ensure tests pass**
2. **Update documentation**
3. **Add entry to CHANGELOG.md**
4. **Verify visual outputs** if plotting changes were made
5. **Submit PR** with clear description of changes

## Important Notes

⚠️ **Do not modify plotting logic** without discussion - the visual output is carefully calibrated

⚠️ **Always verify visual output** - automated tests cannot catch all visual issues

## Questions?

Contact: danilo.oceano@gmail.com

Thank you for contributing! 🎉
