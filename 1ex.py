from collections import deque

opashka = deque()

while True:
    klienti = input().lower()

    if klienti == "end":
        remaining_people = len(opashka)
        print("\n".join(opashka))
        print(f"{remaining_people} people remaining.")
        break

    elif klienti == "paid":
        print("\n".join(opashka))
        opashka.clear()

    else:
        opashka.append(klienti)
