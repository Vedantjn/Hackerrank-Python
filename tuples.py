n = input()
input_line = input()
input_list = input_line.split()

#    for i in range(n):
#         input_list[i] = int(input_list[i])

#    for i in range(len(input_list)):
#         input_list[i] = int(input_list[i])

# input_list = map(int, input_list)

input_list = [int(x) for x in input_list]

t = tuple(input_list)

print(hash(t))