import numpy as np
##x = np.array([1,2,3,4,5,6,7,8,9,10])
##print(x.shape)
##print(x.size)
##print(x.dtype)
##print(x.ndim)

##x = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
##print(x)
##print(x.ndim)

##x = np.array([[[1,2,3,4,5,6,7],[8,9,10,11,12,13,14],[15,45,17,18,19,20,21]]])
##print(x)
##print(x.ndim)

##x = np.array([1,9,8,7,10,5])
##n = x.copy()
##p = x.view()
##x[1] = 10
##print(n)
##print(p)


x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
z = np.concatenate((x,y))
print(z)
p=np.array_split(x,2)
print(p)
print(x[2:])
print(x[1:5])
print(z[1:6])
np.save('array.npy',z)
print(np.load('array.npy'))

