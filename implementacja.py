

import numpy as np


WEZLY=2
ELEMENTY=3
WAR_BRZEGOWE=6


def tablicegeometrii(x_0, x_p, n):
    temporary = (x_p - x_0) / (n - 1)
    wezly = np.array([x_0, x_p])

    for i in range(1, n-1, 1):
        wezly = np.block([wezly, i * temporary + x_0])

    elementy = np.array([])
    n = n-1

    return wezly
print(tablicegeometrii(WEZLY,ELEMENTY,WAR_BRZEGOWE))

