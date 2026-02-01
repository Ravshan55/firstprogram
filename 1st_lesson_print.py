# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 18:46:57 2026

@author: xalil
"""
########## 1st lesson ############
#print("Hello world")
#print(8-7)

#print(" I am learning \"python\" programming language")

# There is a backslash sign (\"----\") which is used to run the stirng if there is anthor quotation mark in it. 
# To print the text in several lines we should use triple quotation marks ("""-----""") and divide the text according to selected sections.
#print(""" I am at the university library.
      #I am learning python programming from Mohir.dev""")
      
#Anthor the sign to divide the text into several lines is (\n).

#print("I am at the \nuniversity library. \nI am learning python programming \nfrom Mohir.dev")
##########2nd lesson Variables##############
# Varaiables are an imaginary box in which we contain different data.
# Variables should called with meaningful names.
# There are some specific words. They can be used as a variable name. 

#name="John"
#year=25

#name="Barry"
#year=27
#print(name)
#print(year)

########### 3rd Lessson Strings ############

#name="Jahn"
#surname="Terry"
#print(f"My full name is {name } {surname}")

#smile = "😂"
#print(smile)

#name= "Robin"
#surname="Hood"

#full_name=f"My name is {name} \t{surname}."
#print(full_name)

#There is a \t sign to put a big space between the specific words.

##### String methods ######

#name = "         billy james         "
#name1 = name.upper()
#print(name1)
#name2 = name1.lower()
#print(name2)
#name3 = name2.title()
#print(name3)
#name4 = name3.capitalize()
#print(name4)
#name5 = name4.lstrip()
#print(name5)
#name6 = f"My name is {name4.rstrip()}"
#print(name6)
#name7 = f"My name is {name.strip().title()}." 
#print(name7)

#name = input("What is your name?\n")
#print(f" Hello {name.strip().title()}.")

############# 4th Numbers ##############
#a = 20
#b = 4.5

#c=b*a
#print(c)



#name = input("What is your name?")
#age = int(input("How old are you?"))

#details = name + " is " + str(age) + " years old."
#print(details)

############ 5th List ###############

students = ["John", "Ron", "Harry", "Emma"]
marks = [5, 6, 9, 8]

students[0] = "Draco"
#print(students)

#print(students[-1].upper())

#print(students[2].title())
#print(marks[0]+marks[-2])

#print(students)

#append() method adds value at the end of the list

students.append("John")
#print(students)

# insert(index, object) method adds value in any order of the list.

students.insert(2, "Jeremy")
students.insert(4, "Su")
#print(students)

fruits = []

fruits.append("banana")
fruits.append("apple")
fruits.append("cherry")
fruits.append("peach")
#print(fruits)

# del deletes a value according to the index of list items
#del fruits[1]
#print(fruits)

# remove deletes any value of list according to the value name and deletes the first element


fruits.remove("peach")
#print(fruits)

# list.pop(index) is used to extract a value from the list according to an index. If index is not shown the last element is extracted and creates new variable.

#print(students)

student = students.pop(3)
#print(student)

############ List methods ###########

# sort() method is used to order values in an alphabetical order.
# This method is applied to both strings and numbers
# sort(reverse=True) is used to order values from back order.
# sorted(variable) is used to order values without change order.
# reverse() is used to turn around the list
# len(variable) is used t measure the length of list. You can save the length
# to a new variable
# range(1,10) this method is used to count the numbers one to another one number.
# max() this is used to find maximum amount out of list numbers 
# min() this is used to find minimum amount out of list numbers
# list_name[0:0] is used to cut the list based on the index of list items
# new_list_name = list_name[:] copying list is done with cutting method new_list_name = list_name[:]

#footballers = ["Messi", "Ronaldo", "Neymar", "Xavi", "Drogba", "Ramos", "Puyol"]
#new_footballers = footballers[:]
#new_footballers.append("Prilo")

#print(new_footballers)
#print(footballers)


#odd_umbers = list(range(1, 50,  2))
#even_numbers = list(range(0, 50, 2))

#max_amount = max(even_numbers)

#print(max_amount)

#footballers.sort()
#footballers.sort(reverse=True)
#print(sorted(footballers))
#print(sorted(footballers, reverse=True))
#footballers.reverse()
#footballers2 = len(footballers)

#print(footballers2)

#prices = [100, 10, 50.78, 5, -98, 304]

#prices.sort()
#print(prices)

###### TUPLES ########

# TUPLES are unchangeable list of items. tuple_name("element", "element"...)
# We cannot change tuples, but if we need first we have to change tuple
# into list with list_name = list(tuple_name) and make changes and again turn
# list_name into tuple with tuple_name = tuple(list_name)

#footballers = ("Messi", "Ronaldo", "Neymar", "Xavi", "Drogba", "Ramos", "Puyol")

#footballers1 = list(footballers)

#footballers1.append("Bale")
#footballers = tuple(footballers1)

#print(footballers)



############## For Loop #################

# footballers = ["Messi", "Ronaldo", "Neymar", "Xavi", "Drogba", "Ramos", "Puyol"]
# #for footballer in footballers:
# #    print(f"I am {footballer}.")

# numbers = list(range(1,11))
# for number in numbers:
#     print(f"{number} * {number} = {number*number}")
# print(numbers)

# numbers = list(range(1,20))
# minus_one = []

# # for number in numbers:
# #     minus_one.append(f"{number - 1} subtracted") 
      
# # print(numbers)
# # print(minus_one)



# students = []
# print("Enter students' names")

# for student in range(5):
#     students.append(input(f"Enter {student+1} name."))
    
# print(students)
 
########### if/else ###########

#To compare strings first we should make the same as the strings that we want to
# to compare
# We can check length of value with len(variable_name)
# We can write if and else in the same line.


# footballers = ["Messi", "Ronaldo", "Neymar", "Xavi", "Drogba", "Ramos", "Puyol"]
    
# for footballer in footballers:
#     if footballer == "Messi":
#         print(f"{footballer.upper()} is legend of Barcelona.")
#     elif footballer == "Ronaldo":
#         print(f"{footballer.upper()} is legend of Real Madrid.")
#     else:
#         print(f"{footballer} is a legend.")
    
# name = input("What is your name? \n:")

# if name.lower() != "john":
#     print(f"Hello {name.title()}, this is not your account.")
# else:
#     print(f"Hello, {name.title()}!")

# login = input("Enter your login:")

# if len(login) <= 8:
#     print("Login should be more than 8 characters!")

# name = input("What is your name?")
# age = int(input("Enter your age:"))

# if age <= 18:
#     print(f"Dear, {name}. You cannot drive a car!")
# else:
#     print(f"{name} you can drive.")


########## if elif else ################

## to check every line of code we should use if condition every time.
## input_info in list_name checks items of the list. If the item is on the list
## it returns TRUE we can use it in our condition.
## opposite of input_info not in list_name

# price = int(input("How much is it?\n"))

# if price <= 10000:
#     print (f"${price} is cheap.")
# elif price  <= 15000:
#     print (f"${price} is normal.")
# else:
#     print(f"${price} is unaffordable.")
    
# day = input("What is a day today?")
# weekdays =["monday", "tuesday", "wednesday", "thursday", "friday"]


# if day.lower() == "saturday" or day.lower() == "sunday":
#     print("Today stay at home!")
# elif day.lower() in weekdays:
#     print( "You should go to work!")

# else:
#     print("Enter weekdays name!")

## 1st exercise ##
# number = int(input("Enter even number!"))

# if number % 2 != 0:
#     print("This is not an even number")
# else:
#     print("Thank you")
    
## 2 exercise ##
# age = int(input("Enter your age!"))

# if age <=4 or age> 60:
#     print("You do not have to pay!")
# elif age <=18 and age > 4:
#     print("The ticket price is 10000 for you!")
# else:
#     print("You should pay 20000!")

## 3 exercise ##

# number = float(input("Enter number 1:"))
# number1 = float(input("Enter number 2:"))

# if number < number1:
#     print(f"{number} < {number1}")
# else:
#     print(f"{number} > {number1}")

## 4 exercise ##

# goods =["banana", "apple", "orange", "cherry", "grape", "kiwi", "avacado","mango", "easy peelers", "plums"]
# basket=[]

# for x in range(5):
#     basket.append(input("Enter 5 fruits: >>>"))

# basket in goods

# if basket[0] not in goods:
#     print(f"{basket[0]} is not available")
# if basket[1] in goods:
#     print(f"{basket[1]} is available")
# if basket[2] in goods:
#     print(f"{basket[2]} is available")
# if basket[3] not in goods:
#     print(f"{basket[3]} is not available")
# if basket[4] not in goods:
#     print(f"{basket[4]} is not available")
    
## 5 exercise ##
# goods =["banana", "apple", "orange", "cherry", "grape", "kiwi", "avacado","mango", "easy peelers", "plums"]
# basket =[]

# for x in range(5):
#     basket.append(input(f"Enter  good {x+1}: >>>"))

# available_goods=[]
# not_goods = []

# for x in basket:
#     if x in goods:
#         available_goods.append(x)
#     else:
#         not_goods.append(x)

# if not_goods:
#     print("The follwing goods are not available:")
#     for x in not_goods:
#         print(x)
# else:
#     print("All goods are available.")


## 6 exercise ## 

# users = ["john", "alex", "ben", "marcus", "chad"]
# new_login = input("Enter new login! >>>")

# if new_login.lower() in users:
#     print("Login is occupied. Please choose another one!")
# else:
#     print(f"Welcome, {new_login.title()}")

## 7 exercise ## 
number = int(input("Enter intiger number! >>>"))

for x in range(2,11):
    if not (number%x):
        print(f"{number} is diveded by {x} without remainder!")



