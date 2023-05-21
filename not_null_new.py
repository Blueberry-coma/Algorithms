n = int(input())
numbers = list(map(int, input().strip().split()))

def near_null(n, numbers):
    left = []
    for i in range(n):
        if numbers[i] > 0:
            left.append(i)
        else:
            left.append(0)

    right = []
    for i in range(n-1, -1, -1):
        if numbers[i] > 0:
            right.insert(n, i)
        else:
            right.insert(n, 0)
    
    for i in range(n):
        if left[i] > right[i]:
            left[i] = right[i]
    print(left)
    return left

near_null(n, numbers)