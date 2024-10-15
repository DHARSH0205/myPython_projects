import numpy as np

#AXIS 
#axis = 0 helps operate over vertically i.e row by row
#axis = 1 -> horizantally column by column

a = np.array([0,30,45,60,90])
'''a = a*5
a = a + 5
a = a-5
a = a/5
a = a*5
a = a**5

a = np.cos(a)
a = np.sin(a) '''
print(a)

b = np.full((2,2),4)
c = np.full((2,2),3)
print(b*c) #normal multiplication (only for same dimension arrays)
print(np.matmul(b,c)) #matrix multiplication -> gives matrix multiplication result

b1 = np.full((2,3),4)
c1 = np.full((3,2),3)
#print(np.matmul(b1,c1)) #matrix multiplication

identity = np.identity(4) #for identity matrix, determinant is one
determinant = np.linalg.det(identity)
print(determinant) 

v1 = np.array([1,2,3])
v2 = np.array([5,6,7])

print(np.hstack((v1,v2)))
print(np.vstack((v1,v2)))

h1 = np.ones((2,5))
h2 = np.zeros((2,2))

print(np.hstack((h1,h2)))