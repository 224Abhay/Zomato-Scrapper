# Zomato Scraper

A Python-based scraper that leverages Zomato’s web routes to fetch restaurants and menus based on your current location. The project uses IP-based geolocation to determine your area, retrieves restaurant listings, and extracts detailed menu information from the Zomato website.

## Features

- **Dynamic Location Detection:** Automatically fetches the user’s current latitude and longitude based on their public IP.
- **Restaurant Listings:** Scrapes Zomato to get a list of restaurants available in your area.
- **Menu Extraction:** Retrieves detailed menu information for a selected restaurant.
- **JSON Output:** Saves restaurant data and menus as JSON files for further processing or analysis.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/zomato-scraper.git
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

