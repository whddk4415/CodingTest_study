
N = int(input())
M = int(input())

if M > 0 :
  error_list = input().split()

mini = 9999999

for i in range(0,1000001):
  if len(list(set(str(i))&set(error_list))) == 0:
    if abs(N-i) < mini:
      mini = abs(N-i)
      result = i

answer = min(abs(N-100),mini+len(str(result)))

print(answer)