def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def quick_sort2(arr):
    if len(arr) <= 1:
        return arr
    mid = [arr[0]]
    left = []
    right = []
    for i in arr[1:]:
        if i < mid[0]:
            left.append(i)
        elif i > mid[0]:
            right.append(i)
        else:
            mid.append(i)
    return quick_sort2(left) + mid + quick_sort2(right)

def quick_sort3(arr):
    if len(arr) <= 1:
        return arr
    left = 0
    right = len(arr) - 1
    std = [arr[left]]
    while left < right:
        while left < right and arr[right] > std[0]:
            right -= 1
        if left == right:
            arr[left] = std[0]
            break
        else:
            arr[left] = arr[right]
            left += 1
        while left < right and arr[left] < std[0]:
            left += 1
        if left == right:
            arr[left] = std[0]
            break
        else:
            arr[right] = arr[left]
            right -= 1

    return quick_sort3(arr[0:left]) + std + quick_sort3(arr[left + 1:len(arr)])

tt = [22, 5, 7, 3, 1, 88, 43, 486, 45, 5, 1, 86, 8, 4, 67, 64]
tt = quick_sort(tt)
print(f' quick_sort排序后的顺序是：{tt}')
tt = [22, 5, 7, 3, 1, 88, 43, 486, 45, 5, 1, 86, 8, 4, 67, 64]
tt = quick_sort2(tt)
print(f'quick_sort2排序后的顺序是：{tt}')
tt = [22, 5, 7, 3, 1, 88, 43, 486, 45, 5, 1, 86, 8, 4, 67, 64]
tt = quick_sort3(tt)
print(f'quick_sort3排序后的顺序是：{tt}')

