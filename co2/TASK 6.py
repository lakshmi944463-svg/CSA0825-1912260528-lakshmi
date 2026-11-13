Vfrom functools import lru_cache

calls = 0

def ways_naive(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_naive(n-1) + ways_naive(n-2)

@lru_cache(None)
def ways_memo(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_memo(n-1) + ways_memo(n-2)

calls = 0
ways_naive(25)
print("Naive calls:", calls)

calls = 0
ways_memo(25)
print("Memo calls:", calls)

n = int(input("Enter steps: "))
a, b = 1, 1

for i in range(n):
    a, b = b, a+b

print("Ways:", a)
