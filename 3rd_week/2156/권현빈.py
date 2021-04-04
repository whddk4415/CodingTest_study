import sys
num = int(sys.stdin.readline().rstrip())
i = 0
list = []
while i < num:
    i += 1
    list.append(int(input()))


def solution():
    dp = []
    dp.append(list[0])

    if(len(list) == 1):
        print(dp[0])
        return
    elif(len(list) == 2):
        print(list[0] + list[1])
        return
    else:
        dp.append(list[0] + list[1])
        dp.append(max(list[1]+list[2],
                      list[0]+list[2], list[0]+list[1]))
        i = 3
        while i < num:
            dp.append(max(dp[i-3]+list[i-1]+list[i], dp[i-2]+list[i], dp[i-1]))
            i += 1

    print(dp[num - 1])


solution()
