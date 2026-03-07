def second_largest(arr):
    arr = list(set(arr))
    arr.sort()
    return arr[-2]

arr = list(map(int, input().split()))
print(second_largest(arr))