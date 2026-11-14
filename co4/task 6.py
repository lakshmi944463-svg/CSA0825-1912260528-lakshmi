data = [
"101,Anu,CSE,anu@gmail.com,Dance;Singing",
"102,Ravi,ECE,ravi@gmail.com,Music",
"103,Sam,IT,sam@gmail.com,Drama",
"101,Anu,CSE,anu@gmail.com,Dance",
"104,Tom,ECE,tom@gmail.com,Music"
]

seen = set()
events = {}
errors = []
students = []

for line in data:
    try:
        p = line.split(",")
        if len(p) != 5:
            raise ValueError("Invalid record")

        reg, name, dept, email, choices = p

        if reg in seen:
            continue
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email")

        seen.add(reg)
        students.append(name)

        for e in choices.split(";"):
            events.setdefault(e, []).append(name)

    except ValueError as x:
        errors.append(str(x))

print("Master List:", students)
print("Event Details:", events)
print("Total Students:", len(students))
print("Errors:", errors)
print("Registration Completed")
