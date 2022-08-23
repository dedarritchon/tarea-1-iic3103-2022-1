import numpy as np


point_a = (38.851497,-77.04796)
point_b = (-33.390084,-70.794254)

p1 = [38.851497, -77.04796]
p2 = [-33.390084, -70.794254]

def hanging_line(point1, point2):
    import numpy as np

    a = (point2[1] - point1[1])/(np.cosh(point2[0]) - np.cosh(point1[0]))
    b = point1[1] - a*np.cosh(point1[0])
    x = np.linspace(point1[0], point2[0], 100)
    y = a*np.cosh(x) + b

    return x, y