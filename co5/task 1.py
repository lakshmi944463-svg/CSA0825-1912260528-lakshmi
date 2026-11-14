import csv
import io

RAW = """station,date,pm25
Adyar,2026-10-01,48
Adyar,2026-10-02,NA
Adyar,2026-10-03,
Guindy,2026-10-01,95
Guindy,2026-10-02,-5
Guindy,2026-10-03,121
Adyar,2026-10-04,1200
"""

def load_clean(data):
    rows = []
    for r in csv.DictReader(io.StringIO(data)):
        v = r["pm25"].strip()
        if v and v != "NA":
            n = float(v)
            if 0 <= n <= 999:
                rows.append((r["station"], r["date"], n))
    return rows

def min_max(values):
    a, b = min(values), max(values)
    return [round((v-a)/(b-a), 3) for v in values]

clean = load_clean(RAW)
print(clean)
print(min_max([r[2] for r in clean]))
