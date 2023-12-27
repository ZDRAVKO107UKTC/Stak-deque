from collections import deque

m = input()
n = [int(num) for num in m.split(", ")]


stack = deque(n)
reversed_numbers = []

while stack:
    reversed_numbers.append(stack.pop())

print(" ".join(map(str, reversed_numbers)))
