x, y = map(int, input().split(" "))
xx = (x / 100) + 1
yy = (y / 100) + 1
tt = xx * yy
print("%.6f" % (tt - 1) * 100)
