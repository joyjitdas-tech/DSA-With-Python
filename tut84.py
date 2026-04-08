#deque class in python->basicaly a doubly linked list

from collections import deque

q = deque()
q.append(8)
q.append(9)
q.append(10)
q.appendleft(1)
print(q)
q.pop()
print(q)
q.popleft()
print(q)