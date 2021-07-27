def swap_case(s):   
    return s.swapcase()

    # s=[]
    # if s[i].upper():
    #     return s[i].lower()
    # else:
    #     return s[i].upper()
#========================================================================================
    # def swap_case(s):
    # result = ""
    # for letter in s:
    #     if letter == letter.upper():
    #         result += letter.lower()
    #     else:
    #         result += letter.upper()
    # return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    