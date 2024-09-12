from my_utils import str_util
from my_utils import file_util

my_str = "123456"
my_str = str_util.str_reverse(my_str)
print(my_str)
my_str = str_util.substr(my_str,0,3)
print(my_str)

file_util.append_to_file("D:/github Code/乱码.txt","\nbkjD?LJD4136$#!R%TY!UE")
file_util.print_file_info("D:/github Code/乱码.txt")

