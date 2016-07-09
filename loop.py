#looppy, written by Eric Bearic in the 5th of July, 2016 in the years of our
# lord.
# 7:59:29 7:59:30

import random

X = []
y_vals = []
for i in range(100):
    x, y, z = random.gauss(85, 10), random.gauss(85, 10), random.gauss(85, 10)
    x, y, z = min(100, x), min(100, y), min(100, z)
    avg = (x + y + z) / 3.0
    X.append('[{0}, {1}, {2}],'.format(x, y, z))
    y_vals.append(str(avg) + ',')

for i in X:
    print i

for i in y_vals:
    print i
