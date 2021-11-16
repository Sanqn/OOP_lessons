# class Cat:
#     name = 'Micki'
#     color = 'black'

# print(Cat.name)
# print(Cat.__dict__)
# print(getattr(Cat, 'color')) #black
# print(getattr(Cat, 'age', 5))
# Cat.age = 10 #append 'age': 10
# setattr(Cat, 'price', 100) #append 'price': 100
# print(Cat.__dict__)
# del Cat.age #'age': 10
# print(Cat.__dict__)
# delattr(Cat, 'price') # del 'price': 100
# print(Cat.__dict__)
#
# a = Cat()
# b = Cat()
# Cat.age = 10
# a.surname = 'joom'
# print(a.surname)

# class Car:
#     model = "BMW"
#     engine = 1.6
#
#     @staticmethod
#     def f():
#         print('Hello world')
#
# Car.f()
# print(Car.engine)
# a = Car()
# print(a.f())

# class Cat:
#     breed = 'Pers'
#     def set_value(self, name, age = 0):
#         self.name = name
#         self.age = age
#
#     def hello_cat(self):
#         print('Hello', self.name)
#
#     def say_how_are_you(self):
#         print('How are you', self.name)
#
# jerry = Cat()
# jerry.name = 'Jarry'
# jerry.age = 5
# jerry.breed = 'Seam'
# print(jerry.__dict__)
# jerry.hello_cat()
# jerry.say_how_are_you()

# class Lion:
#     def roar(self):
#         print('Rrrrrrr!!!')
# sinba = Lion()
# sinba.roar()

# class Counter:
#     def start_from(self, start = 0):
#         self.start = start
#
#     def increment(self):
#         self.start += 1
#
#     def display(self):
#         print(f'Текущее значение счетчика = {self.start}')
#
#     def reset(self):
#         self.start = 0
#
# c1 = Counter()
# c1.start_from()
# c1.increment()
# c1.display() # печатает "Текущее значение счетчика = 1"
# c1.increment()
# c1.display() # печатает "Текущее значение счетчика = 2"
# c1.reset()
# c1.display() # печатает "Текущее значение счетчика = 0"
# from math import sqrt
# class Point:
#
#     def set_coordinates(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_distance(self, another_point):
#         if not isinstance(another_point, Point):
#             return "Передана не точка"
#         return sqrt((self.x - another_point.x)**2 + (self.y - another_point.y)**2)
# p1 = Point()
# p2 = Point()
# p1.set_coordinates(1, 2)
# p2.set_coordinates(4, 6)
# d = p1.get_distance(p2) # вернёт 5.0
# print(d)
# print(p1.get_distance(10)) # Распечатает "Передана не точка"

# class Laptop:
#
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#         self.laptop_name = brand + ' ' + model
#
# hp = Laptop('hp', '15-bw0xx', 57000)
# print(hp.price) # выводит 57000
# print(hp.laptop_name) # выводит "hp 15-bw0xx"

# class SoccerPlayer:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.goals = 0
#         self.assists = 0
#
#     def score(self, goals=1):
#         self.goals += goals
#
#     def make_assist(self, assists=1):
#         self.assists += assists
#
#     def statistics(self):
#         print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')
#
#
# leo = SoccerPlayer('Leo', 'Messi')
# leo.score(700)
# leo.make_assist(500)
# leo.statistics() # выводит "Messi Leo - голы: 700, передачи: 500"
# kokorin = SoccerPlayer('Alex', 'Kokorin')
# kokorin.score()
# kokorin.statistics() # выводит "Kokorin Alex - голы: 1, передачи: 0"

# class Zebra:
#
#     def __init__(self):
#         self.count = 1
#
#     def which_stripe(self):
#         if self.count % 2 != 0:
#             print('Полоска белая')
#             self.count += 1
#         else:
#             print('Полоска черная')
#             self.count += 1
#
# z1 = Zebra()
# z1.which_stripe() # печатает "Полоска белая"
# z1.which_stripe() # печатает "Полоска черная"
# z1.which_stripe() # печатает "Полоска белая"
#
# z2 = Zebra()
# z2.which_stripe() # печатает "Полоска белая"

class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name= last_name
        self.age = age

    def full_name(self):
        return self.last_name + ' ' + self.first_name

    def is_adult(self):
        if self.age >= 18:
            return True
        return False

p1 = Person('Jimi', 'Hendrix', 55)
print(p1.full_name())  # выводит "Hendrix Jimi"
print(p1.is_adult()) # выводит "True"

