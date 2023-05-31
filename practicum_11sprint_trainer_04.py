# 87760430
from typing import List, Tuple

def trainer(matrix: List[str], k: int) -> int:
    scores = 0
    count = [0] * 10
    # Понял ошибку. 10 т.к. в матрице числа от 1 до 9
    for numbers in matrix:
        if numbers != '.':
            count[int(numbers)] += 1
    for numbers in count:
        if 0 < numbers <= k:
            scores += 1
    return scores
        

def read_input() -> Tuple[List[str], int]:
    k = int(input()) * 2
    matrix = [i for i in range(4) for i in input().strip()]
    return matrix, k


if __name__ == '__main__':
    k, matrix = read_input()
    print(trainer(k, matrix))