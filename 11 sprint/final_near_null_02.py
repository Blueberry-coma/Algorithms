# 87693672

def near_null(n, numbers):
    null_id = []
    for i in range(n):
        if numbers[i] == 0:
            null_id.append(i)
    
    first_zero = null_id[0]
    second_zero = null_id[-1] if len(null_id) == 1 else null_id[1]
    for i in range(first_zero):
        numbers[i] = first_zero - i
    
    temp = 1
    for i in range(first_zero + 1, null_id[-1]):
        if numbers[i]:
            numbers[i] = min(i - first_zero, second_zero - i)
        else:
            temp += 1
            first_zero = second_zero
            second_zero = null_id[temp]
    
    for i in range(second_zero + 1, n):
        numbers[i] = i - second_zero
    print(*numbers)

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().strip().split()))
    near_null(n, numbers)