"""
python的包
包就是一个文件夹，里面有python的代码模块，通过包来对代码模块进行分类与管理
__init__.py 的作用：来表示这是一个包，而不是普通的文件夹，
同时，可将__all__定义的列表放在__init__.py里
"""

# import Sort.quick_sort
# arr = [2, 58, 9, 3, 47, 8, 31, 6, 8, 78, 19, 64, 45, 356, 1, 35, 56, 48, 12, 4,]
# arr = Sort.quick_sort.quick_sort3(arr)
# print(arr)

from Sort import quick_sort
arr = [2, 58, 9, 3, 47, 8, 31, 6, 8, 78, 19, 64, 45, 356, 1, 35, 56, 48, 12, 4,]
arr = quick_sort.quick_sort2(arr)
print(arr)
