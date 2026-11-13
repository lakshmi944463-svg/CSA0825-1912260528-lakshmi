otp = "1234"
attempt = 0

while attempt < 3:
    user = input("Enter OTP: ")

    if user == "":
        continue
    elif user == otp:
        print("Verified")
        break
    else:
        attempt += 1

if attempt == 3:
    print("Account Locked")
