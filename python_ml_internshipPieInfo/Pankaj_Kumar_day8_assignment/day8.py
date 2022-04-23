from numpy import *
arr1=array([22,33,44,55,66])
#shallow copy
arr2=arr1.view()
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
arr1[1]=0
print(arr1)
print(arr2)