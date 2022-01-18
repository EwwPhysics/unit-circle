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

DEGREES = [0, 30, 45, 60, 90,
           180, 150, 135, 120, 90]
DEGREES.extend([360 - x if x != 0 else 0 for x in DEGREES])

plt.scatter(x_vals, y_vals)

for x, y, rad, deg in zip(x_vals, y_vals, RADIANS, DEGREES):
    plt.annotate(f"{rad} -- ({x:.2f}, {y:.2f})", (x, y), (x, y + .09))
    plt.annotate(f"{deg}°", (x, y), (x, y + .02))
    plt.plot([0, x], [0, y], "g")

plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])

circle = plt.Circle((0, 0), 1, fill=False)

ax = fig.gca()

ax.add_patch(circle)

plt.show()

