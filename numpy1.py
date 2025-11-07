import numpy as np

#creating array
n1= np.array([3,1,2,6,4,5])
print (n1)
#creating 2d array
n2= np.array([[3,5,4],[7,9,8]])
print(n2)

#creating zero filled 2d array
n3= np.zeros([3,5]) #this will create floating point value so . is have
print(n3)

#creating zero filled 2d array
n3= np.zeros([3,5],dtype='int32') #if would not be wanted the floating point
print(n3)

#creating zero filled 3d array
n4= np.ones([2,3,3],dtype='int32')
print(n4)

#create with random values like empty use
n5= np.empty([1,3])
print(n5)

#create array with range of values
n6= np.arange(9)  #it will create 0 to 9 without 9
print(n6)
#            start end step
n7= np.arange(-5,  10,  2)
print(n7)

#linearly spaced entries
n8= np.linspace(0,20,num=5)
print(n8)

# create array with default value
n9= np.full([2,5],99)
print(n9)

#create array and fill another values
nn5= np.empty([1,3])
print(nn5)
nn5.fill(9)
print(nn5)

#change values from array one seperate index
nn4= np.ones([2,3,3],dtype='int32')
print(nn4)
nn4[1,2,1]=99   #value change
print(nn4)

#accessing or printing values of array
print(n8[1])    #normal
print(n8[-1])   #reverse
print(n2[1,2])  #2d array
print(n2[1,:])  # get all rows
print(n2[:,2])  # get all coloms
print(n4.ndim)  #find diamantional array
print(n4.shape) #find the shape of creation of the array
print(n4.dtype) # find type of the value
print(n4.itemsize)  # find the every item's alocating space
print(n4.nbytes)    # find the size of the array in bytes

#print with transpose the array
print(np.transpose(n2)) 

#sorting value from array (we can short any type of array :1d & 2d & 3d)
print(np.sort(n1)) 
print(np.sort(n2))#all row sorted
print(np.sort(n2,axis=0))#sort by rowby row
print(np.sort(n2,axis=1))#sort by colom by colom

#change the 1d array into split the array as the 2d array
n12 = np.array([3,1,2,6,4,5,7,5,6,7,8,3])
print(n12)
nn12= n12.reshape(3,4)
print(nn12)

#join 2d array using concatenate
n13 = np.arange(4)
print(n13)
n14= np.arange(5,9)
print(n14)
n15= np.concatenate((n13,n14)) 
print(n15)

#converting 1d array into 2d array using newaxis
n16= np.array([3,1,2,6])
print(n16)
n17= n16[np.newaxis,:] #row wise
print(n17)
print(n17.shape)
n18= n16[:,np.newaxis] #colom wise
print(n18)
print(n18.shape)

#expand dims
n19= np.expand_dims(n16, axis=0) #row wise
print(n19)
n20= np.expand_dims(n16,axis=1) #colom wise
print(n20)

#advanced indexing
n21= np.arange(10)
print(n21)
print(n21[n21<5])

print(n21[(n21>3) & (n21<8)])

fiveup = n21>5
print(fiveup)
print(n21[fiveup])

#Stacking arrays(joining arrays in a different way)
n22= np.array([[1,2],[3,4]])
print(n22)
n23= np.array([[5,6],[7,8]])
print(n23)
n24= np.vstack((n22,n23)) #vertical stack
print(n24)
n25= np.hstack((n22,n23)) #horizontal stack
print(n25)

#splitting arrays
n26= np.arange(9)
print(n26)
n27= np.split(n26,3) #split into 3 equal parts
print(n27)

#copying arrays(deep copy)
n28= np.array([1,2,3,4,5])
n29= n28.copy()
n28[0]=99
print(n28)
print(n29)

#math operations on array
n30= np.array([1,2,3,4,5])
print(n30)
n31= n30 + 5
print(n31)
n32= n30 * 2
print(n32)
n33= n30 ** 2
print(n33)
n34= np.sqrt(n30)
print(n34)
n35= np.sin(n30)
print(n35)
n36= np.log(n30)
print(n36)
n37= np.exp(n30)
print(n37)
print(n30+n31) #array addition
print(n30*n31) #array multiplication

#random values
n38= np.random.rand(3,4) #uniform distribution
print(n38)
n39= np.random.randn(3,4) #normal distribution
print(n39)
n40= np.random.randint(1,10,size=(3,4)) #random integers between 1 and 10
print(n40)
n41= np.random.choice([10,20,30,40,50], size=(3,4)) #random choice from given array
print(n41)

#seed value
n42= np.random.seed(42)
print(n42)