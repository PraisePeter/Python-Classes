# lang = input("What is the programming language, you want to learn?")
#
# if lang.lower() == "javascript":
#     print("You can become a web developer")
# elif lang.lower() == "python":
#     print("You can become a Data Scientist")
# elif lang.lower() == "php":
#     print("You can become a backend developer")
# elif lang.lower() == "solidity":
#     print("You can become a Blockchain Developer")
# elif lang.lower() == "java":
#     print("You can become a mobile app developer")
# else:
#     print("The language doesn't matter, what matters is solving problems.")


lang = input("What is the programming language, you want to learn?")

#Using match and case statements
match lang:
    case "javascript":
        print("You can become a web developer")
    case "python":
        print("You can become a Data Scientist")
    case "php":
        print("You can become a backend developer")
    case "solidity":
        print("You can become a mobile app developer")
    case "java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")


