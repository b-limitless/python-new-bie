import numpy as np


"""
#Create a 0-D array with value 42
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#Create an array with 5 dimensions and verify that it has 5 dimensions:


#NumPy Array Indexing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st dim: ', arr[0, 1])


arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('5th element on 2nd dim: ', arr[1, 4])
"""


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

#Slice elements from index 1 to index 5 from the following array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

#Slice elements from index 4 to the end of the array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])

#Slice elements from the beginning to index 4 (not included):
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])

#Slice from the index 3 from the end to index 1 from the end:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])

#Return every other element from index 1 to index 5:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])

#Return every other element from the entire array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2])

#From the second element, slice elements from index 1 to index 4 (not included):
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])

#From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])


#################################################################
##NumPy Data Types
#################################################################

"""
strings - used to represent text data, the text is given under quote marks. eg. "ABCD"
integer - used to represent integer numbers. eg. -1, -2, -3
float - used to represent real numbers. eg. 1.2, 42.42
boolean - used to represent True or False.
complex - used to represent a number in complex plain. eg. 1.0 + 2.0j, 1.5 + 2.5j
"""

arr = np.array([1, 2, 3, 4])
print(arr.dtype) #int64

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype) #<U6

#Create an array with data type 4 bytes integer:
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)
#[1 2 3 4]
#int32
#https://www.w3schools.com/python/numpy_data_types.asp


##################################
## NumPy Array Copy vs View ##
##################################
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

#Make a view, change the original array, and display both arrays:
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

#Make a view, change the view, and display both arrays:
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31


#Print the value of the base attribute to check if an array owns it's data or not:
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

#Print the shape of a 2-D array:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)


#Reshape From 1-D to 2-D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
"""
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
"""

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)
"""
[[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]]
"""
#https://www.w3schools.com/python/numpy_array_iterating.asp
#Try converting 1D array with 8 elements to a 2D array with 3 elements in each dimension (will raise an error):
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(3, 3)

#Iterate on each scalar element of the 2-D array:
for x in arr:
  for y in x:
    print(y)


#Iterate down to the scalars:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  for y in x:
    for z in y:
      print(z)

######################################
## Joining NumPy Arrays
#https://www.w3schools.com/python/numpy_array_join.asp
######################################
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))

#Join two 2-D arrays along rows (axis=1):
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)

