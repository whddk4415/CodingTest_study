a, b = map(int, input().split())
count = 0
check = False
while b > a :

  if (b % 2 != 0) and (str(b)[-1] != '1'):
    count = -1
    break

  if str(b)[-1] == '1':
    b = int(str(b)[:-1])
    count += 1

  elif b % 2 == 0:
    b = b // 2
    count += 1

  if b == a:
    print(count + 1)
    check = True
    break

if check == False:
  print(-1)

