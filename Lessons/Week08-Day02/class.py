class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, info):
        self.name = restaurant_name
        self.type = cuisine_type
        self.info = info
    
    def func(self):
        print(f'Restaurant: {self.name}\nCuisine Type: {self.type}')

    def open_restaurant(self):
        self.info = "Restaurant Opened"
        print(self.info)

describe_restaurant = Restaurant('Qaqarin', "Milli", " ")
describe_restaurant.func()
describe_restaurant.open_restaurant()




# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = 20
#     def describe_user(self):
#         print(f'Ad:{self.first_name}\nSoyad:{self.last_name}\nAge:{self.age}')
#     def greet_user(self):
#         print(f'{self.first_name} {self.last_name} {self.age} years old.')

# user1 = User('Ahmed', 'Hajiyev')
# print(user1.first_name, user1.last_name, user1.age)
# user1.describe_user()
# user1.greet_user()

# user2 = User('Ilyas', 'Mustafazada')
# print(user1.first_name, user1.last_name, user1.age)
# user2.age = 40
# user2.describe_user()
# user2.greet_user()



