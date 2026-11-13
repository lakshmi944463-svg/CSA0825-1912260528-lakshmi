def normalise(text):
    return text.replace(" ", "").replace("-", "").upper()

def is_valid(s):
    return (len(s) in (9, 10) and
            s[:2].isalpha() and
            s[2:4].isdigit() and
            s[4:-4].isalpha() and
            s[-4:].isdigit())

reg = input("Enter registration number: ")
reg = normalise(reg)

if is_valid(reg):
    print("Valid")
else:
    print("Invalid")
