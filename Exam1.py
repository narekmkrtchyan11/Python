# 1 Create a triangle

# def returnTriangle(height, symbol = '#'):
#     array = []
#     for i in range(1, height + 1):
#         arr = [symbol]*i
#         array.append(arr)
#     return array
# print(returnTriangle(3))

# 2 Greatest common divisor

# arr = [1, 2, 3, 4, 5, 6]
# def gcd (num1,num2):
#     if (num2 == 0):
#         return num1
#     else:
#          return gcd (num2, num1 % num2)

# def getMaxDivisor(arr):
#     max = arr[0]
#     for i in arr[1:]:
#         max = gcd(max , i)
#     return max

# print(getMaxDivisor(arr))

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

def jumping_frog(P, h):
    for i in range(1, len(P)):
        if P[i] - P[i - 1] == 2 or P[i] - P[i - 1] == -2:
            continue
        else:
            return 'Game over'
    return 'Frog wins'



print(jumping_frog([4,5, 2], 2))

    

