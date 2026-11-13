import random

readings = [round(random.uniform(0, 60), 1) for i in range(365)]

weekly = [sum(readings[i:i+7]) for i in range(0, 364, 7)]

print("Weekly totals:", weekly)
print("Wettest week:", max(weekly))
print("Driest week:", min(weekly))

print("Maximum rainfall:", max(readings))
print("Minimum rainfall:", min(readings))

dry = [i+1 for i, x in enumerate(readings) if x == 0]
print("Dry days:", dry)

avg = [sum(readings[i:i+7])/7 for i in range(359)]
print("7-day moving average:", avg[:5])

print("Second week:", readings[7:14])
print("Last 7 days:", readings[-7:])
