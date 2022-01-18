import matplotlib.pyplot as plt
from math import sqrt

fig = plt.figure(figsize=(9, 9))

X_QUADRANT = [1, sqrt(3) / 2, sqrt(2) / 2, 1 / 2, 0]
x_vals = X_QUADRANT + [-x for x in X_QUADRANT]
x_vals.extend(x_vals)

Y_QUADRANT = [0, 1 / 2, sqrt(2) / 2, sqrt(3) / 2, 1]
y_vals = Y_QUADRANT + Y_QUADRANT
y_vals.extend([-y for y in y_vals])

RADIANS = ["0", "π / 6", "π / 4", "π / 3", "π / 2", 
            "π", "5π / 6", "3π / 4", "2π / 3", "π / 2",
            "0", "11π / 6", "7π / 4", "5π / 3", "3π / 2",
            "π", "7π / 6", "5π / 4", "4π / 3", "3π / 2"]


plt.scatter(x_vals, y_vals)

for i in range(len(x_vals)):
    x, y, distance = x_vals[i], y_vals[i], RADIANS[i]
    plt.annotate(f"{distance} -- ({x:.2f}, {y:.2f})", (x, y), (x, y + .05))
    plt.plot([0, x], [0, y])


plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])



plt.show()
