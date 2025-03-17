from math import pi , sin , cos

hValues = [0.001, 0.01, 0.1]

for h in hValues:
    print(f"Results for h = {h}")
    x = -pi
    while x <= pi:
        approx_derivative = (sin(x + h) - sin(x)) / h
        actual_derivative = cos(x)
        print(f"{actual_derivative}: {approx_derivative}")
        x += h
        