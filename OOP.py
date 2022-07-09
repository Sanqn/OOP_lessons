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

# ================================================================================

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


# class BankAccount:
#
#     def __init__(self, name, balance, passport):
#         self.__name = name
#         self.__balance = balance
#         self.__passport = passport
#
#     def print_data(self): # but you can print private mathod by open method print_data
#         self.__print_private_data()
#
#     def __print_private_data(self): # private method
#         print(self.__name, self.__balance, self.__passport) # encapsulation
#
# account1 = BankAccount('Tom', 10000, 124519873)
# account1.print_data()
# print(dir(account1)) #['_BankAccount__balance', '_BankAccount__name', '_BankAccount__passport', '_BankAccount__print_private_data'....]
# print(account1._BankAccount__name)
# print(account1._BankAccount__passport)
# print(account1._BankAccount__balance)

# Property getattr and setter method+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# class BankAccount:
#
#     def __init__(self, name, balance):
#         self.__name = name
#         self.__balance = balance
#
#
#     def get_balance(self):
#         return self.__balance
#
#
#     def set_balance(self, value):
#         if not isinstance(value, (int, float)):
#             raise ValueError('Balance must be number')
#         self.__balance = value
#
#     def del_balance(self):
#         del self.__balance
#
#     balance = property(fget=get_balance, fset=set_balance, fdel=del_balance)
#
# # a1 = BankAccount('Nick', 1000)
# # print(a1.get_balance())
# # a1.set_balance(1500)
# # print(a1.get_balance())
# # a1.set_balance('hello')
# # print(a1.get_balance())
#
# a1 = BankAccount('Nick', 1000)
# print(a1.balance)
# a1.balance = 500
# print(a1.balance)
# del a1.balance
# a1.balance = 777
# print(a1.balance)

# class UserMail:
#
#     def __init__(self, login, email):
#         self.login = login
#         self.__email = email
#
#     def get_email(self):
#         return self.__email
#
#     def set_email(self, new_mail):
#         if isinstance(new_mail, str) \
#                 and new_mail.count('@') == 1 \
#                 and '.' in new_mail[new_mail.find('@'):]:
#             self.__email = new_mail
#         else:
#             print('Ошибочная почта')
#
#     email = property(fget=get_email, fset=set_email)
#
# k = UserMail('belosnezhka', 'prince@wait.you')
# print(k.email)  # prince@wait.you
# k.email = [1, 2, 3] # Ошибочная почта
# k.email = 'prince@still@.wait'  # Ошибочная почта
# k.email = 'prince@still.wait'
# print(k.email)  # prince@still.wait

# import re
# class UserMail:
#
#     def __init__(self, login, email):
#         self.login = login
#         self.__email = email
#
#     def get_email(self):
#         return self.__email
#
#     def set_email(self, new_mail):
#         if isinstance(new_mail, str) and re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$', new_mail):
#             self.__email = new_mail
#         else:
#             print('Ошибочная почта')
#
#     email = property(fget=get_email, fset=set_email)
#
# k = UserMail('belosnezhka', 'prince@wait.you')
# print(k.email)  # prince@wait.you
# k.email = [1, 2, 3] # Ошибочная почта
# k.email = 'prince@still@.wait'  # Ошибочная почта
# k.email = 'prince@still.wait'
# print(k.email)  # prince@still.wait

# class BankAccount:
#
#     def __init__(self, name, balance):
#         self.__name = name
#         self.__balance = balance
#
#     @property
#     def my_balance(self):
#         return self.__balance
#
#     @my_balance.setter
#     def my_balance(self, value):
#         if not isinstance(value, (int, float)):
#             raise ValueError('Balance must be number')
#         self.__balance = value
#
#     @my_balance.deleter
#     def my_balance(self):
#         del self.__balance
#
#
# a1 = BankAccount('Nick', 1000)
# print(a1.my_balance)
# a1.my_balance = 500
# print(a1.my_balance)
# a1.my_balance = 777
# print(a1.my_balance)
# del a1.my_balance
# print(a1.__dict__)

# Magic method __str__ and __repr__ +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# class Lion:
#
#     def __init__(self, name):
#         self.name = name
#
#     # def __repr__(self):
#     #     return f'The object Lion - {self.name}'
#
#     def __str__(self):
#         return f'The Lion - {self.name}'
#     @property
#     def ime(self):
#         return self.name
#
# l = Lion(10)
# l # The object Lion - Simba output in console
# print(l)# The Lion - Simba
# print(l.ime)


# class Money:
#
#     def __init__(self, dollars, cents):
#         self.total_cents = dollars * 100 + cents
#
#     @property
#     def dollars(self):
#         return self.total_cents // 100
#
#     @dollars.setter
#     def dollars(self, value):
#         if isinstance(value, int) and value >=0:
#             self.total_cents = self.total_cents % 100 + value * 100
#         else:
#             print('Error dollars')
#
#     @property
#     def cents(self):
#         return self.total_cents % 100
#
#     @cents.setter
#     def cents(self, value_cent):
#         if isinstance(value_cent, int) and 0 <= value_cent < 100:
#             self.total_cents = self.total_cents // 100 * 100 + value_cent
#         else:
#             print('Error cents')
#
#     def __str__(self):
#         return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'
#
# Bill = Money(1512, 99)
# print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
# print(Bill.dollars, Bill.cents)  # 101 99
# Bill.dollars = 666
# print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
# Bill.cents = 12
# print(Bill)  # Ваше состояние составляет 666 долларов 12 центов

# class Square:
#
#     def __init__(self, side):
#         self.__side = side
#         self.__area = None
#
#     @property
#     def side(self):
#         return self.__side
#
#     @side.setter
#     def side(self, value):
#         self.__side = value
#         self.__area = None
#
#     @property
#     def area(self):
#         if self.__area is None:
#             print('Calculate')
#             self.__area = self.__side**2
#         return self.__area
#
# a1 = Square(5)
# print(a1.side)
# a1.side = 5
# print(a1.area)
# a1.side = 5
# print(a1.area)

# class Perimetr:
#
#     def __init__(self, side_1, side_2):
#         self.__side_1 = side_1
#         self.__side_2 = side_2
#         self.__perim = None
#
#     @property
#     def side(self):
#         return self.__side_1, self.__side_2
#
#     @side.setter
#     def side(self, arg):
#         self.__side_1, self.__side_2 = arg
#         self.__perim = None
#
#     @property
#     def perim(self):
#         if self.__perim is None:
#             print('tcnm')
#             self.__perim = self.__side_1 * 2 + self.__side_2 * 2
#         return self.__perim
#
# p1 = Perimetr(3, 4)
# print(p1.perim)
# p2 = Perimetr(5, 6)
# print(p2.perim)
# p2.side = 7, 8
# print(p2.perim)

# @staticmethod and @staticmethod++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# class Example:
#
#     def hello():
#         print('Hello') # only Example.hello()
#
#     def instance_hello(self):
#         print(f'Hello instance {self}') # only d = Example() => d.instance_hello
#
#     @staticmethod
#     def static_print():
#         print('Hello static')
#
#     @classmethod
#     def class_hello(self):
#         print(f'Hello class {self}')
#
# Example.static_print()
# a = Example()
# a.static_print()
# Example.class_hello()
# b = Example()
# b.class_hello()

# class Robot:
#     population = 0
#
#     def __init__(self, name):
#         self.name = name
#         print(f'Робот {self.name} был создан')
#         Robot.population += 1
#
#     def destroy(self):
#         print(f'Робот {self.name} был уничтожен')
#         del self.name
#         Robot.population -= 1
#
#     def say_hello(self):
#         print(f'Робот {self.name} приветствует тебя, особь человеческого рода')
#
#     @classmethod
#     def how_many(self):
#         print(f'{self.population}, вот сколько нас еще осталось')
#
# r2 = Robot("R2-D2") # печатает "Робот R2-D2 был создан"
# r2.say_hello() # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
# Robot.how_many() # печатает "1, вот сколько нас еще осталось"
# r2.destroy() # печатает "Робот R2-D2 был уничтожен"

# class DepartamentIT:
#     PYTHON_DEV = 3
#     GO_DEV = 3
#     REACT_DEV = 2
#
#     @classmethod
#     def info_class(cls):
#         print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV)
#
#     @staticmethod
#     def info_stat():
#         print(DepartamentIT.PYTHON_DEV, DepartamentIT.GO_DEV, DepartamentIT.REACT_DEV)
#
#     @property
#     def info_prop(self):
#         print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)
#
#     def info(self):
#         print(DepartamentIT.PYTHON_DEV, DepartamentIT.GO_DEV, DepartamentIT.REACT_DEV)
#
#     def make_backend(self):
#         print('Python and Go')
#
#     def make_fronend(self):
#         print('React')
#
#     def hiring_dev_python(self):
#         DepartamentIT.PYTHON_DEV += 1
#
# itl = DepartamentIT()
# itl.info_prop
# itl.hiring_dev_python()
# print(itl.PYTHON_DEV)

# class User:
#
#     def __init__(self, login, password):
#         self.login = login
#         self.password = password
#         self.__secret_cod = 'You are good chel'
#
#     @property
#     def get_secret(self):
#         s = input('input your pass')
#         if s == self.password:
#             return self.__secret_cod
#         else:
#             raise ValueError('you input not that password')
#
#     @property
#     def password(self):
#         return self.__password
#
#     @staticmethod
#     def check_pass(password):
#         for i in '0123456789':
#             if i in password:
#                 return True
#         return False
#
#     @staticmethod
#     def simple_pass(password):
#         file = open('simple_pas.txt', encoding='utf-8').read()
#         for name in file:
#             if not name in password:
#                 return True
#         return False
#
#     @password.setter
#     def password(self, value):
#         if not isinstance(value, str):
#             raise TypeError('password must be string')
#         if len(value) < 4:
#             raise ValueError('password must be more then 4 letters')
#         if len(value) > 12:
#             raise ValueError('password must be less then 12 letters')
#         if not User.check_pass(value):
#             raise ValueError('password must include digits')
#         if not User.simple_pass(value):
#             raise ValueError('пароль простой')
#         self.__password = value
#
# s1 = User('Nick', 'Chegg123')
# # s1.password = 'ter457'
# print(s1.password)
#

# import string
#
#
# class Registration:
#
#     def __init__(self, login, password):
#         self.login = login
#         self.password = password
#
#     @property
#     def login(self):
#         return self.__login
#
#     @login.setter
#     def login(self, value):
#         if not '@' in value:
#             raise ValueError("Login must include at least one ' @ '")
#         if not '.' in value:
#             raise ValueError("Login must include at least one ' . '")
#         self.__login = value
#
#     @property
#     def password(self):
#         return self.__password
#
#     @staticmethod
#     def is_include_digit(password):
#         for i in '0123456789':
#             if i in password:
#                 return True
#         return False
#
#     @staticmethod
#     def is_include_all_register(password):
#         count = 0
#         for i in password:
#             if i.isupper():
#                 count += 1
#         if count >= 2:
#             return True
#         return False
#
#     @staticmethod
#     def is_include_only_latin(password):
#         for i in string.ascii_letters:
#             if i in password:
#                 return True
#         return False
#
#     @staticmethod
#     def check_password_dictionary(password):
#         easy_passwords = ['123456', 'password', '123456789', '12345', '12345678', 'qwerty', '1234567', '111111',
#                           '1234567890', '123123', 'abc123', '1234', 'password1', 'iloveyou', '1q2w3e4r', '000000',
#                           'qwerty123', 'zaq12wsx', 'dragon', 'sunshine', 'princess', 'letmei', '654321', 'monkey',
#                           '27653', '1qaz2wsx', '123321', 'qwertyuiop', 'superman', 'asdfghjkl']
#         for i in easy_passwords:
#             if password != i:
#                 return True
#         return False
#
#     @password.setter
#     def password(self, value):
#         if not isinstance(value, str):
#             raise TypeError("Пароль должен быть строкой")
#         if len(value) < 5:
#             raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
#         if len(value) > 11:
#             raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
#         if not Registration.is_include_digit(value):
#             raise ValueError('Пароль должен содержать хотя бы одну цифру')
#         if not Registration.is_include_all_register(value):
#             raise ValueError('Пароль должен содержать хотя бы 2 заглавные буквы')
#         if not Registration.is_include_only_latin(value):
#             raise ValueError('Пароль должен содержать только латинский алфавит')
#         if not Registration.check_password_dictionary(value):
#             raise ValueError('Ваш пароль содержится в списке самых легких')
#         self.__password = value
#
# s = Registration("translate@gmail.com", "as1SNdf")
# s.login = 'com'
# print(s.login)

# class Person:
#
#     def __init__(self, name, surname, gender='male'):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         if 'female' != gender != 'male':
#             self.gender = 'male'
#             print(f'Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
#
#     def __str__(self):
#         if self.gender == 'male':
#             return f'Гражданин {self.surname} {self.name}'
#         elif self.gender == 'female':
#             return f'Гражданка {self.surname} {self.name}'
#         else:
#             self.gender = 'male'
# p3 = Person('Оби-Ван', 'Кеноби', True)# печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
# print(p3) # печатает "Гражданин Кеноби Оби-Ван"

# class Vector:
#
#     def __init__(self, *args):
#         self.values = []
#         for i in args:
#             if isinstance(i, int):
#                     self.values.append(i)
#
#     def __str__(self):
#         if len(self.values):
#             return f"Вектор{tuple(sorted(self.values))}"
#         else:
#             return f'Пустой вектор'
#
#
# v1 = Vector(4,1,3,5,2,8,2,6,8,4,2)
# print(v1)  # печатает "Вектор(1, 2, 3)"
# v2 = Vector()
# print(v2)  # печатает "Пустой вектор"


##__len__ and __abs__++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# class Person:
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __len__(self):
#         return len(self.name + self.surname)
#
#
# # p1 = Person('aaaa', 'vvvev')
# # print(len(p1))
#
# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return self.x, self.y
#
# class Otrezok:
#
#     def __init__(self, point, point2):
#         self.point = point
#         self.point2 = point2
#
#     def __len__(self):
#         return abs(self.point2 - self.point)
#         #return abs(self) #or abs(self.point2 - self.point)
#
#     def __abs__(self):
#         dx = abs(self.point2.x - self.point.x)
#         dy = abs(self.point2.y - self.point.y)
#         return abs(dy + dx)
#
# x = Point(0, 0)
# y = Point(4, 6)
# xy = Otrezok(x, y)
# print(abs(xy))

# __add__(+), __mul__(*), __sub__(-) и __truediv__(/)++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# class BankAcount:
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def __add__(self, other):
#         if isinstance(other, (int, float)):
#             return self.balance + other
#         if isinstance(other, BankAcount):
#             return self.balance + other.balance
#         raise NotImplemented
#
#     def __mul__(self, other):
#         if isinstance(other, (int, float)):
#             return self.balance * other
#         if isinstance(other, BankAcount):
#             return self.balance * other.balance
#         if isinstance(other, str):
#             return self.name + other
#         raise NotImplemented
#
#     def __radd__(self, other):
#         print('radd')
#         return self + other
#
# t1 = BankAcount('Tom', 530)
# print(t1+500) #1030
# print(500 + t1)
# print(t1 + 30)
# print(t1*50)
# print(t1*'Nick')

# class BankAcount:
#
#     def __init__(self, name, balance):
#         print('New object')
#         self.name = name
#         self.balance = balance
#
#     def __repr__(self):
#         return f'Customer name is {self.name}, balance: {self.balance}'
#
#     def __add__(self, other):
#         print('add __call__')
#         if isinstance(other, (int, float)):
#             return BankAcount(self.name, self.balance + other)
#         if isinstance(other, BankAcount):
#             return self.balance + other.balance
#         raise NotImplemented
#
# t1 = BankAcount('John', 1000)
# print(t1 + 11)
# d = t1 + 20
# print(d)
# print(id(t1), id(d))
# print(t1 + d)
#
# class Vector:
#
#     def __init__(self, *args):
#         self.values = sorted([i for i in args if isinstance(i, int)])
#
#     def __str__(self):
#         if self.values:
#             return f"Вектор{tuple(self.values)}"
#         else:
#             return f"Пустой вектор"
#
#     def __add__(self, other):
#         if isinstance(other, int):
#             return Vector(*(i + other for i in self.values))
#
#         if isinstance(other, Vector) and len(self.values) == len(other.values):
#             return Vector(*(map(sum, zip(self.values, other.values))))
#
#         if isinstance(other, Vector) and len(self.values) != len(other.values):
#             print("Сложение векторов разной длины недопустимо")
#
#         else:
#             print(f"Вектор нельзя сложить с {other}")
#
#     def __mul__(self, other):
#         if isinstance(other, int):
#             return Vector(*(i * other for i in self.values))
#
#         if isinstance(other, Vector) and len(self.values) == len(other.values):
#             return Vector(*(x*y for x,y in zip(self.values, other.values)))
#
#         if isinstance(other, Vector) and len(self.values) != len(other.values):
#             print("Умножение векторов разной длины недопустимо")
#
#         else:
#             print(f"Вектор нельзя умножать с {other}")
#
#
#
# v1 = Vector(1, 2, 3)
# print(v1)  # печатает "Вектор(1, 2, 3)"
# v2 = Vector(3, 4, 5)
# print(v2)  # печатает "Вектор(3, 4, 5)"
# v3 = v1 + v2
# print(v3)  # печатает "Вектор(4, 6, 8)"
# v4 = v3 + [1, 2, 8]
# print(v4)  # печатает "Вектор(9, 11, 13)"


# Magic method++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# __eq__ ==  '=='
# __ne__ ==  '!='
# __lt__ ==  '<'
# __le__ ==  '<='
# __gt__ ==  '>'
# __ge__ ==  '>='

# class Rectangle:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     @property
#     def area(self):
#         return self.a * self.b
#
#     def __eq__(self, other):
#         if isinstance(other, Rectangle):
#             return self.a == other.a and self.b == other.b
#
#     def __lt__(self, other):
#         if isinstance(other, Rectangle):
#             return self.area < other.area
#         elif isinstance(other, (int, float)):
#             return self.area < other
#
#     def __le__(self, other):
#         return self==other or self<other
#
# q1 = Rectangle(1, 2)
# q2 = Rectangle(1, 2)
# print(q1==q2)
# print(q1.area)
# print(q1<=q2)
# print(q1<15)

# class ChessPlayer:
#
#     def __init__(self, name, surname, rating):
#         self.name = name
#         self.surname = surname
#         self.rating = rating
#
#     def __eq__(self, other):
#         if isinstance(other, ChessPlayer):
#             return self.rating == other.rating
#         if isinstance(other, int):
#             return self.rating == other
#         return f'Невозможно выполнить сравнение'
#
#     def __gt__(self, other):
#         if isinstance(other, ChessPlayer):
#             return self.rating > other.rating
#         if isinstance(other, int):
#             return self.rating > other
#         return f'Невозможно выполнить сравнение'
#
#     def __lt__(self, other):
#         if isinstance(other, ChessPlayer):
#             return self.rating < other.rating
#         if isinstance(other, int):
#             return self.rating < other
#         return f'Невозможно выполнить сравнение'
#
#
#
# magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
# ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
# print(magnus == 4000) # False
# print(ian == 2789) # True
# print(magnus == ian) # False
# print(magnus > ian) # True
# print(magnus < ian) # False
# print(magnus < [1, 2]) # печатает "Невозможно выполнить сравнениe"

# method eq and hash++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         return isinstance(other, Point) and \
#                self.x == other.x and self.y == other.y
#
#     def __hash__(self):
#         return hash(id(self)) #hash((self.x, self.y))
#
#     def __repr__(self):
#         return f'{self.x}, {self.y}'
#
# d = {}
# p1 = Point(1, 2)
# p2 = Point(1, 2)
# print(p1==p2)
# print(hash(p1))
# print(hash(p2))
# d[p1] = 100
# d[p2] = 200
# print(d) #{1, 2: 100, 1, 2: 200}


# __bool__+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __len__(self):
#         print('len___')
#         return abs(self.x - self.y)
#
#     def __bool__(self):
#         if self.x != 0 or self.y != 0:
#             print('bool___')
#             return True
#         return False
#
#
# p1 = Point(1, 0)
# print(bool(p1))

# class City:
#
#     def __init__(self, name):
#         self.name = name.title() #''.join([word[0].upper() + word[1:] for word in name])
#
#     def __str__(self):
#         return f'{self.name}'
#
#     def __bool__(self):
#         if self.name[-1] in 'a, e, i, o, u':
#             return False
#         return True

# p1 = City('new york')
# print(p1)  # печатает "New York"
# print(bool(p1))  # печатает "True"
# p2 = City('SaN frANCISk')
# print(p2)  # печатает "San Francisco"
# print(p1 == True)  # печатает "False"

# class Quadrilateral:
#
#     def __init__(self, *args):
#         if len(args) == 1:
#             self.width = args[0]
#             self.height = args[0]
#         else:
#             self.width, self.height = args
#
#     def __str__(self):
#         if self.width == self.height:
#             return f'Куб размером {self.width}х{self.height}'
#         return f'Прямоугольник размером {self.width}х{self.height}'
#
#     def __bool__(self):
#         return self.width == self.height
#
#
# q1 = Quadrilateral(10)
# print(q1)  # печатает "Куб размером 10х10"
# print(bool(q1))  # печатает "True"
# q2 = Quadrilateral(3, 5)
# print(q2)  # печатает "Прямоугольник размером 3х5"
# print(q2 == True)  # печатает "False"


# class Counter:
#
#     def __init__(self):
#         self.counter = 0
#         self.summ = 0
#         self.lenths = 0
#         print('init object', self)
#
#     def __call__(self, *args, **kwargs):
#         self.counter += 1
#         self.summ += sum(args)
#         self.lenths += len(args)
#         return f'our instance was called {self.counter} times'
#
#     def average(self):
#         return int(self.summ/self.lenths)
#
# v = Counter()
# print(v.summ)
# print(v.lenths)
# print(v.counter)
# print(v(1, 5, 8))
# print(v.summ)
# v(3, 18)
# print(v.summ)
# print(v.lenths)
# print(v.average())

# __call__+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# from time import perf_counter
#
# class Timer:
#
#     def __init__(self, func):
#         self.fn = func
#
#     def __call__(self, *args, **kwargs):
#         start = perf_counter()
#         print('start timer')
#         work_func = self.fn(*args, **kwargs)
#         finish_count_time = perf_counter()
#         print(f'work func time = {finish_count_time - start}')
#         return work_func
#
# # @Timer
# # def per(n):
# #     pr = 1
# #     for i in range(1, n + 1):
# #         pr *= i
# #     return pr
#
# def fib(n):
#     if n <= 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
# print(Timer(fib)(40))

# Polimorfizm***************************************************************************************

# class Rectangle:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __repr__(self):
#         return f'{self.a}, {self.b}'
#
#     def get_rect_area(self):
#         return self.a * self.b
#
# class Square:
#
#     def __init__(self, a):
#         self.a = a
#
#     def __repr__(self):
#         return f'{self.a}'
#
#     def get_sq_area(self):
#         return self.a ** 2
#
# class Circle:
#
#     def __init__(self, r):
#         self.r = r
#
#     def __repr__(self):
#         return f'{self.r}'
#
#     def get_cir_area(self):
#         return 3.14 * self.r ** 2
#
#
# rec1 = Rectangle(2, 6)
# rec2 = Rectangle(4, 5)
# cir1 = Circle(2)
# cir2 = Circle(4)
# sq1 = Square(3)
# sq2 = Square(7)
#
# figures = (rec1, rec2, sq1, sq2, cir1, cir2)
# print(figures)
# for figure in figures:
#     if isinstance(figure, Rectangle):
#         print(figure.get_rect_area())
#     elif isinstance(figure, Square):
#         print(figure.get_sq_area())
#     else:
#         print(figure.get_cir_area())

# Polimorfizm if all merhod named identi

# class Rectangle:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return f'side rectangle = {self.a}x{self.b}'
#
#     def get_area(self):
#         return self.a * self.b
#
# class Square:
#
#     def __init__(self, a):
#         self.a = a
#
#     def __str__(self):
#         return f'side = {self.a}'
#
#     def get_area(self):
#         return self.a ** 2
#
# class Circle:
#
#     def __init__(self, r):
#         self.r = r
#
#     def __str__(self):
#         return f'radius circle = {self.r}'
#
#     def get_area(self):
#         return 3.14 * self.r ** 2
#
#
# rec1 = Rectangle(2, 6)
# rec2 = Rectangle(4, 5)
# cir1 = Circle(2)
# cir2 = Circle(4)
# sq1 = Square(3)
# sq2 = Square(7)
#
# figures = (rec1, rec2, sq1, sq2, cir1, cir2)
# print(figures)
# for figure in figures:
#     print(figure, figure.get_area())

# Method __getitem__, __setitem__, __delitem__+++++++++++++++++++++++++++++++++++++++++++++++++++++++

# class Vector:
#
#     def __init__(self, *args):
#         self.values = list(args)
#
#     def __repr__(self):
#         return str(self.values)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.values):
#             return self.values[item]
#         else:
#             raise IndexError('index out of range')
#
#     def __setitem__(self, key, value):
#         if 0 <= key < len(self.values):
#             self.values[key] = value
#         elif key > len(self.values):
#             deff = key - len(self.values)#  разряженный список до значения введенного индекса
#             self.values.extend([0]*(deff+1))
#             self.values[key] = value
#         else:
#             raise IndexError('index out of range')
#
#     def __delitem__(self, key):
#         if 0 <= key < len(self.values):
#            del self.values[key]
#         else:
#             raise IndexError('index out of range')
#
# v1 = Vector(1, 2, 8, 5, 4)
# print(v1)
# print(v1.values)
# v2 = Vector(10, 7, 4, 5, 3)
# print(v2.values[1]) # 7
# print(v2[1]) #TypeError: 'Vector' object is not subscriptable without __getitem__
# print(v2[1]) #with __getitem__ = 7
# v2[1] = 150
# print(v2) #[10, 150, 4, 5, 3]
# del v2[1]
# print(v2) #[10, 4, 5, 3]
# v2[10] = 16
# print(v2)

# class Vector:
#
#     def __init__(self, **kwargs):
#         self.values = dict(kwargs)
#
#     def __repr__(self):
#         return str(self.values)
#
#     def __getitem__(self, item):
#         return self.values[item]
#
#     def __setitem__(self, key, value):
#         self.values[key] = value
#
#
#     def __delitem__(self, key):
#        del self.values[key]
#
# v1 = Vector(a=1, b=2, c=3)
# print(v1)
# print(v1.values)
# print(v1['b'])
# v1[2] = 5
# print(v1)

# Method __iter__ and __next__+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# class Mark:
#
#     def __init__(self, value):
#         self.value = value
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.value):
#             raise StopIteration
#         else:
#             letter = self.value[self.index]
#             self.index += 1
#             return letter
#
#
# class Student:
#
#     def __init__(self, name, surname, marks):
#         self.name = name
#         self.surname = surname
#         self.marks = marks
#
#     def __iter__(self):
#         self.index = 0
#         return iter(self.marks)
#
#     def __next__(self):
#         if self.index >= len(self.marks):
#             raise StopIteration
#         else:
#             letter = self.marks[self.index]
#             self.index += 1
#             return letter
#
# m = Mark([8, 7, 9, 10, 6, 7])
# nick = Student('Nick', 'Mitchel', m)
# for i in nick:
#     print(i)


# class MyNumIter:
#
#     def __init__(self):
#         self.nums = '0123456789'
#         self.counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.counter >= len(self.nums):
#             raise StopIteration
#         else:
#             mark = self.nums[self.counter - 1]
#             self.counter += 1
#             if self.counter % 2 == 0:
#                 return mark
#
#
# c = MyNumIter()
# print(iter(c))  # <__main__.MyNumIter object at 0x0000023ADE809608>

# for i in c:
#     print(i, end=' ')

# c = 'jfsl ksKjll ekljs'
# print(' '.join([i[0].upper() + i[1:].lower() for i in c.split()]))
# print(c.title())


# perimeter_sequence = lambda a, n: a*n*4
#
# print(perimeter_sequence(1, 3))

# def cost(mins):
#     sum = 30
#     if mins <= 65:
#         return 30
#     elif mins > 65:
#         sum += 10
#         a = mins - 60
#         for i in range(30, a + 1, 30):
#             sum += 10
#         if (mins - 60) % 30 <= 5:
#             sum -= 10
#     return sum
#
# print(cost(346))

# principle inheritance++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# class Person: # Parent
#
#     def can_walk(self):
#         print('I can walk')
#
#     def can_jump(self):
#         print('I can jump')
#
#
# class Doctor(Person):#subclass
#
#     def can_cure(self):
#         print('I can treat')
#
# class Housewife(Doctor):
#     pass
#
# class Architect(Person):#subclass
#
#     def can_build(self):
#         print('I can build')
#
#
#
# d = Architect()
# d.can_walk()
# d.can_build()
# a = Doctor()
# a.can_walk()
# a.can_cure()
# b = Housewife
# b.can_cure()#can_walk() can_jump()
# print(issubclass(Doctor, Person))#True
# print(isinstance(d, Architect))#True
# print(isinstance(d, Person))#True

# class Person: # Parent
#     pass
#
# class MyDict(dict):
#     pass
#
# class Doctor(Person):#subclass
#     pass
#
# class Architect(Person):#subclass
#     pass
# a = MyDict()
# print(a)#{}

# class NewInt(int):
#
#     def __init__(self, value):
#         self.value = value
#
#     def repeat(self, n=2):
#         self.n = n
#         return int(self.n * str(self.value))
#
#     def to_bin(self):
#         return f'{int(bin(self.value)[2:])} - двоичное представление числа {self}'
#
# # or
# # class NewInt(int): #
# #
# #     def repeat(self, n=2):
# #         return int(str(self) * n)
# #
# #     def to_bin(self):
# #         return int(bin(self)[2:])

# a = NewInt(16)
# print(a.repeat())  # печатает число 99
# d = NewInt(a + 5)
# print(d.repeat(3)) # печатает число 141414
# b = NewInt(NewInt(7) * NewInt(5))
# print(b)
# print(a.to_bin()) # печатает 100011 - двоичное представление числа 35

# method overriding++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# class Person:  # Parent
#
#     def __init__(self, name):
#         self.name = name
#
#     def can_walk(self):
#         print('Person can walk')
#
#     def can_jump(self):
#         print('Person can jump')
#
#     def combo(self):
#         self.can_walk()
#         self.can_jump()
#
#     def __str__(self):
#         return f'Person {self.name}'
#
# class Doctor(Person):  # subclass
#
#     def can_jump(self):
#         print('Doctor can jump and swim')
#
#     def __str__(self):
#         return f'Doctor {self.name}'
#
#
# d = Person('Alex')
# a = Doctor('Robinson')
# print(d)
# print(a)
# a.combo()

# Extending+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# class Person:
#
#     age = 25
#     def sleep(self):
#         print('Person can sleep')
#
#     def combo(self):
#         if hasattr(self, 'can_walk'):
#             self.can_walk()
#         if hasattr(self, 'can_jump'):
#             self.can_jump()
#         self.sleep()
#         print(self.age)
#
# class Doctor(Person):
#
#     age = 30
#     def can_walk(self):
#         print('Doctor can walk')
#
#     def can_jump(self):
#         print('Doctor can jump')
#
#     def sleep(self):
#         print('Doctor can sleep')
#
# p = Person()
# d = Doctor()
# p.combo()
# print('--'*10)
# d.combo()

# Delegating+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# class Person:
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __str__(self):
#         return f'Person {self.name}, {self.surname}'
#
#     def sleep(self):
#         print('Person can sleep')
#
#     def info(self):
#         print('Paren class')
#         print(self)
#
# class Doctor(Person):
#
#     def __init__(self, name, surname, age):
#         super(Doctor, self).__init__(name, surname)
#         self.age = age
#
#     def __str__(self):
#         return f'Doctor {self.name}, {self.surname}, {self.age}'
#
#     def sleep(self):
#         super(Doctor, self).sleep()
#         print('Doctor can sleep')
#         super(Doctor, self).sleep()
#
# p = Person('Vitold', 'Boshak')
# d = Doctor('Nick', 'Korik', 87)
# print(p.name, p.surname)
# print(d.name, d.surname, d.age)
# print(p)
# print(d)
# print('**'*10)
# d.info()

# class Transport:
#
#     def __init__(self, brand, max_speed, kind=None):
#         self.brand = brand
#         self.max_speed = max_speed
#         self.kind = kind
#
#     def __str__(self):
#         return f'Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч'
#
# class Car(Transport):
#     def __init__(self, brand, max_speed, mileage, gasoline_residue):
#         super(Car, self).__init__(brand, max_speed)
#         self.kind = 'Car'
#         self.mileage = mileage
#         self.__gasoline_residue = gasoline_residue
#
#     def __str__(self):
#         return f'Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч'
#
#     @property
#     def gasoline(self):
#         return f'Осталось бензина на {self.__gasoline_residue} км'
#
#     @gasoline.setter
#     def gasoline(self, value):
#         if isinstance(value, int):
#             self.__gasoline_residue += value
#             print(f'Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л')
#         else:
#             print('Ошибка заправки автомобиля')
#
# class Boat(Transport):
#
#     def __init__(self, brand, max_speed, owners_name):
#         super(Boat, self).__init__(brand, max_speed)
#         self.owners_name = owners_name
#         self.kind = 'Boat'
#
#     def __str__(self):
#         return f'Этой лодкой марки {self.brand} владеет {self.owners_name}'
#
# class Plane(Transport):
#     def __init__(self, brand, max_speed, capacity):
#         super(Plane, self).__init__(brand, max_speed)
#         self.capacity = capacity
#         self.kind = 'Plane'
#
#     def __str__(self):
#         return f'Самолет марки {self.brand} вмещает в себя {self.capacity} людей'
#
# transport = Transport('Telega', 10)
# print(transport)  # Тип транспорта None марки Telega может развить скорость 10 км/ч
# bike = Transport('shkolnik', 20, 'bike')
# print(bike)  # Тип транспорта bike марки shkolnik может развить скорость 20 км/ч
#
# first_plane = Plane('Virgin Atlantic', 700, 450)
# print(first_plane)  # Самолет марки Virgin Atlantic вмещает в себя 450 людей
# first_car = Car('BMW', 230, 75000, 300)
# print(first_car)  # Тип транспорта Car марки BMW может развить скорость 230 км/ч
# print(first_car.gasoline)  # Осталось бензина на 300 км
# first_car.gasoline = 20  # Печатает 'Объем топлива увеличен на 20 л и составляет 320 л'
# print(first_car.gasoline)  # Осталось бензина на 320 км
# second_car = Car('Audi', 230, 70000, 130)
# second_car.gasoline = [None]  # Печатает 'Ошибка заправки автомобиля'
# first_boat = Boat('Yamaha', 40, 'Petr')
# print(first_boat)  # Этой лодкой марки Yamaha владеет Petr

# class Initialization:
#
#     def __init__(self, capacity, food):
#         if not isinstance(capacity, int):
#             print('Количество людей должно быть целым числом')
#         else:
#             self.capacity = capacity
#             self.food = food
#
#     def __str__(self):
#         return f'{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}'
#
# class Vegetarian(Initialization):
#
#     def __init__(self, capacity, food):
#         super(Vegetarian, self).__init__(capacity, food)
#
#     def __str__(self):
#         return f'{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}'
#
# class MeatEater(Initialization):
#
#     def __init__(self, capacity, food):
#         super(MeatEater, self).__init__(capacity, food)
#
#     def __str__(self):
#         return f'{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}'
#
# class SweetTooth(Initialization):
#
#     def __init__(self, capacity, food):
#         super(SweetTooth, self).__init__(capacity, food)
#
#     def __str__(self):
#         return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}'
#
#     def __eq__(self, other):
#         if isinstance(other, int):
#             return other == self.capacity
#         if isinstance(other, Initialization):
#             return other.capacity == self.capacity
#         return f'Невозможно сравнить количество сладкоежек с {other}'
#
#     def __lt__(self, other):
#         if isinstance(other, int):
#             return other > self.capacity
#         if isinstance(other, Initialization):
#             return other.capacity > self.capacity
#         return f'Невозможно сравнить количество сладкоежек с {other}'
#
#     def __gt__(self, other):
#         if isinstance(other, int):
#             return other < self.capacity
#         if isinstance(other, Initialization):
#             return other.capacity < self.capacity
#         return f'Невозможно сравнить количество сладкоежек с {other}'
#
#
# v_first = Vegetarian(10000, ['Орехи', 'овощи', 'фрукты'])
# print(v_first)  # 10000 людей предпочитают не есть мясо! Они предпочитают ['Орехи', 'овощи', 'фрукты']
# v_second = Vegetarian([23], ['nothing'])  # Количество людей должно быть целым числом
# m_first = MeatEater(15000, ['Жареную картошку', 'рыба'])
# print(m_first)  # 15000 мясоедов в Москве! Помимо мяса они едят еще и ['Жареную картошку', 'рыба']
# s_first = SweetTooth(30000, ['Мороженое', 'Чипсы', 'ШОКОЛАД'])
# print(s_first)  # Сладкоежек в Москве 30000. Их самая любимая еда: ['Мороженое', 'Чипсы', 'ШОКОЛАД']
# print(s_first > v_first)  # True
# print(30000 == s_first)  # True
# print(s_first == 25000)  # False
# print(100000 < s_first)  # False
# print(100 < s_first)  # True

# Multi_Delegating+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# class Doctor:
#
#     def __init__(self, rank):
#         self.rank = rank
#
#     def graduate(self):
#         print('Eeeepp i am a doctor')
#
#     def can_cure(self):
#         print('I am doctor, i can cure ')
#
#     def can_build(self):
#         print('I am doctor i can build too')
#
# class Builder:
#
#     def __init__(self, degree):
#         self.degree = degree
#
#     def graduate(self):
#         print('Eeeepp i am a builder')
#
#     def can_build(self):
#         print('I am builder i can build')
#
# class Person(Doctor, Builder):
#
#     def __init__(self, rank, degree):
#         super(Person, self).__init__(rank)
#         Builder.__init__(self, degree)
#
#     def __str__(self):
#         return f'Person {self.rank}, {self.degree}'
#
#     def graduate(self):
#         print('Look who i am')
#         super(Person, self).graduate()
#         Builder.graduate(self)
#
# p = Person('Lord', 5)
# p.can_cure()
# p.can_build() # class Person(Doctor, Builder) first find in Doctor I am doctor i can build too
# p.can_build() # class Person(Builder, Doctor) first find in Builder I am builder i can build
# print(Person.__mro__) # (<class '__main__.Person'>, <class '__main__.Doctor'>, <class '__main__.Builder'>,
# <class 'object'>)
# p.graduate()
# print(p) #Person Lord, 5

# Slots++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# from timeit import timeit
#
# class Point:
#
#     def __init__(self, x, y): #method __init__
#         self.x = x # instance class self.x, attribute x
#         self.y = y
#
# class PointSlots:
#
#     __slots__ = ('x', 'y') # input only x, y
#
#     def __init__(self, x, y): #method __init__
#         self.x = x # instance class self.x, attribute x
#         self.y = y
#
#     def __str__(self):
#         return f'PointSlots position {self.x}, {self.y}'
#
#
# def make_time1():
#     s = Point(4, 5)
#     s.x = 100
#     s.x
#     del s.x
#
# def make_time2():
#     s = PointSlots(4, 5)
#     s.x = 100
#     s.x
#     del s.x
#
# print(timeit(make_time1)) #0.799924
# print(timeit(make_time2)) #0.5114496

# d = PointSlots(4, 5)
# d.x = 500
# #d.q = 200 # AttributeError: 'PointSlots' object has no attribute 'q'
# print(d)
# a = Point(4, 5)
# a.q = 500
# print(a.__dict__)

# Slots property++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# class Rectangle:
#
#     __slots__ = ('__width', '__height', '__perim')
#
#     def __init__(self, a, b):
#         self.__width = a
#         self.__height = b
#         self.__perim = None
#
#     @property
#     def perim(self):
#         if self.__perim is None:
#             self.__perim = self.__width + self.__height * 2
#         return self.__perim
#
#     @perim.setter
#     def perim(self, value):
#         self.__width, self.__height = value
#         self.__perim = None
#
#     @property
#     def area(self):
#         return self.__width * self.__height
#
#
# class Square(Rectangle):
#     __slots__ = 'color'
#
#     def __init__(self, a, b, color):
#         super(Square, self).__init__(a, b)
#         self.color = color
#
#
# c = Rectangle(4, 5)
# print(c.perim)
# c.perim = 2, 3
# print(c.perim)
#
# d = Square(2, 2, 'Red')
# print(d.area, d.color)

# Exceptions++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# print('hello')
# print('hello1')
# print('hello2')
# try:
#     int('hello')
# except ValueError:
#     print('Неправильное преобразование')
# print('hello3')

# class Wallet:
#
#     def __init__(self, currency, balance):
#         self.balance = balance
#         if not isinstance(currency, str):
#             raise TypeError('Неверный тип валюты')
#         elif len(currency) != 3:
#             raise NameError('Неверная длина названия валюты')
#         elif currency != currency.upper() and len(currency) == 3:
#             raise ValueError('Название должно состоять только из заглавных букв')
#         else:
#             self.currency = currency
#
#     def __eq__(self, other):
#         if isinstance(other, Wallet):
#             if other.currency != self.currency:
#                 raise ValueError('Нельзя сравнить разные валюты')
#             return other.balance == self.balance
#         if isinstance(other, int):
#             raise TypeError(f'Wallet не поддерживает сравнение с {other}')
#
#     def __add__(self, other):
#         if isinstance(other, Wallet):
#             if other.currency == self.currency:
#                 return Wallet(self.currency, self.balance + other.balance)
#         if isinstance(other, int):
#             raise ValueError('Данная операция запрещена')
#
#     def __sub__(self, other):
#         if isinstance(other, Wallet):
#             if other.currency == self.currency:
#                 return Wallet(self.currency, self.balance - other.balance)
#         if isinstance(other, int):
#             raise ValueError('Данная операция запрещена')

# wallet1 = Wallet('USD', 50)
# wallet2 = Wallet('RUB', 100)
# wallet3 = Wallet('RUB', 150)
# # wallet4 = Wallet(12, 150)  # исключение TypeError('Неверный тип валюты')
# # wallet5 = Wallet('qwerty', 150)  # исключение NameError('Неверная длина названия валюты')
# # wallet6 = Wallet('abc', 150)  # исключение ValueError('Название должно состоять только из заглавных букв')
# print(wallet2 == wallet3)  # False
# # print(wallet2 == 100)  # TypeError('Wallet не поддерживает сравнение с 100')
# # print(wallet2 == wallet1)  # ValueError('Нельзя сравнить разные валюты')
# wallet7 = wallet2 - wallet3
# print(wallet7.currency, wallet7.balance)  # печатает 'RUB 250'
# wallet2 + 45  # ValueError('Данная операция запрещена')

# def third():
#     print('third start')
#     print('third end')
#
# def second():
#     print('second start')
#     try:
#         1/0
#     except ZeroDivisionError:
#         print('На ноль делить нелзя')
#     third()
#     print('second end')
#
#
# def first():
#     print('First start')
#     second()
#     print('First end')
#
# print('Hello')
# first()

# try:
#     1/0
#     int('joon')
#     a + b
# except ZeroDivisionError:
#     print('eroDivisionError')
# except ValueError:
#     print('invalid literal for int(), only digit')
# except Exception:
#     print('eroDivisionError')

# d = 'hello'
# c = {}
# try:
#     d[15]
#     c['key']
# except (IndexError, KeyError) as error:
#     print(f'Loddind error: {repr(error)}')
#     raise #TypeError from None # if you want see last error
# else:
#     print('good') # you can see 'good' if try without exception
# finally:
#     print('end')

# users exceptions++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# class MyExceptions(Exception):
#     '''This is my first exception'''
#
#     def __init__(self, *args):
#         if args:
#             self.massage = args[0]
#         else:
#             self.massage = None
#
#     def __str__(self):
#         if self.massage:
#             return f'MyExceptions {self.massage}'
#         else:
#             return 'MyExceptions is empty'
#
# d = MyExceptions('hello', 15)
# raise d
# # try:
# #     raise MyExceptions('it work')
# # except Exception:
# #     print('done')

# class River:
#     # список всех рек
#     all_rivers = []
#
#     def __init__(self, name, length):
#         self.name = name
#         self.length = length
#         # добавляем текущую реку в список всех рек
#         River.all_rivers.append(self)
#
#     def __str__(self):
#         return f'{self.name} {self.length}'
#
#
# volga = River("Волга", 3530)
# seine = River("Сена", 776)
# nile = River("Нил", 6852)
#
# # далее печатаем все названия рек
# for river in River.all_rivers:
#     print(river.name)

# class Book:
#
#     def __init__(self, name, author):
#         self.name = name
#         self.author = author
#
#     def __str__(self):
#         return f'{self.name} - {self.author}'
#
# a = Book(input(), input())
# b = Book(input(), input())
# c = Book(input(), input())
# print(a)
# print(b)
# print(c)


# class Movie:
#     def __init__(self, title,director, year):
#         self.title = title
#         self.year = year
#         self.director = director
#
#     def __str__(self):
#         return f'«{self.title}» (реж. {self.director}, {self.year})'
#
# # objects of the class Movie
# titanic = Movie('Титаник', 'Джеймс Кэмерон', '1997')
# star_wars = Movie('Звездные войны', 'Джордж Лукас', '1977')
# fight_club = Movie('Бойцовский клуб', 'Дэвид Финчер', '1999')
#
# # don't delete this code
# # it is here to check your results
# print(titanic.title)
# print(star_wars.year)
# print(fight_club.director)
# print(Movie(star_wars))

# class Student:
# 
#     def __init__(self, name, last_name, birth_year):
#         self.name = name[0]
#         self.last_name = last_name
#         self.birth_year = birth_year
# 
#     def __str__(self):
#         return f'{self.name}{self.last_name}{self.birth_year}'
# 
# n = Student(name=input(), last_name=input(), birth_year=input())
# 
# print(n)

# our class Ship
# class Ship:
#     def __init__(self, name, capacity):
#         self.name = name
#         self.capacity = capacity
#         self.cargo = 0
#
#             # the old sail method that you need to rewrite
#     def sail(self, arg):
#         self.arg = arg
#         print(f"The {self.name} has sailed for {self.arg}!")
#
# black_pearl = Ship("Black Pearl", 800)
# black_pearl.sail(input())

# class User:
#     def __init__(self, username):
#         self.username = username
#         self.friends = 0
#
#     # fix this method
#     def add_friends(self, n):
#         self.friends += n
#         print(f"{self.username} now has {self.friends} friends.")
#
# a = User('Alex')
# a.add_friends(5)


# class PiggyBank:
#
#         def __init__(self, dollars, cents):
#             self.total_cents = dollars * 100 + cents
#
#         @property
#         def dollars(self):
#             return self.total_cents // 100
#
#         @property
#         def cents(self):
#             return self.total_cents % 100
#
#         def add_money(self, deposit_dollars, deposit_cents):
#             self.total_cents += deposit_dollars * 100
#             self.total_cents += deposit_cents
#
#         def __str__(self):
#             return f'({self.dollars}, {self.cents})'

# a = PiggyBank(1512, 55)
# a.add_money(50,234)
# print(a)

# class Pet:
#     kind = "mammal"
#     n_pets = 0
#     pet_names = []
#
#     def __init__(self, spec, name):
#         self.spec = spec
#         self.name = name
#         self.legs = 4
#
#     def __str__(self):
#         return f'{self.name} {self.spec}'
#
#     def add_p(self):
#         Pet.n_pets += 1
#
#     def addlist(self):
#         Pet.pet_names.append(self.name)
#
# tom = Pet("cat", "Tom")
# tom.add_p()
# avocado = Pet("dog", "Avocado")
# avocado.add_p()
# ben = Pet("goldfish", "Benjamin")
# ben.add_p()
# tom.addlist()
# avocado.addlist()
# ben.addlist()
# print(Pet.n_pets)
# print(Pet.pet_names)


# class CPU:
#     def __init__(self, name, fr):
#         self.name = name
#         self.fr = fr
#
#
# class Memory:
#     def __init__(self, name, volume):
#         self.name = name
#         self.volume = volume
#
#
# class MotherBoard:
#
#     def __init__(self, name, cpu,  *args):
#         self.name = name
#         self.cpu = cpu
#         self.total_mem_slots = 4
#         self.mem_slots = args[:self.total_mem_slots]
#
#     def get_config(self):
#         return[
#             f"Материнская плата: {self.name}",
#             f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
#             f"Слотов памяти: {self.total_mem_slots}",
#             "Память: " + '; '.join(map(lambda x: f"{x.name} - {x.volume}", self.mem_slots))
#         ]
#
#
# cpu = CPU('asus', 1333)
# mb = MotherBoard('Asus', cpu, Memory('Kingstone', 4000), Memory('Kingstone', 4000))
# print(mb.get_config())


# class Cart:
#
#     def __init__(self, goods=[]):
#         self.goods = goods
#
#     def add(self, gd):
#         self.goods.append(gd)
#
#     def remove(self, indx):
#         self.goods.pop(indx)
#
#     def get_list(self):
#         all_goods = []
#         for i in self.goods:
#             all_goods.append(f'{i.name}: {i.price}')
#         return all_goods
#
#
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Table(Product):
#     pass
#
#
# class TV(Product):
#     pass
#
#
# class Notebook(Product):
#     pass
#
#
# class Cup(Product):
#     pass
#
#
# cart = Cart()
#
# tv1 = TV("samsung", 1111)
# tv2 = TV("LG", 1234)
# table = Table("ikea", 2345)
# n1 = Notebook("msi", 5433)
# n2 = Notebook("apple", 542)
# c = Cup("keepcup", 43)
#
# cart.add(tv1)
# cart.add(tv2)
# cart.add(table)
# cart.add(n1)
# cart.add(n2)
# cart.add(c)
# print(cart.get_list())
# import sys
#
#
# class ListObject:
#
#     def __init__(self, data):
#         self.next_obj = None
#         self.data = data
#
#     def link(self, obj):
#         self.next_obj = obj
#
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# head_obj = ListObject(lst_in[0])
# obj = head_obj
# for i in range(1, len(lst_in)):
#     obj_new = ListObject(lst_in[i])
#     obj.link(obj_new)
#     obj = obj_new
# from random import randint
#
#
# class Cell:
#
#     def __init__(self, around_mines=0, mine=False, fl_open=True):
#         self.around_mines = around_mines
#         self.mine = mine
#         self.fl_open = fl_open
#
#
# class GamePole:
#
#     def __init__(self, N, M):
#         self._n = N
#         self._m = M
#         self.pole = [[Cell() for _ in range(self._n)] for _ in range(self._n)]
#         self.init()
#
#     def init(self):
#         m = 0
#         while m < self._m:
#             i = randint(0, self._n - 1)
#             j = randint(0, self._n - 1)
#             if self.pole[i][j].mine:
#                 continue
#             self.pole[i][j].mine = True
#             m += 1
#         inde = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
#         for x in range(self._n):
#             for y in range(self._n):
#                 if not self.pole[x][y].mine:
#                     mines = sum((self.pole[x + i][y + j].mine for i, j in inde if
#                                  0 <= x + i < self._n and 0 <= y + j < self._n))
#                     self.pole[x][y].around_mines = mines
#
#     def show(self):
#         for row in self.pole:
#             print(*map(lambda x: '#' if not x.fl_open else x.around_mines if not x.mine else '*', row))
#
#
# pole_game = GamePole(10, 12)
# pole_game.show()


n = 5
a = [['#' for _ in range(5)] for _ in range(5)]
for i in a:
    print(*i)
print()

b = [[0] * n for _ in range(n)]

for a in b:
    print(a)

    #test
