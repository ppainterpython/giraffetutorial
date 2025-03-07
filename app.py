from math import *

print("Hello World")
print("")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
print("")
print("There once was a man named George,")
print("he was 70 years old.")
print("He really liked the name George,")
print("but didn't like being 70.")
print("")

# Variable basics
# Python basic data types: string, numbers and boolean
print("Working with variables")
character_name = "John"
character_age = "35"
print("There once was a man named " + character_name + ",")
print("he was " + character_age + " years old.")
character_name = "Mike"
character_age = "40"
is_Male = True
print("He really liked the name " + character_name + ",")
print("but didn't like being " + character_age + ".")
print("")
print("Working with strings")
print("Giraffe Academy")
phrase = "Giraffe Academy"
print(phrase)
print(phrase.lower())
print(phrase.upper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0]) # G - first character of a string, 0-based
print(phrase[5]) # f - 5th character index
print(phrase.index("ff")) # returns 4
print(phrase.replace("ff", "gg")) # returns Giragge Academy
print("")
print("Working with Numbers")
print(2)
print(2.0987)
print(3 + 4.5)
print ((3 *4 ) + 5)
print (10 % 3) # modulus operator, the remainder
my_num = 5
print("my_num = " + str(my_num)) # convert number to string
print("abs(my_num) = " + str(abs(my_num)))
print("pow(my_num,2) = " + str(pow(my_num,2)))
print("max(4,2) = " + str(max(4,2)))
print("min(4,2) = " + str(min(4,2)))
print("round(4.5) = " + str(round(4.5)))
print("round(4.6) = " + str(round(4.6)))
# after import math
print("sqrt(4.6) = " + str(sqrt(4.6)))
print("sqrt(4) = " + str(sqrt(4)))
print("")
print("Getting input from a user")
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "!, aged " + str(age))

print("")
print("Building a Basic Calculator")
# by default, input is converted to a string
# num1 = input("Enter an integer: ")
# num2 = input("Enter another integer: ")
# result = int(num1) + int(num2) # int() is integer only
# print(result)

# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + float(num2)
# print(result)

print("")
print("Building a Mad Libs Game")
# color = input("Color: ")
# plural_noun = input("Plural Noun: ")
# celebrity = input("Celebrity: ")
# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

print("")
print("Working with Lists (Arrays)")
friends = ["Paul","Laura", "Kyle", "Darryl"]
print(friends)
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[-1]) # index from end of list, the back
print(friends[1:]) # Kyle, Darryl
print(friends[0:2])
friends[2] = "Tommy"
print(friends)
print("")
print("Working with List Functions")
friends = ["Paul", "Laura", "Kyle", "Darryl", "Tommy", "Roop"]
lucky_numbers = [4,8,15,16,23,42]
print(friends)
print(lucky_numbers)
# extend function
friends.extend(lucky_numbers)
print(friends)
friends.append("Creed") # add to end of list
print(friends)
friends.insert(1,"Kelly")
print(friends)
friends.remove("Kelly")
print(friends)
# friends.clear() # empty list
print(friends.pop()) # removes and returns last element from list
print(friends)
friends_sort = ["Paul", "Laura", "Kyle", "Darryl", "Tommy", "Roop"]
friends_sort.sort()
print(friends_sort)
print("")
print("Working with Tuples")
# tuples are immutable
coordinates = (4,5)  # parens for tuples
print(coordinates[0])
coordinates = [(4,5), (6,7), (80, 34)]
print(coordinates)
print("")
print("Working with Functions")
def sayhi(name,age):
    # lines of a function are indented
    # in this example, input parameters are not typed, will assume type of data passed
    # This is assuming the input is a number
    print("Hello " + name + " age: " + str(age))
# end of function
print("top")
sayhi("Paul",66)
print("bottom")
print("")
print("Working with Return Statement in Functions")
def cube(num):
    return num*num*num

result = cube(4)
print(cube(3))
print(result)

print("")
print("Working with If statements")
is_male = True
is_tall = True
if is_male:
    print("You are a male")
else:
    print("You are not a male")
is_male = False
if is_male:
    print("You are a male")
else:
    print("You are not a male")

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither tall or male")
is_male = True
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not is_tall:
    print(" You are maile but not tall")
elif not is_male and is_tall:
    print("You are not male but are tall")
else:
    print("You are either not tall or not male or both")
print("")
print("Working with If Statements and Comparison Operators")
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print("max_num(3,4,5) = " + str(max_num(3,4,5)))
print("max_num(3,6,5) = " + str(max_num(3,6,5)))
print("")
print("Building a Better Calculator")



