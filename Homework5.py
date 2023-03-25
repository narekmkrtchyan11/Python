# 1. Smallest divisor of n

# def smallestDivisor(num):
#     for n in range(1, num):
#         if num % n == 0 and n != 1:
#             return n
# print(smallestDivisor(385))

# 2. Infinite loop 

# arr = []
# while True:
#     n = int(input())
#     arr.append(n)
#     if(n == 0):
#         print(arr.count(max(arr)))
#         break

# 3. continue

# arr = [12, 9, 6, 0, 1, -1, 41, 28, 27, 17]
# def printOdds(numbers):
#     for el in numbers:
#         if(el % 2 != 0 and el < 3 or el > 7 and el < 11 or el > 13 and el < 17 or el > 23):
#             print(el)
#         else:
#             continue

# printOdds(arr)

# 4. Google is the king 

# def findWords(string: str) -> int:
#     arr = string.split()
#     return len(arr)

# print(findWords('ed, frfrf/ effrfrfr'))

# 5. split() 

# def printWords(string):
#     arr = string.split()
#     for word in arr:
#         print('\n' + word)
# print('hello world')

# 6. Windows to Linux 

# def changePath(path):
#     os.path.split(path)
#     words = path.split('\')
#     print(words)
#     words[0] = '/home'
#     return '/'.join(words)

# print(changePath('C:\dddd\dffrf\rfrfr\rfrf'))

# 9. swap min & max 
# arr = [5, 1, 0, 3, 4, -1]

# def changeOrder(arr: list) -> list:
#     minimum = min(arr)
#     minIndex = arr.index(minimum)
#     maximum = max(arr)
#     maxIndex = arr.index(maximum)
#     arr.remove(maximum)
#     arr.remove(minimum)
#     arr.insert(minIndex, maximum)
#     arr.insert(maxIndex, minimum)
#     return arr

# print(changeOrder(arr))

# 10. Triangle of numbers 

# n = 6
# def triangleNumbers(n: int):
#     for i in range(1, n + 1):
#         triangle = ''
#         for x in range(1, i + 1):
#             triangle += str(x)
#         print(triangle)

# triangleNumbers(n)

# 11. Double sorting

# arr = [34, 65, 99, 10, 22]

# def doubleSorting(arr: list) -> list:
#     arr.sort()
#     for num in arr:
#         b = list(str(num))
#         arr.clear()
#         for i in range(0, len(b) - 1):
#             if b[i + 1] < b[i]:
#                 b.insert(i, b[i + 1])
#             arr.append(''.join(b))
#     return arr


# print(doubleSorting(arr))

# 12. Is the matrix symmetric? 
# n = int(input())
# matrix = []
# for i in range(n):
#     eachRow = list(map(int, input().split()))
#     matrix.append(eachRow)

# print(matrix)
# n = 3
# matrix = [[123], [456], [789]]


# isSymmetric = bool
# for i in range(0, n):
#     for j in range(0, n):
#         print(i, j)
#         if matrix[i][j] != matrix[j][i]:
#             isSymmetric = False
#             break
#     if not isSymmetric:
#         break

# if isSymmetric:
#     print("yes")
# else:
#     print("No")

# 13. List comprehensions: Squares in a range 

# def getQuatos(num1, num2):
#     for n in range(num1, num2 + 1):
#         print(n ** 2)
# getQuatos(3, 7)

# 14. The square root of numbers

# import math

# def getRoots(arr: list) -> list:
#     newArr = []
#     for num in arr:
#          newArr.append(math.sqrt(num))
#     return newArr
# print(getRoots([3, 7, 9, 16]))


# 15. Filtering in a list comprehension 
# arr = [1, 2, 3, 4]

# def b(n):
#     if n % 2 == 0:
#         return True
#     return False
# a = list(filter(lambda n: n % 2 == 0, arr))
# print(a)


# 16. Nested list comprehension 

# arr = ['A', 'B', 'C', 'D']

# for i in range(1, 9):
#     string = [ str(let) + str(i) for let in arr]
#     print(string)
# def getTuple(n):
#     arr = []
#     for i in range(n):
#         string = input()
#         arr.append(string)
#     return tuple(arr)

# print(getTuple(4))


# 19. set

# def getUniq(n):
#     arr = []
#     for i in range(n):
#         string = input()
#         arr.append(string)
#     return set(arr)
# print(getUniq(4))



