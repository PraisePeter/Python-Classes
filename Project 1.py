# # print("***********************")
# # print("***********************")
# # print("***********************")
# # print("***********************")
# #
# #
# #
# # print("***********************")
# # print("*                     *")
# # print("*                     *")
# # print("***********************")
# #
#
# # for i in range(5):
# #     print("Hello")
#
# # for i in range (5):
# #     num = eval(input("Enter a number: "))
# #     print("The square of your number is: ", num*num)
# # print("The loop is now done.")
#
# # print("A")
# # print("B")
# # for i in range(8) :
# #     print("C")
# # for i in range (5):
# #     print("D")
# # print("E")
#
# # print("A")
# # print("B")
# # for i in range(5) :
# #     print("C")
# #     print("D")
# # print("E")
#
# # for i in range (5):
# #     print(i + 1, " Praise")
#
# for i in range(0, 21, 5):
#     print(i)

# from random import randint
# y = randint(1900, 2026)
# print("A random number between 100 and 150 is: ", y)
''
from math import sqrt

# from math import sin, cos, tan
# print ("Sin(12) is roughly ", sin(12))
# print ("Cos(0) is roughly ", cos(0))
# print ("Tan(1) is roughly ", tan(1))


# from random import randint
# x = randint(1, 50)
# y = randint(2, 5)
# print("This is the result:",  x**y)

'''
# #EXERCISE 4
for i in range(20):
     print(i+1, "-- ", (i+1)*(i+1))

# #EXERCISE 6
for i in range(100, 1, -2):
     print(i)

# #EXERCISE 9
num = eval(input("How many Fibonacci numbers would you like?: "))
a = 1
b = 1

for i in range(1, num):
    print(a)
    a, b = b, a + b

# #EXERCISE 11
weight = eval(input("Enter your weight in kilograms: "))
pounds = weight * 2.20462262
print("This is your weight in Pounds: ", round(pounds, 1))


### IF STATEMENT
from random import randint

num = randint(1, 10)
guess = eval(input("Enter your guess: "))
if guess == num:
    print("You got it")
else:
    print("Sorry the number is: ", num) 

grade = eval(input("Enter your score: "))
if grade>=90:
     print("A")
if grade>= 80 and grade<90:
    print("B")
if grade>= 70 and grade<80:
    print("C")
if grade>= 60 and grade<70:
    print("D")
if grade<60:
    print("F") 


grade = eval(input("Enter your score: "))
if grade>=90:
     print("A")
elif grade>=80:
    print("B")
elif grade>=70:
    print("C")
elif grade>=60:
    print("D")
else:
    print("F") 


quantity = eval(input("Enter your quantity: "))
if quantity<10:
    price = 12
elif quantity<=99:
    price = 10
else:
    price = 7
print("The total cost is: ", quantity*price) 


credit = eval(input("Enter the number of credits taken: "))
if credit<=23:
    print("You are a freshman")
elif credit<=53:
    print("You are a sophomore")
elif credit<=83:
    print("You are a junior")
else:
    print("You are a senior") 


num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
x = (num1 - num2)
if abs(x) <=0.001:
    print("Close")
else:
    print("Not Close")  


count1 = 0
count2 = 0
for i in range(10):
    num = eval(input("Enter a number: "))
    if num > 10:
         count1 = count1 + 1
    if num==10:
        count2 = count2 + 1
print("There are: ", count1, "numbers greater than 10. ")
print("There are: ", count2, "zeros. ") '''
'''
count = 0
for i in range(1, 11):
    num = i**2
    print(num)
    if (num)%10==4:
        count = count + 1
print(count)  

s = 0
for i in range(1, 10):
    s = s + i
print("The sum is: ", s) 

count = 5
num = 10
if num>count:
    count=num
print(count)


smallest = eval(input("Enter a positive number: "))
for i in range(9):
    num = eval(input("Enter a positive number: "))
    if num<smallest:
        smallest = num
print("Smallest number: ", smallest) 

sname = "Gbaraneh"
if 'G' in sname:
    print("Your string contains the letter G")
else:
    print("Your string does not contain the letter g") 


name = input("Enter your name: ")
len(name)
print(name*10)

#
for i in range(name):
print(s[0])"   '''

'''
EXERCISE 4.5, NO 13

import random
user_score = 0
computer_score = 0

for i in range(5):
    user = input("Enter rock, paper or scissors: ").lower()
    computer = random.choice(["rock", "paper", "scissors"])

    if user == computer:
        pass
    elif user == "rock" and computer == "scissors":
        user_score += 1
    elif user == "paper" and computer == "rock":
        user_score += 1
    elif user == "scissors" and computer == "paper":
        user_score += 1
    else:
        computer_score += 1
print("Total User Score: ", user_score)
print("Total Computer Score: ", computer_score)

if user_score>computer_score:
    print("You won the game.")
elif user_score<computer_score:
    print("Computer won the game.")
else:
    print("The game is a tie.") '''

# I don't understand#
'''
count = 0
for i in range(5):
    num = eval(input("Enter a number: "))
    if num>count:
        count = count + 1
        print("Count:", count)
print("Result: ", count)
'''
'''
smallest = eval(input("Enter a positive number: "))
for i in range (1,11):
    user_number =eval(input("Enter a positive number: "))
    if user_number<smallest:
        smallest = user_number
print("The smallest value is: ", smallest) '''


'''
EXERCISE 5.9, NO 2

import math
count1 = 0
count2 = 0
for i in range(1,10):
    #num = eval(input("Enter a number: "))#
    num = (i*i)
    value = str(num)
    print(value)
    if "4" in value:
        count1 = count1 + 1
    elif "9" in value:
        count2 = count2 + 1
print("Counts of 4: ", count1)
print("Counts of 9: ", count2)  '''

'''
EXERCISE 5.9, NO 2
import math
count1 = 0
count2 = 0
for i in range(1,100):
    #num = eval(input("Enter a number: "))#
    num = (i*i)
    value = str(num)[-1]
    print(value)
    if value=='4':
        count1 = count1 + 1
    elif value=='9':
        count2 = count2 + 1
print("Counts of 4: ", count1)
print("Counts of 9: ", count2) '''


'''
EXERCISE 5.9, NO 3
from math import log

n = int(input("Enter a vale n: "))
x=0

for i in range(1,n+1):
    x += 1/i
    print(x)

solve = x-log(n)
print("Result: ", solve)  '''

'''EXERCISE 6.11, NO 1'''
'''
user = input("Enter your your occupation: ")

print(len(user))

x = user * 10
print(x)

first = user[0]
print("The first letter is: ", first)

f_three = user[:3]
print("The first three letters are: ", f_three)

l_three =user[-3:]
print("The last three letters are: ", l_three)

backwards = user[::-1]
print("The string shown backwards is: ", backwards)

if len(user)>=7:
    print("The seventh letter is: ", user[6])
else:
    print("The string is short.")


result = user[1:-1]
print("Middle: ", result)

print("All caps: ", user.upper())

print("A replaced with E: ", user.replace("a", "e"))

print("All strings in small letters: ", user.lower())  '''

'''
fname = input("Enter your name in lowercase: ")
print("Your full name is: ", fname.title()) '''


'''
How to know data types'''
'''
name = "praise"
score = [5, 8, 16, 15, 12, 3, 2]
score1 = [12, 17, 8, 9, 11, 66, 8]


a = score + score1
print(a)

b = a[:]
print("Copy List:", b) '''
'''
a.append(25)
print(a, "\n")

a.sort()
print(a, "\n")

print("Count: ", a.count(8), "\n")

print("Index:", a.index(11), "\n")

a.reverse()
print(a, "\n")

a.remove(66)
print(a, "\n")

a.pop(2)
print(a, "\n")

a.insert(0, 2026)
print(a, "\n") '''



'''
print(min(a))
print(max(a))
print(sum(a))

print(type(a))

print(score*3) '''
'''
print("This is the length of the list: ", len(a))
for i in range(len(a)):
    print(a[i]) '''
'''
print(type(score))
print(type(name))

print(len(score))

if 8 in score:
    print("Yes")

first = score[:3]
print("These are the first three letters: ", first) 

fruits = ["orange", "mango", "banana", "pear", "apple"]

fruits.insert(3, "green")
print(fruits, "\n")

del fruits[1]
print(fruits, "\n")  

from random import randint
mylist = []
for i in range(10):
    mylist.append(randint(1, 14))
print("Example 1:",mylist, "\n")

for i in range(len(mylist)):
    mylist[i] =mylist[i] ** 2
print("Example 2:", mylist, "\n")

count = 0
for item in mylist:
    if item > 100:
        count = count + 1
print("Example 3:", count, "\n")

print(mylist, "\n")

frequencies = []
for i in range(1, 101):
    frequencies.append(mylist.count(i))
print("Example 4: ", frequencies, "\n")

x = [1, 4, 6, 8,9]
x.append(7)
print(x, "\n")

scores = [10, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
scores.sort()
print("Two smallest: ", scores[0], ",", scores[1])
print("Two largest: ", scores[-1], ",", scores[-2], "\n")  

num = 0
print("What is the capital of France?", end=" ")
guess = input()
if guess.lower() == "paris":
    print("Correct")
    num+=1
else:
    print("Wrong.  The answer is Paris.")
print("You have", num, "out of 1 right")

print("Which state has only one neighbour?", end=" ")
guess = input()
if guess.lower() == "Maine":
    print("Correct")
    num+=1
else:
    print("Wrong. The answer is Maine.")
print("You have", num, "out of 2 right", "\n")  

#EXERCISE 1, 7.7#

family = ["Wisdom", "Success", "Delight", "Peter", "Helen"]

from random import sample
sample1 = sample(family, 1)
print(sample1, "\n")


from random import choice
choice1 = choice(family)
print(choice1, "\n")

from random import shuffle
shuffle(family)
for i in family:
    print(i, "It's your turn", "\n")
print(family, "\n") 

x = "I live at Number 310, avenue 4, New York"
print(x.split(), "\n")  

value = input("Enter five numbers: ")  

x = "I live at Number 310, avenue 4, New York" 


from string import punctuation
s = "This is good!"
for c in punctuation:
    s = s.replace(c, "+")
print(s, "\n")   

from string import punctuation

s = input("Enter a string: ")
for c in punctuation:
    s = s.replace(c, "")
s = s.lower()
l = s.split()

word = input("Enter a word: ")
print(word, "appears", l.count(word), "times.", "\n")  

from random import shuffle

word = input("Enter a word: ")

letter_list = list(word)
print(letter_list, "\n")
shuffle(letter_list)
print(letter_list, "\n")
anagram = "".join(letter_list)
print(anagram, "\n")  


values = []
for i in range(5):
    number = input("Enter a number: ")
    values.append(number)
print(values, "\n")

Result = "+".join(values)
print(Result, "\n")  

#EXERCISE 5#
from random import choice
Quote_of_the_day = ["Believe you can and you're halfway there.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The only way to do great work is to love what you do.",
    "Don’t watch the clock; do what it does. Keep going.",
    "Your time is limited, so don’t waste it living someone else’s life."]
print(choice(Quote_of_the_day), "\n")

#EXERCISE 6#
import random

numbers = random.sample(range(1, 49), 6)
print("Lottery number: ", numbers, "\n")
print(" ".join(map(str, numbers)))  

#EXERCISE 3, 8.7#

user = input("Enter a sentence: ")
print(user)
x = user.split()
print(x)

if len(x) >= 3:
    print("The third word is:", x[2], "\n")

else:
    print("The sentence does not have three words.")

user = input("Enter a sentence: ")

words = user.split()

third_words = words[2::3]
print("Example b:", " ".join(third_words)) 

string = "Hello"
L = [1, 14, 5, 9, 12]
M = ("one", "two", "three", "four", "five", "six")

u = [0 for i in range(10)]
print(L, "\n")

a = [i**2 for i in range(1,8)]
print(L, "\n")

x = [i*10 for i in L]
print(x, "\n")

y = [c*2 for c in string]
print(y, "\n")

p = [m[0] for m in M]
print(p, "\n")

h = [i for i in L if i<10]
print(h, "\n")

s = [m[0] for m in M if len(m) == 3]
print(s, "\n") 

L = []
for i in range(2):
    for j in range(2):
        L.append((i,j))
print(L, "\n")   

m = ["orange", "apple", "banana", "pear", "red"]
L = [1, 14, 5, 9, 100]

c = len([i for i in L if i>50])
print(c, "\n") 

L = [1, 14, 5, 9, 100]
frequencies = [L.count(i) for i in range(1, 20)]
print(frequencies, "\n")

from random import choice
alphabet = "abcdefghijklmnopqrstuvwxyz"
s = ",".join([choice(alphabet) for i in range(20)])
print(s, "\n")

M = [[2,3], [6,2], [1,0]]
c = [[y,x] for x,y in M]
print(c, "\n")   


temp = 0
while temp != -1000:
    temp = eval(input("Enter a temperature (-1000 to quit): "))
    if temp !=-1000:
        print("In Fahrenheit that is: ", 9/5*temp+32, "Fahrenheit")
    else:
        print("Bye")  


from random import randint
secret_num = randint(1, 10)
guess = 0 
while guess !=secret_num:
    guess = eval(input("Guess the secret number: "))
print("You finally got it!")  

i = 0
while i<10:
    print(i)
    i = i + 1  

for i in range(10):
    num = eval(input("Enter a number: "))
    if num<0:
        break


i = 0
num = 1
while i<10 and num>0:
    num = eval(input("Enter a number: "))  

#QUESTION 3, EXERCISE 9.6#

weight = eval(input("Enter a weight: "))
while weight < 0:
    weight = eval(input("Invalid Weight. Enter a valid weight: "))
print("Your weight is: ", 2.20462262185*weight, "pounds")

#QUESTION 4, EXERCISE 9.6#

password = "1234pp"
user = input("Enter a password: ")
tries = 0
while user != password and tries < 4:

    user = input("Invalid Password. Enter a valid password: ")
    tries = tries + 1
if user == password:
    print("You are logged in to the system")
else:
    print("Too many attempts. You have been logged out of the system.")
'''


"""
correct_password = "python123"
attempts = 0

while attempts < 5:
    password = input("Enter your password: ")

    if password == correct_password:
        print("You are logged in to the system.")
        break
    else:
        attempts += 1
        print("Incorrect password.")

if attempts == 5:
    print("You are kicked off of the system.")



correct_password = "python123"
attempts = 0

while attempts < 5:
    password = input("Enter your password: ")

    if password == correct_password:
        print("You are logged in to the system.")
        break
    else:
        attempts += 1
        print("Incorrect password.")

if attempts == 5:
    print("You are kicked off of the system.")

"""


"""
for i in range(1, 1001):
    s =str(i)
    if s ==s [::-1]:
        print(s)
sequence[start : stop : step] 
"""

"""
birthday = "January 1, 2001"
year = int(birthday[-4:])
print("You are", 2026-year, "years old", "\n")

birthday = "2001, January 1"
year = int(birthday[:4])
print("You are", 2026-year, "years old", "\n")

#DICTIONARY#

countries = {"Nigeria":"Lagos", "India":"Delhi", "Afghanistan":"Kabul", "Albania":"Tirana", "Algeria":"Algiers" }
countries["Nigeria"] = "Abuja"
countries["Ghana"] = "Accra"
del countries["Afghanistan"]
print(countries)
country = input("Enter a country: ")
print("The capital is: ", countries[country], "\n") 

deck = [{"value":i, "suit":c}
    for c in ["spades", "clubs", "hearts", "diamonds"]
    for i in range(2,15)]
print(deck)
deck = []

for c in ['spades', 'clubs', 'hearts', 'diamonds']:
    for i in range(2, 15):
        card = {'value': i, 'suit': c}
        deck.append(card)

card_value_map = {
    2:  "2",
    3:  "3",
    4:  "4",
    5:  "5",
    6:  "6",
    7:  "7",
    8:  "8",
    9:  "9",
    10: "10",
    11: "Jack",
    12: "Queen",
    13: "King",
    14: "Ace"
}


countries = {"Nigeria":"Lagos", "India":"Delhi", "Afghanistan":"Kabul", "Albania":"Tirana", "Algeria":"Algiers" }
countries["Nigeria"] = "Abuja"
countries["Ghana"] = "Accra"
del countries["Afghanistan"]


countries2 = countries.copy()
print(countries2)

country = input("Enter a country: ")
if country in countries2:
    print("The capital is:", countries2[country])
else:
    print("Not in dictionary")

#looping dictionary

for country in countries2:
    print(country)   """
#
# from string import punctuation
#
# text = open("romeo.txt").read()
# text = text.lower()
# for p in punctuation:
#     text = text.replace(p, " ")
# words = text.split()
# d = { }
# for w in words:
#     if w in d:
#         d[w] = d[w] + 1
#     else:
#         d[w] = 1
# items = list(d.items())
# items.sort()
# for i in items:
#     print(i)
#
# # items = [(i[1], i[0]) for i in items]
# # items.sort()
# # for i in items:
# #     print(i)
#
# items = list(d.items())              # (word, count)
# items = [(count, word) for word, count in items]  # swap
# items.sort()
#
# for item in items:
#     print(item)

#EXERCISE 1, 11.5

#create an empty dictionary to store product and prices
product = {}
#repeatedly ask user to enter product names and prices
while True:
    product_name = input("Enter product name (or 'done' to finish): ")
    if product_name.lower() == "done":
        break

    price = eval(input("Enter price (or 'done' to finish): "))
    product[product_name] = price
print(product)

#allow user to search for product prices
while True:
    search = input("Enter a product name to check price (or 'done' to quit): ")
    if search.lower() == "done":
        break
    if search in product:
        print("Price:", product[search])
    else:
        print("Not found")
print(product)

#EXERCISE 2

amount = eval(input("Enter an amount: $"))
while True:
    if product <= amount:
        print("Products: ", product)



# #EXERCISE 3
# days = {"January": 31, "February": 28, "March": 31, "April": 30,
#         "May": 31, "June": 30, "July": 31, "August": 31,
#         "September": 30, "October": 31, "November": 30, "December": 31}
#
# # a, how many days in a chosen month
#
# # search = input("Enter month: ")
# # print("The number of days is: ", days[search])
#
# # b, Print out all the keys in alphabetical order
# # items = list(days.values())
# # items.sort()
# # for i in items:
# #     print(i)
#
# #C PRINT OUT ALL THE MONTHS WITH 31 DAYS

