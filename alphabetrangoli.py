# def print_rangoli(size):
    # your code goes here
    # n=size
    # l1=list(map(chr,range(97,123)))
    # x=l1[n-1::-1]+l1[1:n]
    # m=len('_'.join(x))
    
    # for i in range(1,n):
    #     print('_'.join(l1[n-1:n-i:-1]+l1[n-i:n]).centre(m,'_'))

    
    # for i in range(n,0,-1):
    #     print('_'.join(l1[n-1:n-i:-1]+l1[n-i:n]).centre(m,'_'))
    #=====================================================================
#   n = int(input('Enter a size: '))
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',  'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',   'w', 'x', 'y', 'z']
    
# for j in range(0, n-1):
#     ls_1 = str(''.join(alpha[n-1:abs(n-(j+2)):-1]))
#     ls_1 = ls_1 + ls_1[-2::-1]
#     ls = str('-'.join(ls_1))
#     print('-' * (((n - j) * 2) - 2) + ls + '-' * (((n - j)  * 2) - 2))

# ls_1 = str(''.join(alpha[n-1::-1]))
# ls_1 = ls_1 + ls_1[-2::-1]
# ls = str('-'.join(ls_1))
# print(ls)

# for j in range(n-2, -1, -1):
#     ls_2 = str(''.join(alpha[n-1:abs(n-(j+2)):-1]))
#     ls_2 = ls_2 + ls_2[-2::-1]
#     ls_s = str('-'.join(ls_2))
#     print('-' * (((n - j) * 2) - 2) + ls_s + '-' * (((n -   j) * 2) - 2))
#=========================================================================
def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase

    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
        
    print('\n'.join(L[:0:-1]+L))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)