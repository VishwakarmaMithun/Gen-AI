import numpy as np
arr = np.array([[1,2,3,4],[4,5,6,6]])
print(arr> 2);

#Vector Operations: Oeration will be the given number of matrics
arr_1 = np.arange(1,17).reshape(4,4)
arr_2 = np.arange(20,36).reshape(4,4)
print(arr_1*arr_2)

#import function of numpy for machine learning and data science.

##max() --> it is going to be used to calcuate teh max value insider a matic or an array

print(np.max(arr_2))

arrydata= np.round(np.random.random((4,4))*100).astype('int32')
print(arrydata)