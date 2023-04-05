# 2. Adding elements to dict

# def getNames(n, m):
#     dict = {}
#     for i in range(n):
#         text = input().split(' ')
#         dict[text[0]] = text[1]
#     for i in range(m):
#         possition = input()
#         print(dict[possition])
# getNames(5, 2)

# 3. Checking if the key is in the dict 
# text = input()

# def getMostCommon(text: str):
#     dict = {}
#     word = ''
#     for i in text.split(' '):
#         if i in dict:
#             dict[i] += 1
#             word = i
#         else:
#             dict[i] = 1
#     return word
# print(getMostCommon(text))


# 4. Shuffle the letters

# def isShuffle(text):
#     arr = text.split(' ')
#     arr1 = list(arr[0])
#     arr2 = list(arr[1])
#     arr1.sort()
#     arr2.sort()
#     return arr1 == arr2
        
# print(isShuffle('hello olleh'))


# 5. Safely accessing elements

# def getNames(n, m):
#     dict = {}
#     for i in range(n):
#         text = input().split(' ')
#         dict[text[0]] = text[1]
#     for i in range(m):
#         possition = input()
#         print(dict.get([possition], 'Not found'))

# getNames(5, 2)


