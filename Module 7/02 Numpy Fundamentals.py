from numpy import int32, linspace
import numpy as np
#multiple dimenstional array
numpy_array= np.array([1,3,4,5,5,6,])
print(type(numpy_array))
print(numpy_array)
print(np.array([[1,3,4],[4,5,6],[5,6,7],[3,5,6]]))

#3D Tensor 

ThreeDArray = np.array([[1,2],[3,5],[5,6]])

#np.array used for creating multidimentsion arrry
print(numpy_array.size)

#dtype parameter which can help in deciding the size of element or data

print(np.array([1,3,4,5,6,6],dtype=int32))
print(np.array([3,4,45,6,6,7,7],dtype=np.int8))
print(np.array([True,False],dtype=bool))


emp_list =[]
for i in range(0,15):
    emp_list.append(i);

print(emp_list)
print(np.arange(15));
print(list(np.arange(3)));
print(np.arange(1,35,3))
arange_data = np.arange(1,35,3)
print(arange_data.reshape(3,4));
print(np.arange(2,20))
print(np.ones((2,4),dtype=int))

print(np.ones((4,4)))
print(np.random.random((3,3)))
print(np.identity(5))
print(np.linspace(-20,10,20))

arr = np.array([[1,2,3,4],[4,5,6,6]])
print(arr.dtype)
print(arr.shape)
print(arr.size)


print(arr * 2);
print(arr/2)