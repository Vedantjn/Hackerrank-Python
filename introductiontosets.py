def average(array):
    # your code goes here
    return sum(set(arr))/len(set(arr))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
