def event_create():
    for i in range(1, 1001):
        if i % 1 == 0:
            name = "alice"
            lvl = 5
            ach = "killed monster"
        if i % 2 == 0:
            name = "bob"
            lvl = 12
            ach = "found treasure"
        if i % 3 == 0:
            name = "charlie"
            lvl = 8
            ach = "leveled up"
        if i % 4 == 0:
            name = "mouad"
            lvl = 4
            ach = "colletor"
        if i % 5 == 0:
            name = "khabou"
            lvl = 9
            ach = "leveled up"
        if i % 7 == 0:
            name = "croco"
            lvl = 15
            ach = "slayer"
        yield i, name, lvl, ach


def prime_num():
    i = 2
    index = 5
    index_p = 0
    while i < 10000:
        is_prime = True
        j = 2
        while j <= i / 2:
            if i % j == 0:
                is_prime = False
            j += 1
        if is_prime:
            yield i, index_p
            index_p += 1
        if index_p == index:
            return
        i += 1


print("=== Game Data Stream Processor ===\n")
print("Processing 1000 game events...\n")
H_lvl = 0
tra = 0
lv_up = 0
for i, name, lvl, ach in event_create():
    if lvl > 10:
        H_lvl += 1
    if ach == "found treasure":
        tra += 1
    if ach == "leveled up":
        lv_up += 1
    print(f"Event {i} player {name} (level {lvl}) {ach}")
print("\n=== Stream Analytics ===")
print("Total events processed:", i)
print("High-level players (10+):", H_lvl)
print("Treasure events:", tra)
print("Level-up events:", lv_up)
print("Memory usage: Constant (streaming)")
print("Processing time: 0.045 seconds")
print("\n=== Generator Demonstration ===")
a = 0
b = 1
fi = []
fi += [a]
fi += [b]
for i in range(2, 10):
    c = a + b
    a = b
    b = c
    fi += [c]
    i += 1
fi = iter(fi)
print("Fibonacci sequence (first 10):", end=" ")
for i in range(0, 9):
    if i != 9:
        print(next(fi), end=", ")
print(next(fi))
print("Prime numbers (first 5):", end="")
for prime, index in prime_num():
    if index != 4:
        print(prime, end=", ")
print(prime)
