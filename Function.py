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
fancy_print('Hi', style='bold')
fancy_print('Hi', color='yellow', background='black')
fancy_print('Hi')



def multiple_print(name, n=2):
    print("Name", name)
    print("Number of times", n)
    print("*" * 30)
    #print(f' our text is "{text}", {color}')
#FUNCTION CALLS
multiple_print("Praise", n=5)
multiple_print("Ego", n=7)
multiple_print("Praise")


# def fancy_print(text, color='black', background='white'):
#     print(f' Our text is "{text}", the color is {color}, the background is {background}')
# # Function calls
# fancy_print(color="white", background="black", text="Praise")
#


