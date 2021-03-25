from itertools import product
def _1107():
    channel = input()
    wrong_buttons = set(map(str, input().split())) if int(input()) else set()
    if not (set(channel) & wrong_buttons):
        print(min(abs(100 - int(channel)), len(channel)))
    else:
        channel = int(channel)
        buttons = list(set([str(i) for i in range(10)]) - wrong_buttons)
        answer = abs(100 - channel)
        for i in range(1, len(str(channel)) + 2):
            count = 0
            for prod in product(buttons, repeat=i):
                count+=1
                # current_channel = int(''.join(prod))
                # answer = min(answer, abs(channel - current_channel) + i)
            print(i, count)
        # print(answer)

if __name__ == '__main__':
    _1107()