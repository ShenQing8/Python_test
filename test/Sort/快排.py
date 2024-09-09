
# def qsort(nums):
#     left = 0
#     right = len(nums) - 1
#     if left == right:
#         return nums
#     std = nums[left]
#     nums[left] = None
#     while left < right:
#         if nums[left] is None:
#             while left < right and nums[right] > std:
#                 right -= 1
#             else:
#                 if left == right:
#                     nums[left] = std
#                     break
#                 nums[left] = nums[right]
#                 nums[right] = None
#                 left += 1
#         else:
#             while left < right and nums[left] <= std:
#                 left += 1
#             else:
#                 if left == right:
#                     nums[left] = std
#                     break
#                 nums[right] = nums[left]
#                 nums[left] = None
#                 right -= 1
#     nums = qsort(nums[0:left-1]) + nums[left] + qsort(nums[left+1:len(nums)-1])
#
# def test():
#     tt = [22, 5, 7, 3, 1, 88, 43, 486, 45, 5, 1, 86, 8, 4, 67, 64]
#     qsort(tt)
#     print(tt)
# test()

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)
# tt = [22, 5, 7, 3, 1, 88, 43, 486, 45, 5, 1, 86, 8, 4, 67, 64]
# tt = quick_sort(tt)
# print(tt)

















def qsort(arr):
    if len(arr) == 1:
        return
    left = 0
    right = len(arr) - 1
    std = arr[left]
    # while left < right:
    #     if arr[left] is None:
    #         while left < right and arr[right] > std:
    #             right -= 1
    #         else:
    #             if left == right:
    #                 arr[left] = std
    #                 break
    #             arr[left] = arr[right]
    #             arr[right] = None
    #             left += 1
    #     else:
    #         while left < right and arr[left] <= std:
    #             left += 1
    #         else:
    #             if left == right:
    #                 arr[left] = std
    #                 break
    #             arr[right] = arr[left]
    #             arr[left] = None
    #             right -= 1
    return qsort(arr[0:left]) + std + qsort(arr[left:len(arr)-1])

tt = [22, 5, 7, 3, 1, 88, 43, 486, 45, 5, 1, 86, 8, 4, 67, 64]
tt = qsort(tt)
print(tt)