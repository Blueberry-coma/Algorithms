def move_left(A:list, N:int):
    tmp = A[0]
    for k in range(N-1):
        A[k] = A[k+1]
    A[N-1] = tmp


def move_right(A:list, N:int):
    tmp = A[N-1]
    for k in range(N-2, -1, -1):
        A[k+1] = A[k]
    A[0] = tmp