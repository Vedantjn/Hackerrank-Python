# String Formatting in Python - HackerRank Solution
# def print_formatted(n):
#     width=len(str(bin(n)))[2:]
#     for i in range(1,n+1):
#         print(str(i).rjust(width,' '),oct(i)[2:].rjust(width,' '),hex(i)[2:].upper().rjust(width,' '),bin(i)[2:].rjust(width,' '))
    
def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]

        print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)