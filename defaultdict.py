from collections import defaultdict

n,m = list(map(int,input().split()))
d = defaultdict(list)
for i in range(n):
    a=input()
    d[a].append(i+1)
for i in range(m):
    b=input()
    print(*d[b] or [-1])