Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 123
123
>>> _
123
>>> a=10
>>> id(a)
1508140272
>>> a=12
>>> n=[33,44,556,77,22]
>>> n
[33, 44, 556, 77, 22]
>>> #Tuple
>>> #it is a data type fater than list
>>> #It is immutable in nature
>>> #it is repersent within ()
>>> t=(22,33,44,55,66,77,22)
>>> t
(22, 33, 44, 55, 66, 77, 22)
>>> t.count(22)
2
>>> t.index(77)
5
>>> #Sets
>>> #It is a data type in python .It is similar to the set present in mathematics
>>> #It does not support indexing
>>> #Output of set is in random order
>>> #it is represented within {}
>>> s={33,34,55,66,77,88,99,33,55}
>>> s
{33, 34, 66, 99, 77, 55, 88}
>>> z={55,66,77,22,34,45,67,8,11}
>>> z
{66, 34, 67, 8, 11, 77, 45, 22, 55}
>>> z.difference(s)
{67, 8, 11, 45, 22}
>>> z.intersection(a)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    z.intersection(a)
TypeError: 'int' object is not iterable
>>> #Dictionary
>>> #It is dattype in python
>>> # it supports key:value argument
>>> d={'Angel':'Samsung','Rahul}
