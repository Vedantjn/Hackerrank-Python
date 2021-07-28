# Enter your code here. Read input from STDIN. Print output to STDOUT
# N,M=input()
# for i in range(M):
    # print((((N+5-3*i)*('-')).ljust(N+2))+((((3*i)*(',|,'))).centre(2*i-1))+(((N+5-3*i)*('-')).rjust(N+2))
    # )
# N, M = map(int,input().split())

# for i in range(1,N,2):
#     print((i*",|,").centre(M,"-"))
# print("WELCOME".centre(M,"-"))
# for i in range(N-2,-1,-2):
#     print((i*",|,").centre(M,"-"))



N, M = map(int,input().split())
for i in range(1,N,2):
    pattern=((i * ".|.").center(M, "-")) 
    print(pattern)
print("WELCOME".center(M,"-"))
for i in range(N-2,-1,-2): 
    print((i * ".|.").center(M, "-"))
# print(pattern[::-1])
#==========================================================================
# n, m = map(int,input().split())
# pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))



