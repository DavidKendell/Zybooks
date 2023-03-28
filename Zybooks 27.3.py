from math import sqrt


vals = input() #"(1.5, 2.0) (4.5, 6.0)"
x1, y1, x2, y2 = float(vals[1:4]), float(vals[6:9]), float(vals[12:15]), float(vals[17:20])
print(sqrt((x2-x1)**2 + (y2-y1)**2))