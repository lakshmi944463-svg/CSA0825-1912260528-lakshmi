import copy

bad = [[0]*4]*3
bad[0][1] = 7
print("Bad list:", bad)

good = [[0]*4 for i in range(3)]
good[0][1] = 7
print("Good list:", good)

stops = {(13.08, 80.27): "Chennai",
         (13.04, 80.23): "T Nagar"}
print("Bus stop:", stops[(13.04, 80.23)])

a = [1, 2, 3]
b = a
b.append(4)
print("Alias:", a)

x = [[1, 2], [3, 4]]
y = copy.copy(x)
z = copy.deepcopy(x)

x[0].append(5)
print("Original:", x)
print("Shallow copy:", y)
print("Deep copy:", z)
