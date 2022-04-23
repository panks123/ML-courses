from numpy import*
arr3=array([
    [
        [1,2,3],[9,10,11],[4,5,6],[7,8,9],[1,2,3]
    ]
])
arr4=arr3.flatten()
arr5=arr4.reshape(5,3) #it will reshape the array to a 2D array of order 5X3
print(arr5)
print("-------------------------------")
arr1=array([[1,2,3,2],[4,5,6,7],[1,2,3,4]])
arr2=arr1.reshape(2,2,3)
print(arr2)