data = [
    "101,Anu,2500",
    "102,Ravi,3000",
    "103,Sam,abc",
    "104,Tom,1500"
]

total = 0
report = []
rejected = []

for line in data:
    try:
        p = line.split(",")
        amount = float(p[2])
        total += amount
        report.append(p[1] + " " + p[2])
    except (ValueError, IndexError):
        rejected.append(line)

print("Student Details:")
for x in report:
    print(x)

print("Total Amount:", total)
print("Rejected Records:", rejected)
