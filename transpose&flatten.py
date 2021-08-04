import numpy

n, m = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)
print (array.transpose())
print (array.flatten())

# ------------------------------------------------------------------------------
# import numpy

# n , m = input().split();
# a = [];
# for i in range(int(n)):
#     my_array = input().split();
#     a.append(my_array);
# lis1 = numpy.array(a,int);
# print(numpy.transpose(lis1))
# print(lis1.flatten())
