import heapq
def _16953():
    A, B = map(int, input().split())
    queue = [(-A, 0)]
    while queue:
        a, count = heapq.heappop(queue)
        if -a == B:
            print(count+1)
            return
        if a * 2 >= -B:
            heapq.heappush(queue, (a*2, count+1))
        if (a*10 - 1) >= -B:
            heapq.heappush(queue, (a*10 - 1, count+1))
    print(-1)
if __name__ == '__main__':
    _16953()
