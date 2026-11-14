import tempfile, os

class InvalidRecord(Exception):
    pass

def parse(line):
    p = line.strip().split(",")
    if len(p) != 3:
        raise InvalidRecord(f"expected 3 fields, found {len(p)}")
    if p[2] not in ("P", "A"):
        raise InvalidRecord(f"invalid status '{p[2]}'")
    return p

data = "101,2026-10-08,P\n102,2026-10-08,A\n103,2026-10-08\n104,2026-10-08,L\n"

with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
    f.write(data)
    name = f.name

a, b, errors = 0, 0, []

with open(name) as f:
    for n, line in enumerate(f, 1):
        try:
            p = parse(line)
            if p[2] == "P":
                a += 1
            else:
                b += 1
        except InvalidRecord as e:
            errors.append((n, str(e)))

print(a, b, errors)
os.remove(name)
