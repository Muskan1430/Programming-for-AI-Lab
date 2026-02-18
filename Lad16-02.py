import numpy as np
a = np.array([10,20,30])
print(a)

import numpy as np
a = np.array([10,20,30])
print(type(a))

b = np.array((10,20))
print(type(b))

c = np.array([[10,20],[30,40]])

d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

#ndim
print("a.ndim", a.ndim)
print("c.ndim", c.ndim)

#shape
print("a.shape", a.shape)
print("b.shape", b.shape)
print("c.shape", c.shape)
print("d.shape", d.shape)

x = np.array([1,2,3,4,5])
y = np.array([
    [1,2,3],
    [4,5,6]
])
z = np.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]]
])

print("x.shape", x.shape)
print("y.shape", y.shape)
print("z.shape", z.shape)

#size
print("x.size", x.size)
print("y.size", y.size)
print("z.size", z.size)

#dtype
print("x.shape", x.dtype)
print("y.shape", y.dtype)
print("z.shape", z.dtype)

#itemsize
print(a.itemsize)
print(d.itemsize)
print(y.itemsize)
print(z.itemsize)

#nbytes
print(x.nbytes)
print(y.nbytes)
print(z.nbytes)

#indexing and slicing in 1D
m = np.array([1,2,3,4,5])

#indexing
print("m[0]", m[0])
print("m[-1]", m[-1])

#slicing
#array[start:stop:step]
print(m[0:2])
print(m[-4:-1:2])
print(m[::-1])

#indexing and slicing in 2D
n = np.array([ [1,2,3],
               [4,5,6],
               [7,8,9] ])

#indexing
print(n[1,2])
print(n[1])
print(n[-1])

#slicing
print(n[0:2,0:2])
print(n[0:2,:])

#indexing + slicing
print(n[1,0:2])

#fancy indexing
p = np.array([1,2,3,4,5])
indices = [0, 2, 4]
k = p[indices]
print(k)

#boolean masking
mask = (p > 1)
print(mask)
l = p[mask]
print(l)

#functions
#zeros
g = np.zeros((2,3), dtype="int")
print(g)

#ones
h = np.ones((3,2,3))
print(h)

#arange
j = np.arange(1,11)
print(j)

#linespace
f = np.linspace(1,10,2)
print(f)

#copy
v = np.array([1,2,3])
w = v[0:3].copy()
print(w)
w[0] = 5
print(v)
print(w)
