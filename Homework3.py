# 1. Write a Python program to find out what version of Python you are using.
# from platform import python_version
# print(python_version())
# import sys 
# print("Python version") 
# print (sys. version) 
# print("Version info.") 
# print (sys. version_info)

# 2.Write a Python program to display the current date and time.
# Sample Output :
# Current date and time 
# 2014-07-05 14:34:14

# from datetime import datetime
# print(datetime.now())

# 3.Write a Python program that calculates the area of a circle based on the radius entered by
# the user. (Use input() to solve this task)
# import math
# p = 3.14
# R = float(input())
# area = math.pow(R, 2) * p
# print(area)

# 4.Write a Python program that accepts a filename from the user and prints the extension of
# the file.

# fileName = 'abc.java'
# extension = fileName.split('.')
# print(extension[1])

# 5. Write a Python program to display the first and last colors from the following list.

# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0], color_list[len(color_list) - 1])

# 6.Write a Python program to display the examination schedule. (extract the date from
# exam_st_date).

# exam_st_date = 11,12,2014
# print( "The examination will start from : %i / %i / %i" %exam_st_date)

# 7. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

# n = 5
# nn = int("%i%i" %(n,n))
# nnn = int("%i%i%i" %(n,n,n))
# print(n + nn + nnn)

# 8.Write a Python program that determines whether a given number (accepted from the user)
# is even or odd, and prints an appropriate message to the user.

# n = 2
# print("even" if n % 2 == 0 else 'odd')


# 9.Write a Python program that checks whether a specified value is contained within a group
# of values. 

# n = 6
# array = [1,2,3,4]
# print('yees' if n in array else 'no')

# 10.Write a Python program to create a histogram from a given list of integers.
# Input: [2, 3, 6, 5]

# arr = [2, 3, 6, 5]
# for n in arr:
#         output = ''
#         while( n > 0 ):
#           output += '*'
#           n -= 1
#         print(output)


# 11. Write a Python program that prints out all colors from color_list_1 that are not present in
# color_list_2.

# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# for color in color_list_1:
#     if color not in color_list_2:
#         print(color)

# 12. Write a Python program that concatenates all elements in a list into a string and returns it.

# array = [1,2,3,4,5,6]
# text = ''
# for el in  array: 
#     text += str(el)
# print(text)

# 13. Write a Python program that computes the greatest common divisor (GCD) of two positive 
# import math
# num1 = 10
# num2 = 5
# num = max(num1, num2)
# divisor = int

# print(divisor)
# for n in range(1, num):
#     if num1 % n == 0 and num2 % n == 0:
#         divisor = n
# print(divisor)

# 14. Write a Python program to find the least common multiple (LCM) of two positive integers.

# num1 = 2
# num2 = 5

# lcm = float

# for n in range(1, num1 * num2 + 1):
#     if n % num1 == 0 and n % num2 == 0:
#         lcm = n
# print(lcm)

# 16. Write a Python program to check whether a file exists. (Use os package)
# import os.path
# print(os.path.exists('Homework3.py'))

# 36. Write a Python function that takes a positive integer and returns the sum of the cube of all
# positive integers smaller than the specified number. 


# def getSum (num):
#     sum = 0
#     for i in range(1, num):
#         sum += pow(i, 3)
#     return sum

# print(getSum(8))


# 35Write a Python function to find the maximum and minimum numbers from a sequence of numbers

# nums = [1,2,3,4,5,6]
# def getNumbers (nums):
#     min = nums[0]
#     max = nums[0]
#     for n in nums:
#         if n > max:
#             max = n
#         elif n < min:
#             min = n
#     return min,max

# print(getNumbers(nums))

# 33. Write a Python program to convert true to 1 and false to 0.
# x = 'true'
# x = int(x == 'true')
# print(x)
# x = 'false'
# x = int(x == 'true')
# print(x)

    