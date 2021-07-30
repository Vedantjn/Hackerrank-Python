# Enter your code here. Read input from STDIN. Print output to STDOUT

e, a = input(), set(input().split())
f, b = input(), set(input().split())
print(len(a.intersection(b)))