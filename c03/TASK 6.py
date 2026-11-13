trains = {
    "12601": {
        "name": "Chennai Express",
        "stops": [("Chennai", "06:00", "06:10"),
                  ("Katpadi", "08:00", "08:05"),
                  ("Salem", "11:00", "11:10")],
        "days": {"Mon", "Wed", "Fri"}
    },
    "12602": {
        "name": "Bengaluru Mail",
        "stops": [("Bengaluru", "05:00", "05:10"),
                  ("Katpadi", "09:30", "09:35")],
        "days": {"Tue", "Thu"}
    }
}

print("Third station:", trains["12601"]["stops"][2][0])

index = {}
for no, t in trains.items():
    for stop in t["stops"]:
        index.setdefault(stop[0], []).append(no)

station = "Katpadi"
day = "Fri"
result = []

for no in index.get(station, []):
    t = trains[no]
    if day in t["days"]:
        for s, a, d in t["stops"]:
            if s == station:
                result.append((d, no, t["name"]))

print("Trains:", sorted(result))
