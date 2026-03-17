#Object-Oriented Programming (OOP) is a way of writing programs using objects and classes.
#A class is a blueprint (template)
#An object is an instance of a class

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

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Take your cash.")
        # elif amount > self.__balance:
        #     print("Insufficient fund.")
    def get_balance(self):
            # return f"This is your balance:, {self.__balance}"

acc = BankAccount(50870)
acc.withdraw(32600)
# print(acc.get_balance())


# Requirements:
#
# Create a class called Rectangle
#
# It should have:
#
# length
#
# width
#
# Add these methods:
#
# area() → returns area (length × width)
#
# perimeter() → returns perimeter (2 × (length + width))



class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def sum(self):
        return self.__length + self.__width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)


x = Rectangle(3, 5)
print(x.sum())
print(x.area())
print(x.perimeter())