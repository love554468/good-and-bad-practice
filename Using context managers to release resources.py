open file tối ưu 

>>> my_file = open('filename.csv', 'w')
>>> # do something with `my_file and`
>>> my_file.close()

>>> with open('filename.csv', 'w') as my_file:
...     # do something with `my_file`