import pandas as pd
import sqlite3
import time
import cProfile

data = [
    ("Adyar", "2026-10-01", 48),
    ("Adyar", "2026-10-01", 60),
    ("Guindy", "2026-10-01", 95),
    ("Guindy", "2026-10-02", 121)
]

def python_method():
    result = {}
    for s, d, v in data:
        result.setdefault((s, d), []).append(v)
    return {k: sum(v)/len(v) for k, v in result.items()}

def pandas_method():
    df = pd.DataFrame(data, columns=["station", "day", "pm25"])
    return df.groupby(["station", "day"])["pm25"].mean()

def sql_method():
    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE aq (station, day, pm25)")
    con.executemany("INSERT INTO aq VALUES (?, ?, ?)", data)
    result = con.execute(
        "SELECT station, day, AVG(pm25) FROM aq GROUP BY station, day"
    ).fetchall()
    con.close()
    return result

for method in [python_method, pandas_method, sql_method]:
    start = time.perf_counter()
    print(method())
    print("Time:", time.perf_counter() - start)

cProfile.run("python_method()")
