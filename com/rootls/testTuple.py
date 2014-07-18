# encoding:utf-8
__author__ = 'luowei'

# tuple(元组)是不可变的，长度与值是不可伸缩与变化的

t1 = (0,1,2,3);t2 = (4,5,6)
t3 = (0,1,(2,3),'three',('four,one'))
t4 = ()
print t1+t2 # (0, 1, 2, 3, 4, 5, 6)
print t1*2 # (0, 1, 2, 3, 0, 1, 2, 3)
print t3 # (0, 1, (2, 3), 'three', 'four,one')
print t3.index("three") # 3
