from numpy import *
arr1=array([22,33,44,55,66])
#deep copy
arr2=arr1.copy()
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
arr2[1]=0
print(arr1)
print(arr2)