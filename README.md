# Zomato Scraper

A Python-based scraper that leverages Zomato’s web routes to fetch restaurants and menus based on your current location. The project uses IP-based geolocation to determine your area, retrieves restaurant listings, and extracts detailed menu information from the Zomato website.

Find reading boring? check the data to see if this scrapper fits your needs.
I have put an example of the following:
1. Restaurant Data
2. Restaurant Menu

If you need anything more / help in any way feel free to put up an issue.

This is an extremely fast scrapper, can scrape in realtime if needed.
Only made this scrapper to showcase my skills and nothing more, Use responsibly.
Read the Disclamer given at last. :)

## Features

- **Dynamic Location Detection:** Automatically fetches the user’s current latitude and longitude based on their public IP.
- **Restaurant Listings:** Scrapes Zomato to get a list of restaurants available in your area.
- **Menu Extraction:** Retrieves detailed menu information for a selected restaurant.
- **JSON Output:** Saves restaurant data and menus as JSON files for further processing or analysis.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Contributing](#contributing)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/224Abhay/zomato-scraper.git
   cd zomato-scraper

2. **Create and activate a virtual environment (optional but recommended):**
    
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # For Unix/macOS
    venv\Scripts\activate      # For Windows

3. **Install the required dependencies:**
    
    ```bash
    pip install -r requirements.txt

# Configuration:
User-Agent and Headers:
The scraper uses custom headers (including a User-Agent) to mimic a browser. Adjust these headers in the zomato class if you encounter issues or need to simulate a different browser.

# IP Geolocation:
The get_location() function calls ipify and ipinfo.io to determine your location. If needed, you can replace these endpoints with your preferred geolocation services.

# Contributing:
Contributions are welcome! If you have any ideas, bug fixes, or improvements, feel free to open an issue or submit a pull request.

1. **Fork the repository.**

2. **Create your feature branch: git checkout -b feature/YourFeature**

3. **Commit your changes: git commit -m 'Add new feature'**

4. **Push to the branch: git push origin feature/YourFeature**

5. **Open a pull request.**

# Disclaimer: 
This project is intended for educational purposes only and is not affiliated with or endorsed by Zomato. Users are responsible for ensuring that their use of this tool complies with all applicable laws and Zomato's terms of service.

## 📜 License
This project is open-source under the **MIT License**.
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

