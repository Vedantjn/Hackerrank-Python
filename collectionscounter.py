import collections


number_of_shoes = int(input())
sizes_in_stock = collections.Counter(map(int, input().split()))

total_revenue = 0

for _ in range(int(input())):
    size, price = map(int, input().split())
    if sizes_in_stock[size]:
        total_revenue += price
        sizes_in_stock[size] -= 1

print(total_revenue)
#-----------------------------------------------------------------------------------------
# Enter your code here. Read input from STDIN. Print output to STDOUT
# n=input()
# s=list(map(int,input().split()))
# l=int(input())
# p,q=list(map(int,input().split()))
# sum=0

# for i in l:
#     if p in s:
#         return sum+=q[i]
#     else:
#         return sum
#---------------------------------------------------------------------------------------
    
# import collections

# numShoes = int(raw_input())
# shoes = collections.Counter(map(int, raw_input().split()))
# numCust = int(raw_input())

# income = 0

# for i in range(numCust):
#     size, price = map(int, raw_input().split())
#     if shoes[size]: 
#         income += price
#         shoes[size] -= 1

# print(income)