# encoding:utf-8
__author__ = 'luowei'

# list是可变的，长度可增可减
list1 = [0,1,2,3]
list2 = ['zero','one']
list3 = [0,1,[2,3],'three',['four,one']]
list4 = []

print list1 # [0, 1, 2, 3]
list1[0] = 100
list1[1] = "abc"
print list1 # [100, 'abc ac', 2, 3]

print list3[2][1] # 3
print list3[1:3] # [1, [2, 3]]
l1 = list3[0:2]
l2 = list3[3:5]
print l1+l2 # [0, 1, 'three', ['four,one']]
print list3[2:4]*2 # [[2, 3], 'three', [2, 3], 'three']

list3.append("hello world")
print list3 # [0, 1, [2, 3], 'three', ['four,one'], 'hello world']

list2.insert(1,"second")
print list2 # ['zero', 'second', 'one']
list2.extend(["two","element"]) # ['zero', 'second', 'one', 'two', 'element']
print list2
print list2.index("two") # 3

#排序
list3.sort()
print list3 # [0, 1, [2, 3], ['four,one'], 'hello world', 'three']

#反转
list1.reverse()
print list1 # [3, 2, 'abc', 100]

# shrinking（删除、收缩)
del list1[2]
print list1 # [3, 2, 100]
list1[0:2] = []
print list1 # [100]

# index and slice assignment
list1[0] = 0
list1[1:4] = [4,5,6]
print list1 # [0, 4, 5, 6]

# making a list of integers
print range(4) # [0, 1, 2, 3]
print range(1,5) # [1, 2, 3, 4]

