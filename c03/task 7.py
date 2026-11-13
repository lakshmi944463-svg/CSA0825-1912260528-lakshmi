def number(n):
    return "".join(x for x in n if x.isdigit())[-10:]

contacts = [
    {"name": "Ravi", "number": "+91 98400 12345"},
    {"name": "Anitha", "number": "99620-11111"},
    {"name": "Ravi", "number": "9840012345"},
    {"name": "Kumar", "number": "90030 22222"}
]

merged = {}

for c in contacts:
    n = number(c["number"])
    if n not in merged:
        merged[n] = set()
    merged[n].add(c["name"])

print("Merged contacts:")
for n, names in merged.items():
    print(names, n)
