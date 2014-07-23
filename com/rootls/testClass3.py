# encoding: utf-8
__author__ = 'luowei'


# 类变量定义在类的定义之后，实例变量则是以为self.开头
# 实例也能够访问类变量
class Foo(object):
    val = 0
    def __init__(self):
        self.val = 1
if __name__ == '__main__':
    foo = Foo()
    print foo.val # 1
    print Foo.val # 0

# 另外，可以通过以下方式访问类变量
class Foo2(object):
    val = 3
    def __init__(self):
        print self.__class__.val # 3
if __name__ == '__main__':
    foo = Foo2()


# 用父类的init方法两种方式
# 一种
class A(object):
    def __init__(self):
        self.val = 1
class B(A):
    def __init__(self):
        A.__init__(self)
        print self.val
if __name__ == '__main__':
    foo2 = Foo2()

# 二种
class C(object):
    def __init__(self):
        self.val = 1
class D(C):
    def __init__(self):
        super(C,self).__init__()
        print self.val
if __name__ == '__main__':
    foo2 = Foo2()

# 静太变量

# 静态方法
class Luowei():
    name = "luowei"

    def fun1(self):  # 只有实例可调用
        print (self.name)
        print ("我是公有方法")
        self.__fun2()

    def __fun2(self):  # 只有类内部可调用
        print (self.name)
        print ("我是私有方法")

    @classmethod
    def classFun(self):  #只有实例可调用
        print (self.name)
        print ("我是类方法")

    # classNewFun = classmethod(classFun)

    @staticmethod
    def staticFun():  #只有类可以调用
        print (Luowei.name)
        print ("我是静态方法")


luo = Luowei()
Luowei.staticFun()
luo.classFun()

# 抽象类

# 使用lambda形式
def make_repeater(n):
    return lambda s: s*n
twice = make_repeater(2)
print twice('word')
print twice(5)

# exec语句用来执行储存在字符串或文件中的Python语句
exec 'print "Hello World"'
# eval语句用来计算存储在字符串中的有效Python表达式
eval('2*3')