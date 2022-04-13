import numpy as np

#  how to specify data type  dtype='int16'
a = np.array([1,2,3],dtype='int32')
print(a)


b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])

print(b)

# get dimension

print(b.ndim)

# get shape
# rows, col
print(b.shape)

# Get type

print(a.dtype)

# get Size

print(a.itemsize)

# get total size
print(b.nbytes)

# ----------------- access/ change specific elements,rows,columns

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

# Get specific element [r,c]
# can also use negative notation [1, -2]
print(a[1, 5])

# get specific row
print(a[0, :])

# get specific column
print(a[:, 0])

# lets get fancy [startindex:endindex:stepsize]
# [r, startindex:endindex:stepsize ]
print(a[0,1:-1:2])

# change element

a[1,5] = 20
a[:,5] = [1,2]
print(a)

# 3d ex

b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

# Get specific element (work outside in)
print(b[:,1,1])
