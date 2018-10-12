#I pushed this to git!
# variables
# A variable is something that can change based on information inside the program

# Mild
# write any variable
# my_name == "nick"

# Medium
# 

#Spicy
#

# arrays
# An array is a set of anything like numbers, names, animals, etc

# Mild
# create an array
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Medium
# print the array you created
# print(arr)
# Spicy
# print out the array backwards

# if/else statements
# if...:(press enter key)
#   (statement1)
# else:
#   (statement2)

# Mild
# input "truth or dare"
# return "truth" or "dare"
# ans = input("truth or dare?")
# Medium
# get computer to give a question based on choice of "truth" or "dare"
# ans = input("truth or dare?")
# if ans == "truth":
#    question1 = input("have you ever failed a class?")
# elif ans == "dare":
#    question2 = input("throw paper towels around the room")
#Spicy
# play a full game of truth or dare with the computer
# if ans == "truth":
#    question1 = input("have you ever failed a class?")
#    if question1 == "yes":
#        print("that's not good")
#    else:
#        print("so have i")
# elif ans == "dare":
#    question2 = input("throw paper towels around the room")
#    if question2 == "ok":
#        print("you're going to get in so much trouble")
#    else:
#        print("that was hilarious")

# for loops are used to iterate over a sequence
# for...in...:
#   (variable)

# Mild
# using the array you made earlier, print it out using a for loop
# for x in arr:
#    print(x)
# Medium
# create a new array with words and print out one word letter by letter
# arr2 = ["book", "seed", "cat", "dog"]
# for x in "book":
#    print(x)
# Spicy
# using the range function, go through the range of 11
# for x in range(11):
#    print (x)

# nesting
# define function, loops can be within loops
# def (function):
# (loops)

# Mild
# create a nested loop using a for loop
# def nested(arr):
#    for num in arr:
#        print(num)
# nested(arr)
# Medium
# create a nested loop using a while loop
# def backwards(arr):
#    new_arr = []
#    pos = 1

#    while pos < len(arr):
#        last = arr.pop()
#        new_arr.append(last)
#    print(new_arr)
# read = ["book", "seed", "cat", "dog"]
# backwards(read)

# a method is a function that "belongs" to something
# def (backwards)
# ...
# ...
# call function

# Mild
# using a new, smaller array, start with defining your function and make the beginning of a compare statement
# my_list = [1, 2, 3, 4]
# def most_freq(arr):
#    count = 0
#    ans = 0
#    for outter in arr:

# Medium
# make two loops compare to one another

# def most_freq(arr):
#    count = 0
#    ans = 0

#    for outter in arr:
#       for inner in arr:
# Spicy
# find the most frequent number in array
# def most_freq(arr):
#    count = 0
#    ans = 0
#    for outter in arr:
#           if inner == outter:
#                count = count + 1
#    if count > 1:
#        ans = count
#
#    print(count)
#
# most_freq(my_list)
