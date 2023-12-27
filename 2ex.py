from collections import deque

bites, guests = int(input()), deque()

while (c := input().lower()) != 'start': guests.append(c)

while (c := input().lower()) != 'end':
    bites += int(c.split()[1]) if c.startswith('refill') else (
        (lambda g: print(f"{g} takes bites") if g else print("No more guests left."))(guests.popleft()) if bites >= int(c) and guests else None
    )

print(f"{bites} bites left")
