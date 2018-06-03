# -*- coding: utf-8 -*-
"""
Author: Yiping Deng
"""

import numpy as np
import matplotlib.pyplot as plt

Vs = 10.0
R = 1000.0
L = 0.001
Iini = 0.003

def Isolved(t):
  # the solution to ODE
  return Vs / R + ((Iini * R - Vs)/R) *np.exp((-R/L) * t)

def D(y):
  # the derivative with respect to y
  return (Vs - y * R) / L

def euler(Df,f_start, start, stop, num):
  # implementation of Euler's method
  x = start
  y = f_start
  step = (stop - start) / num
  while x <= stop:
    yield y
    x += step
    y = Df(y) * step + y

def eulerX(start, stop, num):
  # the x-axis for Euler's method
  x = start
  step = (stop - start) / num
  while x <= stop:
    yield x
    x += step

# the solution plot - Blue color
x = np.linspace(0, 0.000002, 200)
y = Isolved(x)
plt.plot(x, y)
print(x, y)


# with 5 iteration - Green color
x1 = list(eulerX(0, 0.000002, 5))
y1 = list(euler(D, Iini, 0, 0.000002, 5))

plt.plot(x1,y1)
print(x1, y1)

# with 10 iteration - Red color
x2 = list(eulerX(0, 0.000002, 10))
y2 = list(euler(D, Iini, 0, 0.000002, 10))
plt.plot(x2, y2)
print(x2, y2)

# with 20 iteration - Violet color
x3 = list(eulerX(0, 0.000002, 20))
y3 = list(euler(D, Iini, 0, 0.000002, 20))
plt.plot(x3, y3)
print(x3, y3)
plt.show()
