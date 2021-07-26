if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    print(max([x for x in arr if x!=max(arr)]))
    

#     i = int(input())
# lis = list(map(int,input().strip().split()))[:i]
# z = max(lis)
# while max(lis) == z:
#     lis.remove(max(lis))

# print max(lis)