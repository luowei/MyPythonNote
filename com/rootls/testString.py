# encoding:utf-8
__author__ = 'luowei'

#字符中可以是单引号，也可以是双引号包裹
#一般一行以内用单引号，多行用双引号

print 'abc'+'def' # abcdef
print "abcd_" \
      "hello"   # abcdhello

print 'abc'*3 # abcabcabc
str = "123456"
print len(str) # 6
print str[1] # 2
print str[1:4] # 234
print str[:4] # 1234
print str[2:] # 3456
print str[0:5:2]  # 135
print str[1:5:2] # 24
print str[-1] # 6
print str[-2] # 5

print  "hello".upper() # HELLO




