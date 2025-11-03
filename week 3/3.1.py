# 3.1 (a)
from numpy import * 
print(add(1,2))


# 3.1 (b)

a=array([1,0,3,4])
print("the array is non zero:",all(a))


# 3.1 (c)
from numpy import * 
a=array([1,2,3])
b=array([3,2,1])
print(greater(a,b))
print(greater_equal(a,b))
print(less(a,b))
print(less_equal(a,b))
print(equal(a,b))
print(allclose(a,b))