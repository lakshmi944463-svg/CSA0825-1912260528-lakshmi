import time

def recursive(n):
    if n <= 1:
        return 1
    return recursive(n-1) + recursive(n-2)

def iterative(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a+b
    return a

n = int(input("Enter steps: "))

start = time.perf_counter()
if n <= 30:
    recursive(n)
print("Recursive time:", time.perf_counter()-start)

start = time.perf_counter()
iterative(n)
print("Iterative time:", time.perf_counter()-start)
