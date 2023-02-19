# 1. Given an integer array nums, rotate the array to the right by k steps, where k is nonnegative
# def returnArray (k):
#     nums =  [1,2,3,4,5,6,7]
#     firstHalf = nums[slice(0, k)]
#     secondHalf = nums[slice(k, len(nums) - k)]
#     thirdHalf = nums[slice((len(nums) - k), len(nums))]
#     newNums = [*thirdHalf, *secondHalf, *firstHalf]
#     return newNums

# print(returnArray(3))


# 2. Given two integer arrays nums1 and nums2, return an array of their intersection. Each
# element in the result must be unique and you may return the result in any order.


# arr1 = [1,2,2,1,3]
# arr2 = [2,2,3]
# def getUniqArray (arr1, arr2):
#     arr3 = []
#     arr4 = []
#     for num in arr1:
#         if num  in arr2:
#             arr3.append(num)
#     for num in arr3:
#         if num not in arr4:
#             print(num)
#             arr4.append(num)
#     return arr4

# print(getUniqArray(arr1, arr2))