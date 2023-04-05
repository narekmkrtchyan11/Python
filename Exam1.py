# 1 Create a triangle

# def returnTriangle(height, symbol = '#'):
#     array = []
#     for i in range(1, height + 1):
#         array.append([symbol]*i)
#     return array
# print(returnTriangle(3))
# print(returnTriangle(2, '*'))

# 2 Greatest common divisor

arr = [2, 4, 6, 18]
def gcd(num1, num2):
    if (num2 == 0):
        return num1
    else:
         return gcd(num2, num1 % num2)

def getMaxDivisor(arr):
    max = arr[0]
    for i in arr[1:]:
        print(1111, i)
        max = gcd(max , i)
    return max

print(getMaxDivisor(arr))

# 3 Recursive Fibonacci

# count = 0
# def fibonacci(n):
#     global count
#     count += 1
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
        
# print(fibonacci(3))
# print(count)

# 4 Prime Factors
# def getPrimeFactors(number):
#     factors = []
#     for num in range(2, number + 1):
#         if number % num == 0:
#             count = 0
#             for i in range(1, num):
#                 if num % i == 0:
#                     count += 1
#             if count < 2:
#                 factors.append(num)
#     return list(set(factors))

# print(getPrimeFactors(100))

# 5 Jumping Frog

# def jumping_frog(P, h):
#     for i in range(1, len(P)):
#         if abs(P[i] - P[i - 1])  <= h:
#             continue
#         else:
#             return 'Game over'
#     return 'Frog wins'

# print(jumping_frog([4,5, 2], 3))

    

