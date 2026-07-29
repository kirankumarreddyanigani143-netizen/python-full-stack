# class Animal:
#     def eat(self):
#         print("Animal eats food")

# class Bird(Animal):
#     def fly(self):
#         print("Bird can fly")

# class Parrot(Bird):
#     def speak(self):
#         print("Parrot can speak")

# p = Parrot()

# p.eat()
# p.fly()
# p.speak()


# class phone:
#     def call (self):
#         print("calling...")

# class music_player:
#     def play_music(self):
#         print("playing music")

# class smartphone(phone, music_player):
#     def take_photo(self):
#         print("taking photo")

# obj = smartphone()

# obj.take_photo()
# obj.play_music()
# obj.call()


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.available = True

#     def borrow_book(self):
#         if self.available:
#             print("Book Borrowed Successfully")
#             self.available = False
#         else:
#             print("Book Not Available")

#     def display(self):
#         print("title:", self.title)
#         print("author:", self.author)


# obj = Book("Python Programming", "ABC")

# obj.display()
# obj.borrow_book()
# obj.borrow_book()


# class Add:
#     def sum(self, a, b, c, d):
#         print(a + b + c + d)

# obj = Add()
# obj.sum(10, 20, 30, 40)


# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# obj = Dog()
# obj.sound()




# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def area(self):
#         r = 5
#         print("Area of Circle =", 3.14 * r * r)

# obj = Circle()
# obj.area()


# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Triangle(Shape):
#     def area(self):
#         b = 10
#         h = 5
#         print("Area of Triangle =", 0.5 * b * h)

# obj = Triangle()
# obj.area()



 # def add(a, b):
#     return a+b

# def multiply(a, b):
#     return a*b

# def divide(a, b):
#     return a%b

# def subtraction(a, b):
#     return a-b
-----------------------
# import os

# print(os.getcwd)
# print(os.listdir)
# print(os.mkdir('new floder'))
--------------------
# from datetime import date, datetime, timedelta

# now = datetime.now()
# print(now.year, now.month, now.day)

# print(now.strftime('%H : %M : %S'))

# today = date.today()
# print(today)

# tomorrow = today + timedelta(days=3)
# print(tomorrow)

# diff = datetime(2026, 7, 29) - datetime.now()
# print(diff)







