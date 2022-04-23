Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> arr1=array('i',[1,2,3,4,5])
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    arr1=array('i',[1,2,3,4,5])
NameError: name 'array' is not defined
>>> from array import *
>>> arr1=array('i',[1,2,3,4,5])
>>> for i in arr1:
	print(i)

1
2
3
4
5
>>> arr1.typecode
'i'
>>> print("Address and size:",arr1.buffer_info())
Address and size: (50724040, 5)
>>> arr2=array('f',[1,2.34,5.09,7.45.4])
SyntaxError: invalid syntax
>>> arr2=array('f',[1,2.34,5.09,7.45,4])
>>> print(arr2)
array('f', [1.0, 2.3399999141693115, 5.090000152587891, 7.449999809265137, 4.0])
>>> arr1=array('i',[1,2,3,4,5,4,3,2,1])
>>> arr2=(arr1.typecode,[i for i in arr1])
>>> for i in arr2:
	print(i)

	
i
[1, 2, 3, 4, 5, 4, 3, 2, 1]
>>> print(arr2)
('i', [1, 2, 3, 4, 5, 4, 3, 2, 1])
>>> 
