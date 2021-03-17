n = int(input())

arr_cost = []   #문제에서 주어지는 전체 RGB 금액 저장 배열
for i in range(n):
  arr_cost.append(list(map(int,input().split())))

result = []   #누적된 비용 저장 배열
result.append(arr_cost[0])

for i in range(1,n):
  temp_0 = min(result[i-1][1],result[i-1][2]) + arr_cost[i][0]
  temp_1 = min(result[i-1][0],result[i-1][2]) + arr_cost[i][1]
  temp_2 = min(result[i-1][0],result[i-1][1]) + arr_cost[i][2]
  result.append([temp_0,temp_1,temp_2])

print(min(result[n-1][0],result[n-1][1],result[n-1][2]))