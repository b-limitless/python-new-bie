import numpy as np




# shaping the array 
arr = np.array([1,2])
arr2 = np.array([2,3])
arr3 =  np.concatenate((arr, arr2))
print(arr3)