# # Enter your code here. Read input from STDIN. Print output to STDOUT
# import re
# s=str(input())

# re.finditer(r'[\+\-\ ]?[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]*[AEIOUaeiou]+[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]',s)

# import re
# s = '[qwrtypsdfghjklzxcvbnm]'
# a = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I)
# print('\n'.join(a or ['-1']))

import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
s=input()
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), s, flags = re.I)
print('\n'.join(m or ['-1']))