# Goal is to animate is the kinetic and potential energy of a ball, 
# while the ball jumps up and down

from ball import Ball
import numpy as np
import matplotlib.pyplot as plt

b = Ball(1, 10)
for i in range(1000):
    b.update(0.02)

print(b.heights[1])




fix, ax = plt.subplots()
ax.plot(b.heights)
plt.show()