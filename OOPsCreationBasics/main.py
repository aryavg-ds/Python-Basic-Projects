# class Car():
#     pass
#
# my_car = Car()
# my_car.id = "001"
# my_car.name = "polo"
# print(my_car.name)

class Cars:
    def __init__(self, cid, name, colour):
        self.cid = cid
        self.name = name
        self.colour = colour
        self.initial_followers_count = 0        #default arg

car_1 = Cars("001", "polo", "blue") #commented 3 statements converted to one using init
car_2 = Cars("002", "brezza", "red")

print(car_1.cid, car_1.name, car_1.colour)
print(car_1.initial_followers_count) #printing the def keyword arg passed in class def, always 0

class User:
    def __init__(self, id, u_name):
        self.id = id
        self.u_name = u_name
        self.followers_count = 0        #keyword arg, no need to give as para in class def.
        self.following_count = 0        # "

    def follow(self, user):
        user.followers_count += 1
        self.following_count += 1

user_1 = User("1", "Anoop")
user_2 = User("2", "Arya")
user_3 = User("3", "Samanvitha")
user_1.follow(user_2) #1 is following 2
print(user_1.followers_count, user_1.following_count)
print(user_2.followers_count, user_2.following_count)