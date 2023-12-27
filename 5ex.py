from collections import deque

stack = deque()

for _ in range(int(input())):
    cmd, *args = input().split()

    if cmd == '1':
        stack.append(int(args[0]))
    elif cmd == '2' and stack:
        stack.pop()
    elif cmd == '3' and stack:
        print(max(stack))
    elif cmd == '4' and stack:
        print(min(stack))
    elif cmd == '5':
        print(len(stack))

print("------------------------------------------------------")
print(*reversed(stack))
