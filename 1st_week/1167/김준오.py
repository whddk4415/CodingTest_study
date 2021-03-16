#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
k = int(input())
d={}

for i in range(1,n+1):
  d[i] = []

for i in range(k):
  a,b = map(int,input().split())
  d[a].append(b)
  d[b].append(a)

#DFS 구현
visited_list = [1]
need_visit = d[1]

while need_visit:
  node = need_visit.pop()

  if node not in visited_list:
    visited_list.append(node)
    need_visit.extend(d[node])

print(len(visited_list)-1)

