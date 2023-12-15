class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Restauracja {self.restaurant_name} - {self.cuisine_type}")
    def open_restaurant(self):
        print(f"Restauracja {self.restaurant_name} "
              f"jest otwarta od 11:00 - 23:00")

indie_restaurant = Restaurant("My Delhi", "kuchnia indyjska")
polish_restaurant = Restaurant("Wesoła Jola", "kuchnia polska")
italian_restaurant = Restaurant("Aioli Olio", "kuchnia włoska")
indie_restaurant.describe_restaurant()
polish_restaurant.describe_restaurant()
italian_restaurant.describe_restaurant()

