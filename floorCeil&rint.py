import numpy as np
np.set_printoptions(legacy = '1.13')
ar = np.array(input().strip().split(), float)
print(np.floor(ar), np.ceil(ar), np.rint(ar), sep = "\n")

#Not working:-

# import numpy
# numpy.set_printoptions(legacy='1.3')

# n=(input().split())
# my_array=numpy.array(n)
# print(numpy.floor(my_array))
# print(numpy.ceil(my_array))
# print(numpy.rint(my_array))
