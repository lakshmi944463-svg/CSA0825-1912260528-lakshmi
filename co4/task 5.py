def read_file():
    return ["Anu", "Ravi", "Sam"]

def statistics(data):
    return len(data)

def report(data):
    print("Student List:", data)
    print("Total Students:", statistics(data))

if __name__ == "__main__":
    data = read_file()
    report(data)
