# for i in range(int(input())):    
#     try:
#         n=input()
#         int(n.split('.')[1])    #for Decimal value ('12.')
#         if float(n):
#             print('True')
#     except:        
#         print('False')
# #--------------------------------------------------------------------------------------
# import re

# for _ in range(int(input())):
#     print(bool(re.match("^[\+-]?\d*\.\d+$", input())))
    #--------------------------------------------------------------------------------------\
# import re

# for _ in range (int(input())):
#     print(bool(re.match('[-+]?[0-9]*\.[0-9]+$',input())))
#-------------------------------------------------------------------------------
count=int(input().strip())
for _ in range(count):
    ans=False
    try:
        string=input().strip()
        number=float(string)
        ans=True
        number=int(string)
        ans=False
    except:
        pass
    print(ans)    