#按位与&   按位或|
#按位异或^
#按位取反~

#左移位<<  高位溢出抛弃，低位补0          value * 进制数的个数
#右移位>>  低位溢出抛弃，高位补原高位的数  value / 进制数的个数
print(3<<2)  #相当于3*2*2
print(32>>3)  #相当于（(32/2)/2）/2

a=12
a&=14
print(a)