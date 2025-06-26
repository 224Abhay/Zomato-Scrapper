#!/usr/bin/env python3
"""
Advanced usage example for Zomato Scraper

This script demonstrates advanced features including:
- Multiple page scraping
- Batch menu extraction
- Data analysis and filtering
- Error handling and retries
"""

import sys
import os
import json
import time
from pathlib import Path
from typing import List, Dict, Any

# Add parent directory to path to import the scraper
sys.path.append(str(Path(__file__).parent.parent))

from zomato_scrapper import zomato


def analyze_restaurants(restaurants: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Analyze restaurant data and return statistics."""
    
    stats = {
        'total_restaurants': len(restaurants),
        'avg_rating': 0,
        'cuisine_counts': {},
        'delivery_time_ranges': {},
        'highly_rated': [],
        'quick_delivery': []
    }
    
    total_rating = 0
    rating_count = 0
    
    for restaurant in restaurants:
        info = restaurant.get('info', {})
        
        # Rating analysis
        rating = info.get('rating')
        if rating:
            total_rating += rating
            rating_count += 1
            if rating >= 4.0:
                stats['highly_rated'].append({
                    'name': info.get('name', 'Unknown'),
                    'rating': rating
                })
        
        # Cuisine analysis
        cuisines = info.get('cuisines', [])
        for cuisine in cuisines:
            stats['cuisine_counts'][cuisine] = stats['cuisine_counts'].get(cuisine, 0) + 1
        
        # Delivery time analysis
        delivery_time = info.get('deliveryTime', '')
        if delivery_time:
            stats['delivery_time_ranges'][delivery_time] = stats['delivery_time_ranges'].get(delivery_time, 0) + 1
            if '15' in delivery_time or '20' in delivery_time:
                stats['quick_delivery'].append({
                    'name': info.get('name', 'Unknown'),
                    'delivery_time': delivery_time
                })
    
    if rating_count > 0:
        stats['avg_rating'] = round(total_rating / rating_count, 2)
    
    return stats


def extract_menus_batch(scraper: zomato, restaurants: List[Dict[str, Any]], max_restaurants: int = 5) -> List[Dict[str, Any]]:
    """Extract menus for multiple restaurants with error handling."""
    
    menus = []
    successful = 0
    failed = 0
    
    print(f"\n🍽️  Extracting menus for up to {max_restaurants} restaurants...")
    
    for i, restaurant in enumerate(restaurants[:max_restaurants]):
        try:
            restaurant_name = restaurant.get('info', {}).get('name', f'Restaurant_{i}')
            print(f"  {i+1}/{max_restaurants}: Extracting menu for {restaurant_name}...")
            
            menu_data = scraper.get_menu(restaurant, write_json=True)
            menus.append({
                'restaurant_name': restaurant_name,
                'menu_data': menu_data,
                'success': True
            })
            successful += 1
            
            # Add a small delay to be respectful to the server
            time.sleep(1)
            
        except Exception as e:
            print(f"  ❌ Failed to extract menu for {restaurant_name}: {str(e)}")
            menus.append({
                'restaurant_name': restaurant_name,
                'error': str(e),
                'success': False
            })
            failed += 1
    
    print(f"✅ Menu extraction completed: {successful} successful, {failed} failed")
    return menus


def main():
    """Main function demonstrating advanced scraper usage."""
    
    print("🍕 Zomato Scraper - Advanced Usage Example")
    print("=" * 55)
    
    try:
        # Initialize the scraper
        print("Initializing scraper...")
        scraper = zomato()
        print("✅ Scraper initialized successfully!")
        
        # Get multiple pages of restaurants
        all_restaurants = []
        max_pages = 3
        
        print(f"\n📋 Fetching restaurants from {max_pages} pages...")
        
        for page in range(max_pages):
            print(f"  Page {page + 1}/{max_pages}...")
            restaurants = scraper.get_restaurants(write_json=True)
            all_restaurants.extend(restaurants)
            print(f"    Found {len(restaurants)} restaurants on this page")
            
            # Add delay between pages
            if page < max_pages - 1:
                time.sleep(2)
        
        print(f"✅ Total restaurants collected: {len(all_restaurants)}")
        
        # Analyze restaurant data
        print("\n📊 Analyzing restaurant data...")
        stats = analyze_restaurants(all_restaurants)
        
        print(f"📈 Analysis Results:")
        print(f"  Total Restaurants: {stats['total_restaurants']}")
        print(f"  Average Rating: {stats['avg_rating']}")
        print(f"  Highly Rated (4.0+): {len(stats['highly_rated'])}")
        print(f"  Quick Delivery: {len(stats['quick_delivery'])}")
        
        # Show top cuisines
        top_cuisines = sorted(stats['cuisine_counts'].items(), key=lambda x: x[1], reverse=True)[:5]
        print(f"  Top Cuisines:")
        for cuisine, count in top_cuisines:
            print(f"    {cuisine}: {count} restaurants")
        
        # Show highly rated restaurants
        print(f"\n🏆 Highly Rated Restaurants:")
        for restaurant in stats['highly_rated'][:5]:
            print(f"  {restaurant['name']} - Rating: {restaurant['rating']}")
        
        # Extract menus for a subset of restaurants
        menus = extract_menus_batch(scraper, all_restaurants, max_restaurants=3)
        
        # Save analysis results
        analysis_file = "restaurant_analysis.json"
        with open(analysis_file, 'w', encoding='utf-8') as f:
            json.dump({
                'statistics': stats,
                'menu_extraction_results': menus
            }, f, indent=4, ensure_ascii=False)
        
        print(f"\n📁 Analysis saved to: {analysis_file}")
        print("\n🎉 Advanced usage example completed successfully!")
        
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")
        print("Please check your internet connection and try again.")


if __name__ == "__main__":
    main() 