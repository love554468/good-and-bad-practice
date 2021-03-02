import re
str = """
>>> x = (1, 2, 4, 8, 16)
>>> a = x[0]
>>> b = x[1]
>>> c = x[2]
>>> d = x[3]
>>> e = x[4]
>>> a, b, c, d, e """

str = re.sub(">>> ","",str)
print(str)
======================
#cach don thuan
x = (1, 2, 4, 8, 16)
a = x[0]
b = x[1]
c = x[2]
d = x[3]
e = x[4]
a, b, c, d, e
# cach ma python co the thuc hien
===================
>>> a, b, c, d, e = x
>>> a, b, c, d, e
(1, 2, 4, 8, 16)
==================
>>> a, *y, e = x
>>> a, e, y
(1, 16, [2, 4, 8])
====
# them nua ne
>>> x = 2
>>> y = 2
>>> z = 2
>>> x, y, z = 2, 2, 2

