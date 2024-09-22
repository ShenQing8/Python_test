a = 100
b = 50
print(50)
print(a)
print(a*b)
print("a*b")
# def test(nums):
#     # if len(nums) == 0:
#     #     return None
#     if nums == []:
#         return None
#     left = 0
#     right = len(nums) - 1

nums = [1,2,3,4,5,6,7]
print(f'{nums[0:5]},{type(nums[0:5])}')
print(f'{nums[0:2]+nums[3:5]},{type(nums[0:2]+nums[3:5])}')

k = [x*y for x in range(1,5) if x > 2 for y in range(1,4) if y < 3]
print(k)

s, p = (input()).split(' ')
s = int(s)
p = int(p)
print(s, p,type(s), type(p))
