import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9,10])#Array type
print(type(a))
print(a)

#Zeros

a = np.zeros(4)#four zeros in one dim
print(a)

#Once

a = np.ones(3)# Three ones in n-dim
print(a)

#Range

a=np.arange(1,78)# Range from 1-77

b=np.arange(0,100,5)#it indicates start from zero and end in 99 in sapce b/w 5

print(b)

print(a)

#Line space

a=np.linspace(1,5,10) #it indicates the linspace b/w 1&5 in diff (10)

print(a)

#n-dim

a=np.array([[ [39,4,56,23,56,54],[2,34,355,6754,3,4],[67,3,45,3,25,3] ]]) #it  is an three dimensional array represnt through no.SQ brackets in starting

print(a.ndim)

#Full

a = np.full([2,3],10) #full determines that row and coloum with same values in our program ie)10

print(a)

#Random

a = np.random.randint(1,10,size=(3,4,4))#Randint print random number from give range(1-10)in
                                        #size of three dim 4*4 matrix
print(a)                     


#Reshape

a = np.arange(1,10)

b = a.reshape(3,3) #reshape into 3*3 matrix,if shape may (3,4)it should error

print(b)

#Ravel

a = np.array([[1,2,3,4,5],[3,4,5,6,8]])

b = a.ravel()# Make two dimension multiple dimension in single dimesion

print(a)
             
#Transpons

a = np.array([[[1,2,3,4],[1,2,3,4],[4,5,6,7]]])

b=a.transpose()# Helps to make rows into column and colums into rows

c = np.array([[1,2,34],[1,2,34]])

d = np.array([[1,2,3],[34,4,5]])

print(c,d)
print(a)

#Eye

b = np.eye(4)#Identify matrix(diagonal values are 1 and remaning values are 0)

print(b)

#Slicing

a = np.array([1,2,3,4,56,87,64,46,678,43])

print(a[-2])#slicing of value using index (ie)1(0th index value)-2 from reverse


#Index slicing

a = np.array([[1,23,456,],[1,3,45]])

print(a[1,2])# second row index values 1 & 2 and give remaning value 45 

print(a[:-1])# slice 1st index -1

print(a[1,:-1])

print(a[1,2:3])

a = np.array([1,23,45,2,4,6,4,2,1,78])

print(a[3])


#Concatination

a = np. array ([3,4,5,67])

b = np.array([2,4,56])

con = np. concatenate([a,b])#Used to add row and column 

print(a,b)
    


#Split()

a = np . array([1,3,45,5])

b = np.array_split(a,3)#array split

c = np.hsplit(a,2)#horizondal split

#d= np.vsplit(a,3)

print(b)

print(c)

print(d)


#square

a = 3

b=np.sqrt(a)

c = np.array([2,3,45])

d= np.sqrt(c)#square root values

print(b)

print(d)


#Log

a = 3

b = np.log(a)

print(b)

c= np.array([1,2,34])#Find log value

d = np.log(c)

print(d)


#Exponential

a = 4

b = np. exp(a)#Exponential value of 4

print(b)


#Mod

a = np.array([10,34,23])

b = np.mod(a,2)#It return the remainder value ,2 represent divisor 

print(b)


#Broad casting

a = np.array([[1,2,34,5],[3,4,5,6]])

b = np.array([2,3,4,5])# in broad casting seprate and perform add or else oprations

c = a + b

print("Broad casting \n: ", c)

#Dot

a = np.array([[1,2],[3,4]])

b= np.array([[4,5],[3,4]])

c= np.dot(a,b)

print(c)






































