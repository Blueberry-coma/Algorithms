# 87967669
import operator

operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv,
    }

class Stack:
    def __init__(self):
        self.__value = []

    def push(self, value: int):
        self.__value.append(value)

    def pop(self):
        return self.__value.pop()

def main(stack = Stack(), operators = operators):
    for i in input:
        if i in operators:
            number_two = stack.pop()
            number_one = stack.pop()
            stack.push(operators[i](number_one, number_two))
        else:
            stack.push(int(i))

    print(stack.pop())

input = input().split()

if __name__ == '__main__':
    main()