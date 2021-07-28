# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*product(a, b))

#-------------------------------------------------------------------------------
# import itertools

# A = [int(x) for x in input().split()]
# B = [int(y) for y in input().split()]

# print(*itertools.product(A, B))
