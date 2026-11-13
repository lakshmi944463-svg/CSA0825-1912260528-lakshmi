readings = [3, 5, 9, 12, 55, -60, 7, 4]

valid = [x for x in readings if -50 <= x <= 50]
fahrenheit = [x*9/5+32 for x in valid]
alarm = [i for i, x in enumerate(readings)
         if -50 <= x <= 50 and not 2 <= x <= 8]

print("Valid readings:", valid)
print("Fahrenheit:", fahrenheit)
print("Alarm minutes:", alarm)

print("Using map:", list(map(lambda x: x*9/5+32, valid)))
