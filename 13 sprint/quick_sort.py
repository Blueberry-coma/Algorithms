#88095660
def quick_sort(contenders, start, end):
    if start >= end:
        return -1

    left, right = start, end
    barrier = contenders[start]

    while left <= right:
        while contenders[left] < barrier:
            left += 1
        while contenders[right] > barrier:
            right -= 1
        if left <= right:
            contenders[left], contenders[right] = contenders[right], contenders[left]
            left += 1
            right -= 1

    quick_sort(contenders, start, right)
    quick_sort(contenders, left, end)


def name_sort(contenders):
    contenders[1] = -int(contenders[1])
    contenders[2] = int(contenders[2])
    return [contenders[1], contenders[2], contenders[0]]


def read_input():
    n = int(input())
    players = [name_sort(input().split()) for _ in range(n)]
    return players


def main():
    players = read_input()
    quick_sort(players, start=0, end=len(players) - 1)
    for player_name in players:
        print(player_name[2])


if __name__ == '__main__':
    main()