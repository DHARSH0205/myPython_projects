import numpy as np

c = np.ones((5,5),dtype="int16")
c[1:4,1:4] = 0
c[2,2] = 9
print(c)

#abovee creation can be done by

d = np.ones((5,5) , dtype="int16")
zeros = np.zeros((3,3),dtype="int16")
zeros[1,1] = 9
d[1:-1,1:-1] = zeros
print(d)