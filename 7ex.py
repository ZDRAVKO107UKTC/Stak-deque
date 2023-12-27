from collections import deque

clothes = list(map(int, input().split()))
capacity = int(input())

clothes_stack = deque(clothes)
shelves_count = 0

while clothes_stack:
    current_shelf_capacity = capacity
    while clothes_stack and current_shelf_capacity >= clothes_stack[-1]:
        current_shelf_capacity -= clothes_stack.pop()
    
    shelves_count += 1

print(shelves_count)
