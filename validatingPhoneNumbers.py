# import re
# N=input()
# for i in range(N):
#     if re.match(r'[789]\d{9}$',input()):   
#         print('YES')
#     else:  
#         print('NO')
#---------------------------------------------------------------------------------
import re
[print('YES' if re.match(r'[789]\d{9}$',input()) else 'NO') for _ in range(int(input()))]