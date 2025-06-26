# Contributing to Zomato Scraper

Thank you for your interest in contributing to Zomato Scraper! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Bugs

Before creating bug reports, please check the existing issues to see if the problem has already been reported. When creating a bug report, include:

- **Clear and descriptive title**
- **Detailed description of the problem**
- **Steps to reproduce the issue**
- **Expected vs actual behavior**
- **Environment details** (OS, Python version, etc.)
- **Error messages or logs**

### Suggesting Enhancements

We welcome feature requests! When suggesting enhancements:

- **Describe the feature clearly**
- **Explain why this feature would be useful**
- **Provide examples of how it would work**
- **Consider the impact on existing functionality**

### Code Contributions

#### Development Setup

1. **Fork the repository**
2. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/zomato-scraper.git
   cd zomato-scraper
   ```
3. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

#### Coding Standards

- **Follow PEP 8** style guidelines
- **Use meaningful variable and function names**
- **Add docstrings** for all functions and classes
- **Write clear, concise code**
- **Handle exceptions appropriately**
- **Add type hints** where applicable

#### Testing

- **Test your changes thoroughly**
- **Ensure the scraper works with different locations**
- **Verify JSON output is valid**
- **Check for any breaking changes**

#### Commit Guidelines

Use clear, descriptive commit messages:

```bash
# Good examples
git commit -m "Add error handling for network timeouts"
git commit -m "Fix menu extraction for restaurants with special characters"
git commit -m "Update User-Agent to latest Chrome version"

# Avoid
git commit -m "fix bug"
git commit -m "update code"
```

#### Pull Request Process

1. **Ensure your code follows the project's style guidelines**
2. **Update documentation** if needed
3. **Add tests** for new functionality
4. **Update the README** if you've added new features
5. **Create a pull request** with a clear description
6. **Link any related issues**

### Pull Request Template

When creating a pull request, please use this template:

```markdown
## Description
Brief description of the changes made.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Performance improvement

## Testing
- [ ] Tested locally
- [ ] Verified with different locations
- [ ] Checked JSON output validity

## Checklist
- [ ] Code follows PEP 8 style guidelines
- [ ] Added appropriate docstrings
- [ ] Updated documentation if needed
- [ ] No breaking changes introduced
```

## 🏗️ Project Structure

```
zomato-scraper/
├── main.py              # Main execution script
├── zomato_scrapper.py   # Core scraper class
├── location.py          # Location detection utilities
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
├── LICENSE             # MIT License
├── CONTRIBUTING.md     # This file
├── .gitignore          # Git ignore rules
├── restaurant_data/    # Generated restaurant data
└── menus/             # Generated menu data
```

## 🐛 Common Issues

### Rate Limiting
If you encounter rate limiting:
- Add delays between requests
- Implement exponential backoff
- Use rotating User-Agents

### Location Detection
If location detection fails:
- Check internet connectivity
- Verify IP geolocation services are accessible
- Consider fallback location services

### JSON Parsing Errors
If JSON parsing fails:
- Verify the response structure hasn't changed
- Add error handling for malformed JSON
- Check for encoding issues

## 📞 Getting Help

- **Open an issue** for bugs or feature requests
- **Check existing issues** for solutions
- **Review the README** for usage examples
- **Test with different locations** to ensure compatibility

## 🎯 Areas for Contribution

We're particularly interested in contributions for:

- **Error handling improvements**
- **Performance optimizations**
- **Additional data extraction**
- **Better documentation**
- **Testing framework**
- **Configuration management**
- **Rate limiting improvements**

## 📝 Code of Conduct

- **Be respectful** to all contributors
- **Provide constructive feedback**
- **Help others learn and grow**
- **Follow the project's coding standards**
- **Respect the educational nature** of this project

## 🙏 Recognition

Contributors will be recognized in:
- **README.md** contributors section
- **Release notes**
- **Project documentation**

Thank you for contributing to Zomato Scraper! 🚀 