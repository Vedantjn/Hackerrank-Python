# Enter your code here. Read input from STDIN. Print output to STDOUT
# import calendar

# print(list(calendar.day_name)[calendar.weekday(y, m, d)].upper())
#------------------------------------------------------------------------------
# import calendar

# a = calendar.weekday(y, m, d) calendar.day_name[a]
#------------------------------------------------------------------------------
# import calendar
# n1,n2,n3=map(int,input().split())
# print((calendar.day_name[calendar.weekday(n3,n1,n2)]).upper())
#------------------------------------------------------------------------------
# import calendar

# m, d, y = map(int, input().strip().split())

# print(calendar.day_name[calendar.weekday(y, m, d)].upper())

# #------------------------------------------------------------------------------
# import calendar

# m,d,y = map(int,input().split())
# days = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
# print(days[calendar.weekday(y,m,d)])
#------------------------------------------------------------------------------
import calendar
m,d,y = map(int,input().split())
days = {0:'MONDAY',1:'TUESDAY',2:'WEDNESDAY',3:'THURSDAY',4:'FRIDAY',5:'SATURDAY',6:'SUNDAY'}
print(days[calendar.weekday(y,m,d)])
