import abc
from typing_extensions import ParamSpec


Py ko thực sự riêng tư thành viên lớp 
Tuy nhiên thì ko nên truy cập hoặc chỉnh sửa 
nhưng thằng có gạch dưới _ 
Nó ko tốt chút nào 

====

đơn giản vl tránh dùng nó thế thôi


>>> class C:
...     def __init__(self, *args):
...         self.x, self._y, self.__z = args
... 
>>> c = C(1, 2, 4)

>>> c.x  # OK
1
>>> c._y  # Possible, but a bad practice!
2
>>> c.__z # Error!
Traceback (most recent call last):
File "", line 1, in 
AttributeError: 'C' object has no attribute '__z'
>>> c._C__z # Possible, but even worse!
4
>>>