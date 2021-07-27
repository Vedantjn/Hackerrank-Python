import textwrap

# def wrap(string, max_width):
#     string1=list(string)
# for i in range(len(string1)):
#     print(string[i:i+max_width])
#---------------------------------------------------------------------------
# def wrap(string, max_width):
#     return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])
#---------------------------------------------------------------------------
# def wrap(string, max_width):
#     return textwrap.fill(string,max_width)

#---------------------------------------------------------------------------
def wrap(string, max_width):
    l= list()
    for i in range(0,len(string),max_width): l.append(string[i:i+max_width])
    return "\n".join(l)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)