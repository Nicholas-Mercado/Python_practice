import numpy as np

# All 0s matrix
x=np.zeros((3,3))

# print(x)

# All 1s matrix

x=np.ones((4,4))

# print(x)


# Any other number
#  ((r,c), your #)
x=np.full((2,2),99)

# print(x)

# Any other Number (full_like)
x = np.full_like(x,4)

# print(x)

# Random numbers
x = np.random.rand(4,2)

# print(x)

o = np.ones((5,5))
z= np.zeros((3,3))
z[1,1]= 9
o[1,1] = z

print(o)
