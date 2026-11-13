calls = [
    "seeds not received",
    "fertiliser price high",
    "seeds price high"
]

stop = {"not", "high"}
count = {}

for text in calls:
    for word in text.split():
        if word not in stop:
            count[word] = count.get(word, 0) + 1

print("Word count:", count)
print("Top words:", sorted(count.items(),
      key=lambda x: x[1], reverse=True)[:3])

records = [
    ("Salem", "Paddy", "Seeds delayed"),
    ("Madurai", "Cotton", "Pump failure"),
    ("Salem", "Cotton", "Price high")
]

district = {}

for d, c, complaint in records:
    district.setdefault(d, []).append(complaint)

print("District complaints:", district)
