def array_search(A:list, N:int, x:int):
    for k in range(N): 
        if A[k] == x:
            return k
    return -1

def test_array_search():
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, 5, 8)
    if m == -1:
        print('test 01 ok')
    else:
        print('test 01 fail')


    A2 = [-1, -2, -3, -4, -5]
    m = array_search(A2, 5, -3)
    if m == 2:
        print('test 02 ok')
    else:
        print('test 02 fail')

    A3 = [10, 20, 30, 10, 10]
    m = array_search(A3, 5, 10)
    if m == 2:
        print('test 03 ok')
    else:
        print('test 03 fail')

test_array_search()