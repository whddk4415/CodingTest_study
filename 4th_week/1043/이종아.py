import sys
input = sys.stdin.readline
from collections import deque
def _1043():
    N, M = map(int, input().split())
    truth = set(map(int, input().split()[1:]))
    parties = deque([set(map(int, input().split()[1:])) for _ in range(M)])
    if len(truth) == 0:
        print(M)
    else:
        while True:
            init_truth_num = len(truth)
            for _ in range(len(parties)):
                party = parties.popleft()
                if truth & party:
                    truth |= party
                else:
                    parties.append(party)
            if init_truth_num == len(truth):
                print(len(parties))
                return

if __name__ == '__main__':
    _1043()