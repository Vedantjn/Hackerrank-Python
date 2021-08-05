import numpy as np 
n,m = map(int,input().split())
ar = np.array([input().split() for i in range(n)], int)
print(np.prod((np.sum(ar,axis=0)))) 