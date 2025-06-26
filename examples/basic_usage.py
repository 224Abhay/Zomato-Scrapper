#!/usr/bin/env python3
"""
Basic usage example for Zomato Scraper

This script demonstrates the basic functionality of the Zomato scraper,
including fetching restaurants and extracting menu data.
"""

import sys
import os
import json
from pathlib import Path

# Add parent directory to path to import the scraper
sys.path.append(str(Path(__file__).parent.parent))

from zomato_scrapper import zomato


def main():
    """Main function demonstrating basic scraper usage."""
    
    print("🍕 Zomato Scraper - Basic Usage Example")
    print("=" * 50)
    
    try:
        # Initialize the scraper
        print("Initializing scraper...")
        scraper = zomato()
        print("✅ Scraper initialized successfully!")
        
        # Get restaurant listings
        print("\n📋 Fetching restaurant listings...")
        restaurants = scraper.get_restaurants(write_json=True)
        print(f"✅ Found {len(restaurants)} restaurants")
        
        # Display some restaurant information
        print("\n🏪 Sample Restaurant Data:")
        for i, restaurant in enumerate(restaurants[:3]):  # Show first 3 restaurants
            info = restaurant.get('info', {})
            print(f"  {i+1}. {info.get('name', 'N/A')}")
            print(f"     Rating: {info.get('rating', 'N/A')}")
            print(f"     Cuisines: {', '.join(info.get('cuisines', []))}")
            print(f"     Delivery Time: {info.get('deliveryTime', 'N/A')}")
            print()
        
        # Get menu for the first restaurant
        if restaurants:
            print("🍽️  Extracting menu for the first restaurant...")
            first_restaurant = restaurants[0]
            restaurant_name = first_restaurant.get('info', {}).get('name', 'Unknown Restaurant')
            
            menu_data = scraper.get_menu(first_restaurant, write_json=True)
            print(f"✅ Menu extracted for: {restaurant_name}")
            
            # Display menu structure
            if 'page_data' in menu_data:
                sections = menu_data['page_data'].get('sections', {})
                print(f"\n📋 Menu Sections Found:")
                for section_name in sections.keys():
                    print(f"  - {section_name}")
        
        print("\n🎉 Basic usage example completed successfully!")
        print("\n📁 Generated files:")
        print("  - restaurant_data/restaurants_page1.json")
        print(f"  - menus/{restaurant_name}_menu.json")
        
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")
        print("Please check your internet connection and try again.")


if __name__ == "__main__":
    main() 