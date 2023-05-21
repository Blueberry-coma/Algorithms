from typing import List, Tuple

def trainer(k: int, matrix: List[str]):
    fin = 0
    for t in range(10):
        res = 0
        for string in matrix:
            for let in string:
                if let == str(t):
                    res += 1
        if 0 < res <= k * 2:
            fin += 1
    return fin


def read_input() -> Tuple[int, List[str]]:
    k = int(input())
    matrix = []
    for i in range(4):
        matrix.append( input())
    return k, matrix

k, matrix = read_input()
print(trainer(k, matrix))