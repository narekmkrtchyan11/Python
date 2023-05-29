# 1. Arithmetic operations with several numbers
# Just like programs with several print() statements, we can have several input()
# statements as well.
# Your task is to read 3 integer numbers from the input and print their sum in the output

# def getSum(a:float, b:float, c:float) -> float:
#     return(a + b + c)
# a = float(input())
# b = float(input())
# c = float(input())

# print(getSum(a, b, c))


# 2. Geometric progression 

# def getElement(b1: float, q: float, n: int)-> float:
#     Bn = b1 * (q ** (n - 1))
#     return Bn
# print(getElement(95, 3, 2))



# 3. Odd or even
# Given an integer, your task is to determine if it’s odd or even. The program should print The
# number <NUMBER> is <odd/even>

# def checkNum(n: int) -> str: 
#     return f'{n} is even' if n % 2 == 0 else f'{n} is odd' 

# print(checkNum(0))

# 4. Is this an arithmetic progression?
# Given 3 numbers a, b and c your task is to determine if those 3 numbers could form an
# arithmetic progression. Print arithmetic progression in case those 3 numbers could be part of
# an arithmetic progression and no pattern found otherwise.

# def isArithmaticProgression(*args:tuple) -> float:
#     ls = list(args)
#     ls.sort()
#     const = ls[1] - ls[0]
#     for i in range(len(ls)-1):
#         if ls[i+1] - ls[i] != const:
#             return False
#     return True

# print(isArithmaticProgression(2,4,6,8,10,11))

# 5. Good numbers 
# def GoodNum(num:int) -> bool:
#     if len(str(num)) == 3 or num % 7 != 0 or num % 23 != 0:
#         return False
#     return True
# print(GoodNum(161))

# 6. Quadratic equations 

# def quadraticEquations(a: float, b: float, c: float) -> str or float:
#     D = (b ** 2) - (4 * a * c)
#     if D > 0:
#         x1 = ((-b) +  (D ** 0.5) ) / (2 * a)
#         x2 = ((-b) -  (D ** 0.5)) / (2 * a)
#         return (x1, x2)
#     elif D == 0:
#         x = -b / 2 * a
#     return 'no solution'
# print(quadraticEquations(48, 58, 5))
4

# # 8. Multiples of n
# def mul_n(n:float) -> list:
#     for i in range(1,11):
#         print(f"{n} * {i} = {i*n}")
# mul_n(7)

# 9. Inputting list 
# def inputting_list(n:int) -> list:
#     ls = []
#     for i in range(n):
#         a = int(input())
#         ls.append(a)
#     return ls
# print(inputting_list(int(input())))

# 10. Divisors of n 

# def getDivisors(number: int):
#     for n in range(1, number + 1):
#         if number % n == 0:
#             print(n)

# getDivisors(16)

# 13. Factorial 

# def factorial(n: int) -> int:
#     if n == 1:
#         return n
#     return n * factorial(n - 1)

# print(factorial(5))

# 14. Squares

# def squares(num: int):
#     for n in range(1, num + 1):
#         if n ** 2 <= num:
#             print(n ** 2)

# squares(16)

# 15. Powers of 2 

# def powersOf2(num: int):
#     arr = []
#     curr = int
#     for n in range(0, num):
#         if 2 ** n <= num:
#             arr.append(2 ** n)
#             curr = 2 ** n
#     return arr

# print(powersOf2(51))

# 16. Is it a power of 2?

# def isPowerOf2(num: int):
#     while num != 1:
#         if num % 2 == 0:
#             num = num / 2
#     return True if num == 1 else False

# print(isPowerOf2(3))


# 18. Sum of negatives 

# def getSum(numbers):
#     sum = 0
#     for i in numbers:
#         if i < 0:
#             sum += i
#         else:
#             return sum

# a = (-1, -2, 0, -3)

# print(getSum(a))

# 19. Reverse the number 

# def reverse(num: int) -> int:
#     array = str(num)
#     arr = []
#     for i in range(len(array)):
#         arr.append(array[len(array) - 1 - i])
#     return int("".join(arr))

# print(reverse(123))

# 20. Are digits non-decreasing? 

# def decreasing (num):
#     array = str(num)
#     for i in range(1,len(array)):
#         if array[i] < array[i - 1]:
#             return False
#     return True

# print(decreasing(14234))
