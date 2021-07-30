# print(input() == 0 or len(set(input().split()).union(input() == 0 or input().split())))

_, a = input(), set(input().split())
_, b = input(), set(input().split())
print(len(a.union(b)))
