import numpy

a=int(input())

arr1=numpy.array([list(map(int,input().split())) for _ in range(a)])

arr2=numpy.array([list(map(int,input().split())) for _ in range(a)])

print(numpy.dot(arr1,arr2))

#Not working:-

# import numpy
# n=int(input())
# my_arrayA=numpy.array([list(map(int,input().split())) for _ in range(n)])
# my_arrayB=numpy.array([list(map(input().split())) for _ in range(n)])

# print(numpy.dot(my_arrayA,my_arrayB))