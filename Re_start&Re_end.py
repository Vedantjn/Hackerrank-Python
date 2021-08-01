# import re
# s = input()
# v = input()
# for i,x in enumerate(s):
#     if re.match(v,s[i:]):
#         print((i,i+len(v)-1))
# if re.search(v, s)==None:
#     print((-1,-1))  

#------------------------------------------------------------------------------------
import re
S = input()
k = input()
m = re.search(k, S)
pattern = re.compile(k)
if not m: print("(-1, -1)")
while m:
    print("({0}, {1})".format(m.start(),m.end()-1))
    m = pattern.search(S,m.start()+1)