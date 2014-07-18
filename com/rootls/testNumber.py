# This Python file uses the following encoding: utf-8
__author__ = 'luowei'

print "Hello World !"

# 分组缩进
for i in range(20) :
    if i%3 == 0 :
        print(i)
        if i%5 == 0 :
            print "Hello"
print("----")


# 变量无需要声明
friendly = 1
if friendly: greeting = "hello world"
else:greeting = 12**2
print greeting


print(range(7))

# list的使用
a=[1,2,3]
b=a
a.append(4) # [0, 1, 2, 3, 4, 5, 6]
print  b    # [1, 2, 3, 4]

# 数字的使用
num1 = 1.5e3
num2 = 3.14e-2
longNum = 9999999999999999999L
print  num1,num2,longNum # 1500.0 0.0314 9999999999999999999
print 2**10  # 1024

