from itertools import permutations


def _14888():
    N = int(input())
    numbers = list(map(int, input().split()))
    start, numbers = numbers[0], numbers[1:]
    signs = list(map(int, input().split()))
    signs = ["+"] * signs[0] + ["-"] * signs[1] + ["*"] * signs[2] + ["/"] * signs[3]
    answer = []
    for sign_order in set(map("".join, permutations(signs))):
        result = start
        for number, sign in zip(numbers, sign_order):
            if sign == "+":
                result += number
            elif sign == "-":
                result -= number
            elif sign == "*":
                result *= number
            else:
                if result < 0:
                    result = -1 * (abs(result) // number)
                else:
                    result //= number
        answer.append(result)

    print(max(answer))
    print(min(answer))


if __name__ == "__main__":
    _14888()