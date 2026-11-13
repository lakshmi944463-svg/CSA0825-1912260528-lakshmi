import time

def using_plus(items):
    result = ""
    for x in items:
        result += x + ";"
    return result

def using_join(items):
    return ";".join(items) + ";"

n = 200000
items = [f"Item{i}:Rs{i % 50}" for i in range(n)]

start = time.perf_counter()
a = using_plus(items)
t1 = time.perf_counter() - start

start = time.perf_counter()
b = using_join(items)
t2 = time.perf_counter() - start

print(a == b)
print("Plus time:", t1)
print("Join time:", t2)
