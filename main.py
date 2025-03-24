from zomato_scrapper import zomato

if __name__ == "__main__":

    user_1 = zomato()

    data = user_1.get_restaurants(write_json=True)

    next_data = user_1.get_restaurants(write_json=True)

    restaurant_data = data[1]
    restaurant_menu = user_1.get_menu(restaurant_data, write_json=True)