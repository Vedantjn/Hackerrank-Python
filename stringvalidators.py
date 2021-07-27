if __name__ == '__main__':
    
    
    str = input()
print(any(c.isalnum()  for c in str))
print(any(c.isalpha() for c in str))
print(any(c.isdigit() for c in str))
print(any(c.islower() for c in str))
print(any(c.isupper() for c in str))
#=============================================================================
#     s= input()
# print(any([char.isalnum() for char in s]))
# print(any([char.isalpha() for char in s]))
# print(any([char.isdigit() for char in s]))
# print(any([char.islower() for char in s]))
# print(any([char.isupper() for char in s]))

# string = raw_input()
# l=list(string)
# a,b,c,d,e=False,False,False,False,False
# for i in l:
#     if i.isalnum():
#         a=True
#     if i.isalpha():
#         b=True
#     if i.isdigit():
#         c=True
#     if i.islower():
#         d=True
#     if i.isupper():
#         e=True
# print a
# print b
# print c
# print d
# print e
  #=============================================================================

# if s.isalnum()==True:
#     print("True")
# else:
#     print("False")

# if s.isalpha()==True: 
#      print("True")
# else:
#     print("False")
    
# if s.isdigit()==True:
#       print("True")
# else:
#     print("False")
# if s.islower()==True:
#       print("True")
# else:
#     print("False")
# if s.isupper()==True:
#       print("True")
# else:
#     print("False")

   
