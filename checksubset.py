# Enter your code here. Read input from STDIN. Print output to STDOUT
# t=int(input())
# a=int(input())
# sa=set(map(int,input().split()))
# b=int(input())
# sb=set(map(int,input().split()))
# for i in range(t):
#     if(sa-sb)==0:
#         print("True")
#     else:
#         print("False")
#----------------------------------------------------------------------------------------
# for _ in range(int(input())):
# x, a, z, b = input(), set(input().split()), input(), set(input().split())
# print(a.issubset(b))# Enter your code here. Read input from STDIN. Print output to STDOUT
#----------------------------------------------------------------------------------------
n = int(input())

for i in range(n):
    a = int(input())
    set_a = set(input().split())
    b = int(input())
    set_b = set(input().split())
    out_set = set_a.difference(set_b)
    if len(out_set) == 0:
        print(True)
    else:
        print(False)
    