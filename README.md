# 🍕 Zomato Scraper

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)](https://github.com/224Abhay/zomato-scraper)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/224Abhay/zomato-scraper/graphs/commit-activity)

A high-performance Python scraper that extracts restaurant data and menus from Zomato using their web APIs. This tool automatically detects your location via IP geolocation and fetches comprehensive restaurant information including menus, ratings, and delivery details.

## ✨ Features

- 🎯 **Automatic Location Detection** - Uses IP-based geolocation to determine your current area
- 🏪 **Restaurant Discovery** - Scrapes comprehensive restaurant listings with ratings, cuisines, and delivery info
- 📋 **Menu Extraction** - Retrieves detailed menu information including prices, descriptions, and categories
- ⚡ **High Performance** - Optimized for speed with session management and efficient API calls
- 📊 **JSON Output** - Clean, structured data output for easy analysis and integration
- 🔄 **Pagination Support** - Handles multiple pages of restaurant results
- 🛡️ **Robust Error Handling** - Graceful handling of network issues and API changes

## 📋 Table of Contents

- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage Examples](#-usage-examples)
- [API Reference](#-api-reference)
- [Data Structure](#-data-structure)
- [Configuration](#-configuration)
- [Contributing](#-contributing)
- [Disclaimer](#-disclaimer)
- [License](#-license)

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Step-by-Step Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/224Abhay/zomato-scraper.git
   cd zomato-scraper
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   # For Windows
   python -m venv venv
   venv\Scripts\activate

   # For macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Quick Start

Run the scraper with a simple command:

```bash
python main.py
```

This will:
1. Detect your current location
2. Fetch restaurant listings from your area
3. Extract menu data from the first restaurant
4. Save results to JSON files

## 📖 Usage Examples

### Basic Usage

```python
from zomato_scrapper import zomato

# Initialize the scraper
scraper = zomato()

# Get restaurant listings
restaurants = scraper.get_restaurants(write_json=True)

# Get menu for a specific restaurant
menu_data = scraper.get_menu(restaurants[1], write_json=True)
```

### Advanced Usage

```python
from zomato_scrapper import zomato

# Initialize scraper
scraper = zomato()

# Get multiple pages of restaurants
for page in range(3):
    restaurants = scraper.get_restaurants(write_json=True)
    print(f"Fetched {len(restaurants)} restaurants from page {page + 1}")

# Get menus for multiple restaurants
for restaurant in restaurants[:5]:  # First 5 restaurants
    menu = scraper.get_menu(restaurant, write_json=True)
    print(f"Menu extracted for: {restaurant['info']['name']}")
```

## 🔧 API Reference

### `zomato()` Class

Main scraper class that handles all interactions with Zomato.

#### Methods

##### `get_restaurants(write_json=False)`
Fetches restaurant listings for the current location.

**Parameters:**
- `write_json` (bool): Whether to save results to JSON file (default: False)

**Returns:**
- `list`: List of restaurant data dictionaries

##### `get_menu(restaurant_data, write_json=False)`
Extracts menu information for a specific restaurant.

**Parameters:**
- `restaurant_data` (dict): Restaurant data from `get_restaurants()`
- `write_json` (bool): Whether to save results to JSON file (default: False)

**Returns:**
- `dict`: Menu data dictionary

## 📊 Data Structure

### Restaurant Data
```json
{
  "info": {
    "name": "Restaurant Name",
    "rating": 4.2,
    "cuisines": ["Italian", "Pizza"],
    "deliveryTime": "30-35 min"
  },
  "order": {
    "actionInfo": {
      "clickUrl": "/restaurant-url"
    }
  }
}
```

### Menu Data
```json
{
  "page_data": {
    "sections": {
      "SECTION_BASIC_INFO": {
        "restaurant_name": "Restaurant Name",
        "cuisines": "Italian, Pizza"
      },
      "SECTION_MENU": {
        "categories": [...]
      }
    }
  }
}
```

## ⚙️ Configuration

### User-Agent and Headers
The scraper uses custom headers to mimic a browser. You can modify these in the `zomato` class:

```python
self.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...",
    "Content-Type": "application/json",
}
```

### Geolocation Services
The scraper uses `ipify.org` and `ipinfo.io` for location detection. You can replace these with alternative services in `location.py`.

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes and commit:**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to your branch:**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Development Setup

1. Clone your fork
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Make your changes
5. Test thoroughly
6. Submit a PR

## 📝 Disclaimer

⚠️ **Important Notice**

This project is developed for **educational purposes only** and is not affiliated with or endorsed by Zomato. 

**Please ensure your use of this tool complies with:**
- Zomato's Terms of Service
- Applicable laws and regulations
- Rate limiting and respectful usage practices

**Use responsibly and at your own risk.**

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with ❤️ for educational purposes
- Uses public APIs and web scraping techniques
- Inspired by the need for restaurant data analysis

---

**Made with ❤️ by [Abhay Shinde](https://github.com/224Abhay)**

If you find this project helpful, please consider giving it a ⭐!
```
  MIT License
  
  Copyright (c) 2025 Abhay Shinde
  
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:
  
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
  
  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.
  ```

