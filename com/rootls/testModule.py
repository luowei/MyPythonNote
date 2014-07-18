# encoding:utf-8
__author__ = 'luowei'

#引入(多种引入方式)
from com.rootls.modules import number
from com.rootls.modules.number import divide
import com.rootls.modules
import com.rootls.modules as m

# 相除
# x,y = number.divide(42,5)
x,y = divide(42,5)
print x,y   # 8 2

# 取最大公约数
print number.gcd(128,72)    # 8
print com.rootls.modules.number.gcd(84,72)  # 12
