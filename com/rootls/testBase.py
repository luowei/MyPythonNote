# encoding: utf-8
__author__ = 'luowei'

# python 的statements 与 funcitons的使用

# if elif else的使用
condition1 = False
condition2 = True
if condition1:
    print "condition1..."
elif condition2:
    print "condition2..."
else:
    print "Others...."

# or条件的使用
if condition1 or condition2:
    print "condition1 or condition2 ..."

# in的使用(多个语句在同一行时，用分号";"隔开)
x=2;y=3;L=[0,1,2]
if (1<x<=3 and 4>y>=2) or (1==1 or 0!=1) or 1 in L:
    print "Hello World ..."

# while的使用
x=1
while x<4:
    print x**2
    x=x+1

# for 的使用
for i in range(1,7):
    print i,i**2,i**3,i**4

L=[0,1,2,3]
for i in range(len(L)):
    L[i] = L[i]**2
print L # [0, 1, 4, 9]


# function的使用
def f1(x):
    return x*(x+1)
print f1(3) # 12

def f2(func,list,x):
    L=[]
    for i in range(len(list)):
        L.append(func(x+list[i]))
    return L
L1=[0.0,0.1,0.2,0.3]
L=f2(f1,L1,0.5)
print L # [0.75, 0.96, 1.19, 1.4400000000000002]

# Multiple Assignment
x,y = 2,3
print x # 2
print y # 3

def gcd(a,b):
    "greatest common divisor"
    while a != 0:
        a,b = b%a,a # parallel assignment
    return b

print gcd(36,96) # 12

execfile('helloworld.py') # hello world !

# 异常处理
try:
    f = open("foo")
except IOError:
    print "Couldn't open 'foo'. Sorry"
# finally:
    # f.close()   # always executed

def factorial(n):
    if n < 0:
        raise ValueError,"Expected non-negative number"
    if(n<=1):return 1
    else:return  n*factorial(n-1)

try:
    factorial(-1)
except ValueError:
    print "get exception..."

