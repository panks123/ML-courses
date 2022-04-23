import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)

print(arr.dtype)

arr=np.array([1,2,3.3,4.5,8],int)
print(arr)


# Different types of creating arrays

arr=np.linspace(0,15,9)
print(arr)

arr=np.linspace(0,15) # 50 parts automatically 
print(arr)

arr=np.arange(1,50,2)
print(arr)

arr=np.logspace(1,40,5)
print(arr)

arr= np.zeros(5)
print(arr)

arr= np.zeros(5,int)
print(arr)

arr= np.ones(5)
print(arr)

arr= np.ones(5,int)
print(arr)


#array addition
#1. Scalar Addition
arr=np.array([1,3,4,2,7])
arr=arr+5
print(arr)

#vectorized addition
arr1=arr=np.array([1,3,4,2,7])
arr2=np.array([1,2,3,4,5])
print("Addition: ",arr1+arr2)



