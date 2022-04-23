from numpy import *
arr1=array([
    [1,2,3,4,5,6],
    [7,8,9,10,11,12]
])
arr2=arr1.flatten() #Converts into 1D
print(arr2)

arr3=array([
    [
        [1,2,3],[9,10,11],[4,5,6],[7,8,9],[1,2,3]
    ]
])
arr4=arr3.flatten()
print(arr4)

