from collections import deque
queue = deque(input('Enter queue items separated by spaces: ').split())
print('Queue:', list(queue))
if queue: print('Removed:', queue.popleft())
print('After removal:', list(queue))
