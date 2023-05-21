def invert_array(A:list, N:int):
    for k in range(N//2):
        A[k], A[N - 1 - k] = A[N - 1 - k], A[k]

def test_invert_array():
    A1 = [1, 2, 3, 4, 5]
    print(A1)
    invert_array(A1, 5)
    print(A1)
    if A1 == [5, 4, 3, 2, 1]:
        print('test 01 ok')
    else:
        print('test 01 fail')

    A2 = [0, 0, 0, 0, 0, 0, 0, 10]
    print(A2)
    invert_array(A2, 8)
    print(A2)
    if A2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print('test 02 ok')
    else:
        print('test 02 fail')

test_invert_array()