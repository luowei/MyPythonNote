# encoding: utf-8
__author__ = 'luowei'

# 定义一个类
class Stack:
    "常见的数据结构类"

    # 构造方法
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        x = self.items[-1]
        del self.items[-1]
        return x

    def empty(self):
        return len(self.items) == 0


x = Stack()
print x.empty()  # True
x.push(1)
print x.empty()  # False
x.push("hello")
print x.pop()  # hello


# 类的继承
class FancyStack(Stack):
    "类的继承示例"

    def peek(self, n):
        "peek(0) return top; peek(-1) returns item below "
        size = len(self.items)
        assert 0 <= n < size
        return self.items[size - 1 - n]


class LimitedStack(FancyStack):
    " fance stack with limit on stack size"

    def __init__(self, limit):
        self.limit = limit
        FancyStack.__init__(self)

    def push(self, x):
        assert len(self.items) < self.limit
        FancyStack.push(self, x)


class Connection:
    verbose = 0

    def __init__(self, host):
        self.host = host

    def debug(self, v):
        self.verbose = v

    def connect(self):
        if self.verbose:
            print " connecting to ", self.host

