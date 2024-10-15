import numpy as np

a = np.array([1,2,3,4])
b = np.array([[1,2,3],[3,5,6]], dtype= 'int32')
c = np.array([[0,1,2,3,4],[5,6,7,8,9],[8,6,5,2,1]]) #in multidimension no of rows = no of columns

#dtype = 


'''single dimenstion -> [1,2,4] , {column only}
   two dimension ->     [[1,2,4],[2,4,7]] , {row and coloumn}
   three dimension ->   [[[1,4,5],[1,2,4]],[[2,4,5],[2,4,1]]] {() , row , column}'''
d3 = np.array([[[1,4,5],[1,2,4]],[[2,4,5],[2,4,1]]])

print(b.size) # print number of elements
print(b.dtype) #print type 32 bits or 16 bits -> int16 or int32
print(a.itemsize) # denotes the no of byte of each value [32bits = 4 bytes]
print(a.nbytes) # denotes total number of bytes [no of elements * byte of one value]
print(b.shape) # show the shape (rows,coloums)


#to access specific element array_name[row,column]
print(c[1,4])

#to access entire column
print(c[:,2])
#to access entire row
print(c[1,:])
#
print(c[0:2,1:3])
#to replace elements
c[0,3] = 6
print(c)
c[:,2] = 10 #series of elements
print(c)

'''c[0,:] = 1
print(c)'''

print(d3)
d3[:,1,:] = 6
print(d3)

#MATRIX CREATION

zero1d = np.zeros(3)  # parantesis denotes dimension
zero2d = np.zeros((2,3)) # () - 1d , (()) - 2d , ((())) - 3d
zero3d = np.zeros(((3,3,3)))
print(zero3d)

one = np.ones(3)
one2d = np.ones((2,4))
one3d = np.ones((3,2,3))

fill_with_element = np.full((2,2),5,dtype="float32")
print(fill_with_element) 

r = np.random.randint(0,5)
print(r)
