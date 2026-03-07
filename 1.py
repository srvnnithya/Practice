def filter_even(arr):
    return [x for x in arr if x % 2 == 0]

arr = list(map(int, input().split()))
print(filter_even(arr))