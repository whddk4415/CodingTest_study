import sys

n = int(input())

num_list = list(map(int,sys.stdin.readline().split()))
max_list = [0 for _ in range(n)]
max_list[0] = num_list[0]

for i in range(1,n):
    max_list[i] = max(num_list[i],max_list[i-1]+num_list[i])

print(max(max_list))