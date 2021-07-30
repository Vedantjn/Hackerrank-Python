length=int(input())
s=set(map(int, input().split()))
N=int(input())

for i in range(N):
    (p, q)=input().split()
    s2=set(map(int, input().split()))
    if p=='intersection_update':
        s.intersection_update(s2)
    elif p=='update':
        s.update(s2)
    elif p=='symmetric_difference_update':
        s.symmetric_difference_update(s2)
    elif p=='difference_update':
        s.difference_update(s2)
print(sum(s))
#---------------------------------------------------------------------------------------
#this one not giving correct output
# a=int(input())
# b=set(int(input().split()))
# n=int(input())

# for i in range(n):
#     s=set(input().split())
    
#     if s[0]=="intersection_update":
#         s.intersection_update(s[1])
#     elif s[0]=="update":
#         s.update(s[1])
#     elif s[0]=="symmetric_difference_update":
#         s.symmetric_difference_update(s[1])
#     elif s[0]=="difference_update":
#         s.difference_update(s[1])
# print(sum(s))