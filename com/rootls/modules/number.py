# encoding: utf-8
__author__ = 'luowei'

# 除，返回商，余数
def divide(a, b):
    q = a / b
    r = a - q * b
    return q, r

# 最大公约数
def gcd(x, y):
    g = y
    while x > 0:
        g = x
        x = y % x
        y = g
    return g

