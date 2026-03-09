#Default arguments and keyword arguments

def double(name):
    print(name * 2)

#double("Praise")

def multiple_print(name, n=2):
    print(name * n)

# n=2 is DEFAULT ARGUMENT. The print values runs once if a value is not given to n by user
# 5 is the KEYWORD ARGUMENT
#multiple_print("Hello", 5)
#multiple_print("Hello")


#EXAMPLE 2
def fancy(text, color="black", background="white",
          style="normal", justify="left"):
    print(text, color, background, style, justify)
# fancy("Hi", style="bold")
# fancy("Hi", color="yellow", background="black")
# fancy("Hi")


def fancy_print(text, color='black', background='white',
                style='normal', justify='left'):
    print("Text:", text)
    print("Color:", color)
    print("Background:", background)
    print("Style:", style)
    print("Justify:", justify)
    print("-" * 20)


# Function calls
# fancy_print('Hi', style='bold')
# fancy_print('Hi', color='yellow', background='black')
# fancy_print('Hi')



def multiple_print(name, n=2):
    print("Name", name)
    print("Number of times", n)
    print("*" * 30)
    #print(f' our text is "{text}", {color}')
#FUNCTION CALLS
# multiple_print("Praise", n=5)
# multiple_print("Ego", n=7)
# multiple_print("Praise")


# def fancy_print(text, color='black', background='white'):
#     print(f' Our text is "{text}", the color is {color}, the background is {background}')
# # Function calls
# fancy_print(color="white", background="black", text="Praise")
#


#ASSIGNMENT EXERCISE 13.5, NO 4

# 4. The digital root of a number n is obtained as follows: Add up the digits n to get a new number.
# Add up the digits of that to get another new number. Keep doing this until you get a number
# that has only one digit. That number is the digital root.
# For example, if n = 45893, we add up the digits to get 4 + 5 + 8 + 9 + 3 = 29. We then add up
# the digits of 29 to get 2 + 9 = 11. We then add up the digits of 11 to get 1 + 1 = 2. Since 2 has
# only one digit, 2 is our digital root.
# Write a function that returns the digital root of an integer n. [Note: there is a shortcut, where
# the digital root is equal to n mod 9, but do not use that here.]

def user(name):
    print("What is your name:", name)

# user("Praise")

def digital_root (n):
    while n >= 10:
        total = 0
        for value in str(n):
            total = total + int(value)
        n = total
    return(n)
# print(digital_root(45678))



# digital_root(45678)


def get_digital_root(n):
    # Ensure n is positive for digit summation
    n = abs(n)

    # Continue process until n is a single digit
    while n >= 10:
        digit_sum = 0
        # Sum the digits
        for digit in str(n):
            digit_sum += int(digit)
        # Update n to the new sum
        n = digit_sum
        print(n)
#     # return (n)
# print(get_digital_root(45678))
# get_digital_root(45678)

#3. Write a function called sum_digits that is given an integer num and returns the sum of the
#digits of num
def sum_digits(n):
    digit_sum = 0
    for number in str(n):
        digit_sum = digit_sum + int(number)
        n = digit_sum
    return(n)
# print(sum_digits(243674))


#Write a function called count_digits that is given an
# integer num and returns the number of digits in the number.

#OPTION 1
def count_digits(n):
    print(len(str(n)))
    return(n)
# count_digits(5267)

#OPTION 2
def digits(n):
    n = abs(n)
    while True:
        count = 0
        for num in str(n):
            if n == 1:
                count+=1
            else:
                break
# count_digits(0)


#OPTION 3
def count_digits(num):
    num = abs(num)   # handles negative numbers
    count = 0

    if num == 0:
        return 1

    while num > 0:
        num = num // 10
        count += 1

    return count

#OPTION 4
def digits(n):
    n = abs(n)
    count = 0

    for num in str(n):
        count += 1

    return count


# print(digits(5372))


#TAKE HOME ASSIGNMENT
# 5. Write a function called first_diff that is given two strings and returns the first location in
# which the strings differ. If the strings are identical, it should return -1.


def first_diff(s1, s2):
    # Get the length of string
    length = min(len(s1), len(s2))

    for i in range(length):
        if s1[i] != s2[i]:
            return i

        if len(s1) != len(s2):
            return length

    return -1
print(first_diff("cane", "canes"))


# first location of "a" in our string

country = "nigeria"

for i in range(len(country)):
    if country[i] == "a":
        print(i)