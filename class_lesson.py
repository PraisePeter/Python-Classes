#Object-Oriented Programming (OOP) is a way of writing programs using objects and classes.
#A class is a blueprint (template)
#An object is an instance of a class
from asyncio import Task


class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

# Creating objects
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

# print(car1.brand)   # Toyota
# print(car2.color)   # Blue


#__init__ is a constructor (runs automatically)
#self refers to the current object


# Methods (Functions inside a Class)
class Car:
    def __init__(self, brand):
        self.brand = brand

    # def drive(self):
    #     print(self.brand, "is moving")

# car1 = Car("Toyota")
# car1.drive()

#methods = drive

#Encapsulation (Data Protection)
#Encapsulation means restricting access to data.
#THE ENCAPSULATION IS REPRESENTED BY __
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
# print(acc.get_balance())



# Modify your class to allow a user to withdraw money.
#
# Requirements:
#
# Add a method called withdraw(amount)
#
# If the amount is less than or equal to balance → subtract it
#
# If the amount is greater → print "Insufficient funds"
#
# Keep using __balance (private variable)

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#     def deposit(self, amount):
#         self.__balance += amount
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print("Take your cash.")
#         # elif amount > self.__balance:
#         #     print("Insufficient fund.")
#     def get_balance(self):
#             # return f"This is your balance:, {self.__balance}"
#
# acc = BankAccount(50870)
# acc.withdraw(32600)
# # print(acc.get_balance())


# Task: Create a Rectangle Class
# 🎯 Requirements:
# Create a class called Rectangle
# It should have:
# length
# width
# Add these methods:
# area() → returns area (length × width)
# perimeter() → returns perimeter (2 × (length + width))
# display() → prints rectangle details


#
# class Rectangle:
#      def __init__(self, length, width):
#          self.__length = length
#          self.__width = width
#
#      def sum(self):
#          return self.__length + self.__width
#
#      def area(self):
#          return self.__length * self.__width
#
#      def perimeter(self):
#          return 2 * (self.__length + self.__width)
#
#      def display(self):
#          print(f"Length = {self.__length}, Width = {self.__width}")
#
# x = Rectangle(3, 5)
# x.display()
# print(x.sum())
# print(x.area())
# print(x.perimeter())



# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#     def perimeter(self):
#         return 2 * (self.length + self.width)
#
#     def display(self):
#         print("Length:", self.length, "Width:", self.width)
#
#
# # Testing
# r1 = Rectangle(5, 3)
#
# print(r1.area())
# print(r1.perimeter())
# r1.display()


"""
1. Inheritance
What is Inheritance?

Inheritance allows a class (child class) to reuse properties and methods from another class (parent class).
It helps you:
Avoid repeating code
Organize programs better
"""

# EXAMPLE 2
# class Animal:
#     def speak(self):
#         print("Animal makes a sound")
#
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
#
# d = Dog()
# d.speak()   # inherited method
# d.bark()    # child method


# EXAMPLE 2
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)   # call parent constructor. super().__init shows that particular constructor is from the parent class.
#         self.breed = breed
#
# d = Dog("Buddy", "Labrador")
# print(d.name, d.breed)

#N/B: INHERITANCE DOES NOT END WITH ONE CLASS (PARENT). A SUBCLASS CAN HAVE MORE THAN ONE PARENT


"""

Polymorphism
 What is Polymorphism?

Polymorphism means:
Same method name, different behavior

"""

# EXAMPLE 1
# class Bird:
#     def sound(self):
#         print("Bird makes a sound")
#
# class Parrot(Bird):
#     def sound(self):
#         print("Parrot talks")
#
# class Crow(Bird):
#     def sound(self):
#         print("Crow caws")
#
# p = Parrot()
# c = Crow()
#
# p.sound()
# c.sound()

# EXAMPLE 2
# class Vehicle:
#     def move(self):
#         print("Vehicle is moving")
#
# class Car(Vehicle):
#     def move(self):
#         print("Car is driving")
#
# class Plane(Vehicle):
#     def move(self):
#         print("Plane is flying")
#
# for v in [Car(), Plane()]:
#     v.move()


"""
Practice Task

Create:

A parent class Shape with method draw()
Two child classes:
Circle
Square
Override draw() in both classes
Use a loop to call them


Expected Output: 
Circle drawing
Square drawing

"""

#Lesson
# class Shape:
#     def draw(self):
#         print("This shape can be drawn")
#
# class Circle(Shape):
#     def draw(self):
#         print("Circle can be drawn")
#
# class Square(Shape):
#     def draw(self):
#         print("Square can be drawn")
#
# for c in [Circle(), Square()]:
#     c.draw()


"""
Task: Employee Management System
Requirements
1. Create a parent class Employee
Attributes:
name
salary
Method:
display() → prints name and salary
calculate_bonus() → returns 10% of salary
2. Create two child classes:
🔹 Manager
Inherits from Employee
Extra attribute: department
Override calculate_bonus() → 20% of salary
🔹 Developer
Inherits from Employee
Extra attribute: language
Override calculate_bonus() → 15% of salary
3. Use super()
Use it in constructors to initialize parent attributes
4. Polymorphism
Create a list of employees (Manager + Developer)
Loop through them and:
Call display()
Print their bonus
employees = [
    Manager("Alice", 5000, "HR"),
    Developer("Bob", 4000, "Python")
]

for emp in employees:
    emp.display()
    print("Bonus:", emp.calculate_bonus())
    


class Employee:
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name of the employee:, {self.name}, Salary: {self.salary}")

    def calculate_bonus(self):
        return (10 / 100) * self.salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def calculate_bonus(self):
        return (20 / 100) * self.salary

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def calculate_bonus(self):
        return (15 / 100) * self.salary

m = Manager("Alice", 5000, "HR")
d = Developer("Bob", 4000, "Python")
#
# for i in [Manager(), Developer()]:
#     m.display()
#     d.display()
#     m.department.display()
#     d.language.display()
# print(m.calculate_bonus())
# print(d.calculate_bonus())
employees = [Manager("Alice", 5000, "HR"),
             Developer("Bob", 4000, "Python")]

for emp in employees:
    emp.display()
    print("Bonus:", emp.calculate_bonus())
"""

"""
"