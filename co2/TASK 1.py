units = int(input("Enter units: "))
ration = input("Ration card (yes/no): ").lower()
age = input("Age above 80 (yes/no): ").lower()

if units <= 100:
    print("Full Subsidy")
elif units <= 200 and ration == "yes":
    print("Partial Subsidy")
elif units > 200 and age == "yes":
    print("Special Eligibility")
else:
    print("No Subsidy")
