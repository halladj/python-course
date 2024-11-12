import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

arr1 = np.ones((4,4))
arr2 = np.ones((3,5))
e = np.full((2,5),7)
u = np.eye(4)

d = u.shape  #Array dimensions
len(u)       #Length of array
u.ndim       #Number of array dimensions
u.size       #Number of array elements
u.dtype      #Data type of array elements
u.dtype.name #Name of data type
u.astype(int)

#print(f"{u} - \n{arr1} = \n{u+arr1}")
#print(f"{u} + \n{arr1} = \n{u+arr1}")
#print(f"{u} * \n{arr1} = \n{u+arr1}")
#print(f"{u} - \n{np.array([5])} = \n{u+arr1}")
#print(f"{u} / \n{arr1} = \n{u+arr1}")

print(np.exp(u))