import numpy
numpy.set_printoptions(legacy='1.13')

n,m=map(int,input().split())
if n==m:
    print(numpy.identity(n))
else:
    print(numpy.eye(n,m,k=0))
