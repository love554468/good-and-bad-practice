>>> x = [1, 2, 4, 8, 16]
>>> for i in range(len(x)):
...     print(x[i])

>>> for item in x:
...     print(item)

>>> for item in x[::-1]:
...     print(item)

>>> for item in reversed(x):
...     print(item)

>>> for i in range(len(x)):
...     print(i, x[i])

>>> for i, item in enumerate(x):
...     print(i, item)

x = []
y =''

>>> for item in zip(x, y):
...     print(item)
... 
(1, 'a')
(2, 'b')
(4, 'c')
(8, 'd')
(16, 'e')

>>> for x_item, y_item in zip(x, y):
...     print(x_item, y_item)
... 
1 a
2 b
4 c
8 d
16 e


