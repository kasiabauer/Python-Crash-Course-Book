class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
    def greet_user(self):
        print(f"Witaj {self.first_name}!")

my_user1 = User("Karol", "Krawężnik")
my_user2 = User("Jola", "Zdziwiona")
my_user3 = User("Johnny", "Chudy")
my_user1.describe_user()
my_user1.greet_user()
my_user2.describe_user()
my_user2.greet_user()
my_user3.describe_user()
my_user3.greet_user()
