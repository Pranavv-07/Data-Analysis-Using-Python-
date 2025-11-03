# To extract elements from a NumPy array that are less than or greater than a specified number.
from numpy import *
a=array([10,20,30,40,50])
print(a[a!=30])



# To find the maximum and minimum values and their indices in a 2D array.


arr=array([[10,5,20],[80,60,30]])
arr
print(max(arr))
print(min(arr))
print(argmax(arr))
print(argmin(arr))
print(argmax(arr,axis=0))
print(argmax(arr,axis=1))
print(argmin(arr,axis=0))
print(argmin(arr,axis=1))