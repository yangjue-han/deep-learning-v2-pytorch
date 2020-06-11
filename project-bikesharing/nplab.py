import numpy as np

## Zero dimension np array ##
a = np.array([x for x in range(4)])
a
a.shape

# Element-wise product
a * a

# Inner Product
a@a

a.dot(a)

np.dot(a,a)

# Outer product
a * a[:,None]
a * a.T

a.reshape(1,-1) * a.reshape(-1,1)

## Column vector ##
b = np.array([x for x in range(4)]).reshape(-1,1)
b
b.shape

# Element-wise product
bvec = b * b
print(bvec)
bvec.shape

bvec = b.T * b.T
print(bvec)
bvec.shape

b * b.T

b.T * b

# Inner Product
b.T @ b # returns a 1 by 1 array
np.shape(b.T @ b)

b.T.dot(b) # similarly
np.shape(b.T.dot(b))
