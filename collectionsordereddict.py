# Enter your code here. Read input from STDIN. Print output to STDOUT
# from collections import OrderedDict

# od=OrderedDict()
# for i in range(int(input())):
#     str=input.split()
#     k=' '.join(str[:-1])
#     v=int(str[-1])
    
#     if k in od:
#         od[k]=od[k]+v
#     else:
#         od[k]=v
# for k,v in od.items():
#     print(k,v)

from collections import OrderedDict

number_ = int(input())
odict = OrderedDict()
for i in range(number_):
    litem = input().split(' ')
    price = int(litem[-1])
    item_name = " ".join(litem[:-1])
    if odict.get(item_name):
        odict[item_name] += price
    else:
        odict[item_name] = price

for i,v in odict.items():
    print(i,v)
