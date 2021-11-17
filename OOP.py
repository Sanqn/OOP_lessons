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
# leo.statistics() # output "Messi Leo - голы: 700, передачи: 500"
# kokorin = SoccerPlayer('Alex', 'Kokorin')
# kokorin.score()
# kokorin.statistics() # output "Kokorin Alex - голы: 1, передачи: 0"

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
# z1.which_stripe() # output "Полоска белая"
# z1.which_stripe() # output "Полоска черная"
# z1.which_stripe() # output "Полоска белая"
#
# z2 = Zebra()
# z2.which_stripe() # output "Полоска белая"

# class Person:
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name= last_name
#         self.age = age
#
#     def full_name(self):
#         return self.last_name + ' ' + self.first_name
#
#     def is_adult(self):
#         if self.age >= 18:
#             return True
#         return False
#
# p1 = Person('Jimi', 'Hendrix', 55)
# print(p1.full_name())  # output "Hendrix Jimi"
# print(p1.is_adult()) # output "True"


# class Point:
#
#     def __init__(self, coord_x=0, coord_y=0):
#         self.x = coord_x
#         self.y = coord_y
#
#     def move_to(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y
#
#     def go_home(self):
#         self.x = 0
#         self.y = 0

#================================================================================

# class Point:
#
#     list_points = []
#
#     def __init__(self, coord_x=0, coord_y=0):
#         self.move_to(coord_x, coord_y)
#         Point.list_points.append(self)
#
#
#     def move_to(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y
#
#     def go_home(self):
#         self.move_to(0, 0)
#
#     def print_point(self):
#         print(f'distance is {self.x} {self.y}')
#
#     def calc_distance(self, another_point):
#         if not isinstance(another_point, Point):
#             raise ValueError
#         return ((self.x - another_point.x)**2 + (self.y - another_point.y)**2)*0.5
#
#
# p1 = Point(1, 1)
# print(p1.list_points[0].x)
# p1.move_to(4, 8)
# p1.print_point()
# p2 = Point()
# p2.move_to(2, 3)
# p2.print_point()
# print(p1.calc_distance(p2))


# class Dog:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def description(self):
#         return f'{self.name} is {self.age} years old'
#
#     def speak(self, sound):
#         self.sound = sound
#         return f'{self.name} says {self.sound}'
#
# jack = Dog("Jack", 4)
#
# print(jack.description()) # распечатает 'Jack is 4 years old'
# print(jack.speak("Woof Woof")) # распечатает 'Jack says Woof Woof'
# print(jack.speak("Bow Wow")) # распечатает 'Jack says Bow Wow'


# class Stack:
#
#     def __init__(self):
#         self.values = []
#
#     def push(self, item):
#         self.values.append(item)
#
#     def pop(self):
#         if len(self.values) != 0:
#             self.values.pop()
#         else:
#             print('Empty Stack')
#
#     def peek(self):
#         if len(self.values) != 0:
#             return self.values[-1]
#         print('Empty Stack')
#         return None
#
#     def is_empty(self):
#         return len(self.values) == 0
#
#     def size(self):
#         return len(self.values)
#
#
# s = Stack()
# s.peek()  # распечатает 'Empty Stack'
# print(s.is_empty())  # распечатает True
# s.push('cat')  # кладем элемент 'cat' на вершину стека
# s.push('dog')  # кладем элемент 'dog' на вершину стека
# print(s.peek())  # распечатает 'dog'
# s.push(True)  # кладем элемент True на вершину стека
# print(s.size())  # распечатает 3
# print(s.is_empty())  # распечатает False
# s.push(777)  # кладем элемент 777 на вершину стека
# print(s.pop())  # удаляем элемент 777 с вершины стека и печатаем его
# print(s.pop())  # удаляем элемент True с
# # вершины стека и печатаем его
# print(s.size())  # распечатает 2

# class Cat:
#
#     __shared_atr = {
#         'breed': 'siam',
#         'color': 'black'
#     } #__protect atr
#
#     def __init__(self):
#         self.__dict__ = Cat.__shared_atr
#
# c1 = Cat()
# c2 = Cat()
# c2.age = 5
# print(c1.__dict__)
# print(c2.__dict__)

# class BankAccount:
#
#     def __init__(self, name, balance, passport):
#         self.__name = name
#         self.__balance = balance
#         self.__passport = passport
#
#     # def print_data(self):
#     #     print(self.name, self.balance, self.passport)
#
#     # def print_protected_data(self):
#     #     print(self._name, self._balance, self._passport)
#
#     def print_private_data(self):
#         print(self.__name, self.__balance, self.__passport) # encapsulation
#
# account1 = BankAccount('Tom', 10000, 124519873)
# account1.print_private_data()
# # account1.print_protected_data()
# # account1.print_data()
# print(account1.__name)# AttributeError: 'BankAccount' object has no attribute '__name'
# print(account1.__balance)# AttributeError: 'BankAccount' object has no attribute '__balance'
# print(account1.__passport)# AttributeError: 'BankAccount' object has no attribute '__passport'


class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_data(self): # but you can print private mathod by open method print_data
        self.__print_private_data()

    def __print_private_data(self): # private method
        print(self.__name, self.__balance, self.__passport) # encapsulation

account1 = BankAccount('Tom', 10000, 124519873)
account1.print_data()
print(dir(account1)) #['_BankAccount__balance', '_BankAccount__name', '_BankAccount__passport', '_BankAccount__print_private_data'....]
print(account1._BankAccount__name)
print(account1._BankAccount__passport)
print(account1._BankAccount__balance)

