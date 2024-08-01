#!/usr/bin/env python

import numpy as np
import numpy.linalg as la

omega = np.loadtxt("BTE.omega")
v = np.loadtxt("BTE.v")
vnorm = la.norm(v, axis=1).reshape(omega.shape, order="F")
gruneisen = np.loadtxt("BTE.gruneisen")
nbranches = omega.shape[1]
for i in range(nbranches):
    np.savetxt(f"threecolumns_{i+1:d}.txt",  np.c_[omega[:, i], vnorm[:, i], gruneisen[:, i]])
