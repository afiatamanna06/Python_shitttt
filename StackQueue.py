from collections import deque

myqueue = deque(('p', 'q', 'r'))
print(myqueue)
myqueue.append('s')
print(myqueue)
myqueue.popleft()
print(myqueue)
mylist = [1, 2, 3, 4, 5]
print(mylist)
mylist.append(9)
print(mylist)
mylist.pop()
print(mylist)
