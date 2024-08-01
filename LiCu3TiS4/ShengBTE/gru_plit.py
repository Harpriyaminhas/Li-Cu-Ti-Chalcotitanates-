#!/usr/bin/env python

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.xlim(5.0,60)


omega = np.loadtxt("BTE.omega")
gruneisen = np.loadtxt("BTE.gruneisen")

indices = omega > 5.0

omega = omega[indices]
gruneisen = gruneisen[indices]

indices = omega > 5.0

omega = omega[indices]
gruneisen = gruneisen[indices]

plt.figure()
for i in range(omega.shape[1]):

    indices = omega[:, i] > 27.
    plt.scatter(omega[indices, i], gruneisen[indices, i])


plt.xlabel(r"$\omega\;(\mathrm{rad/ps})$")
plt.ylabel(r"$\gamma$")
plt.tight_layout()
plt.show()
