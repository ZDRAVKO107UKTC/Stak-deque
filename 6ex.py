from collections import deque

food = int(input())
orders = list(map(int, input().split()))

max_order = max(orders)
print(max_order)

ordqueue = deque(orders)

while ordqueue and food >= ordqueue[0]:
    food -= ordqueue.popleft()

if not ordqueue:
    print("Orders complete")
else:
    print(f"Remaining orders: {', '.join(map(str, ordqueue))}")
