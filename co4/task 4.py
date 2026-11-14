import tempfile, os

folder = tempfile.mkdtemp()
os.chdir(folder)

def save_returns(books):
    with open("returns.log", "a") as f:
        for b in books:
            f.write(b + "\n")

def process(file):
    try:
        with open(file) as f:
            save_returns(f.read().splitlines())
    except FileNotFoundError:
        with open("error.log", "a") as f:
            f.write(file + " missing\n")

for i in range(1, 4):
    with open(f"day{i}.txt", "w") as f:
        f.write(f"Book{i}\n")

for i in range(1, 4):
    process(f"day{i}.txt")

print(open("returns.log").read())
print("Completed")
