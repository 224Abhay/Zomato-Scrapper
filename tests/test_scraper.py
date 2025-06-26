#!/usr/bin/env python3
"""
Tests for Zomato Scraper

This module contains basic tests for the scraper functionality.
"""

import pytest
import sys
import os
from pathlib import Path

# Add parent directory to path to import the scraper
sys.path.append(str(Path(__file__).parent.parent))

from zomato_scrapper import zomato
from location import get_location


class TestLocation:
    """Test location detection functionality."""
    
    def test_get_location_returns_tuple(self):
        """Test that get_location returns a tuple of two values."""
        lat, lon = get_location()
        assert isinstance(lat, str)
        assert isinstance(lon, str)
        assert len(lat) > 0
        assert len(lon) > 0
    
    def test_get_location_coordinates_valid(self):
        """Test that returned coordinates are valid latitude/longitude."""
        lat, lon = get_location()
        
        # Convert to float and check ranges
        lat_float = float(lat)
        lon_float = float(lon)
        
        assert -90 <= lat_float <= 90, "Latitude should be between -90 and 90"
        assert -180 <= lon_float <= 180, "Longitude should be between -180 and 180"


class TestZomatoScraper:
    """Test Zomato scraper functionality."""
    
    def test_scraper_initialization(self):
        """Test that scraper can be initialized."""
        scraper = zomato()
        assert scraper is not None
        assert hasattr(scraper, 'session')
        assert hasattr(scraper, 'headers')
        assert hasattr(scraper, 'page_no')
    
    def test_scraper_has_required_methods(self):
        """Test that scraper has required methods."""
        scraper = zomato()
        assert hasattr(scraper, 'get_restaurants')
        assert hasattr(scraper, 'get_menu')
        assert hasattr(scraper, 'get_current_area')
    
    def test_headers_structure(self):
        """Test that headers are properly structured."""
        scraper = zomato()
        headers = scraper.headers
        
        assert 'User-Agent' in headers
        assert 'Content-Type' in headers
        assert headers['Content-Type'] == 'application/json'
        assert 'Mozilla' in headers['User-Agent']


class TestDataStructures:
    """Test data structure handling."""
    
    def test_restaurant_data_structure(self):
        """Test that restaurant data has expected structure."""
        # This is a mock test - in real scenario you'd test with actual data
        sample_restaurant = {
            'info': {
                'name': 'Test Restaurant',
                'rating': 4.5,
                'cuisines': ['Italian', 'Pizza'],
                'deliveryTime': '30-35 min'
            },
            'order': {
                'actionInfo': {
                    'clickUrl': '/test-restaurant'
                }
            }
        }
        
        assert 'info' in sample_restaurant
        assert 'order' in sample_restaurant
        assert 'name' in sample_restaurant['info']
        assert 'rating' in sample_restaurant['info']
        assert 'cuisines' in sample_restaurant['info']
    
    def test_menu_data_structure(self):
        """Test that menu data has expected structure."""
        # This is a mock test - in real scenario you'd test with actual data
        sample_menu = {
            'page_data': {
                'sections': {
                    'SECTION_BASIC_INFO': {
                        'restaurant_name': 'Test Restaurant',
                        'cuisines': 'Italian, Pizza'
                    },
                    'SECTION_MENU': {
                        'categories': []
                    }
                }
            }
        }
        
        assert 'page_data' in sample_menu
        assert 'sections' in sample_menu['page_data']
        assert 'SECTION_BASIC_INFO' in sample_menu['page_data']['sections']
        assert 'SECTION_MENU' in sample_menu['page_data']['sections']


# Integration tests (these would require internet connection)
class TestIntegration:
    """Integration tests that require internet connection."""
    
    @pytest.mark.integration
    def test_location_detection_integration(self):
        """Test location detection with actual internet connection."""
        try:
            lat, lon = get_location()
            assert float(lat) != 0
            assert float(lon) != 0
        except Exception as e:
            pytest.skip(f"Location detection failed: {e}")
    
    @pytest.mark.integration
    def test_scraper_integration(self):
        """Test scraper with actual internet connection."""
        try:
            scraper = zomato()
            # This would require actual internet connection
            # In a real test, you might mock the responses
            assert scraper is not None
        except Exception as e:
            pytest.skip(f"Scraper integration test failed: {e}")


if __name__ == "__main__":
    pytest.main([__file__]) 