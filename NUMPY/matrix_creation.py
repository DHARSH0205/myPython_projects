import numpy as np

#full(size,number_to_be_filled)
fill_with_element = np.full((2,2),5,dtype="float32")
print(fill_with_element)

b = np.array([[1,2,3],[3,5,6]], dtype= 'int32')

r = np.random.randint(0,5)

#c = np.full_like(b,3)
c2 = np.full(b.shape,r)
#both c and c2 are equal

print(r)
print(c2)
c3 = np.random.rand(3,3) #fill with random values from 0 to 1 in the given dimension 
c3 = np.random.random_sample(b.shape) #fill with random values from 0 to 1 like the dimension of given argument

c4 = np.random.randint(0,9,size=(4,3)) #size= can be [1d-1], [2d-(2,3)] ,[3d-(3,3,3)]

identity = np.identity(5,dtype="int8") #create identity matrix 5= 5X5 (since identity matrix is a square matrix)
print(identity)

#print(c4)

a = np.array([1,2,3])
b = a.copy() #its gets a copy of the contents of 'a'
c = a #it points a -> if c gets changed a will also gets changed and vice versa
