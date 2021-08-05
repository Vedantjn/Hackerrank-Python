import numpy
n,m=list(map(int,input().split()))

my_array=numpy.array([input().split() for _ in range(n)],int)
print(numpy.mean(my_array,axis=1))
print(numpy.var(my_array,axis=0))
# print(numpy.std(my_array,axis=None))
print(round(numpy.std(my_array, axis = None),11))
