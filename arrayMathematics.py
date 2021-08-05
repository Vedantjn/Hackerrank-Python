import numpy as np
N, M = list(map(int, input().split()))

a1 = np.array([input().split() for _ in range(N)], int)
a2 = np.array([input().split() for _ in range(N)], int)

print(*[eval('a1'+i+'a2') for i in ['+','-','*','//','%','**']], sep='\n')

#Not working:

# import numpy

# n,m=list(map(int.input().split()))

# for i in range(n):
#     A=input().split()
#     a=numpy.array(A,float)
# for i in range(n):
#     B=input().split()
#     b=numpy.array(B,float)
    
# print(numpy.add(a, b))           #[  6.   8.  10.  12.]

# print(numpy.subtract(a, b))     #[-4. -4. -4. -4.]

# print(numpy.multiply(a, b))      #[  5.  12.  21.  32.]

# print(numpy.divide(a, b))      #[ 0.2         0.33333333  0.42857143  0.5       ]

# print(numpy.mod(a, b))          #[ 1.  2.  3.  4.]

# print(numpy.power(a, b))