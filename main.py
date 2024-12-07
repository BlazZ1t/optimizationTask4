import numpy as np

def bisection_func(x):
    return x**3 - 6 * x**2 + 11 * x - 6

def golden_section_func(x):
    return (x - 2) ** 2 + 3

def gradient_ascent_func(x):
    return -1 * x**2 + 4 * x + 1

def gradient_ascent_derivative(x):
    return -2 * x + 4


def get_input() -> tuple[float, float, float]:
    left_border = float(input())
    right_border = float(input())
    tolerance = float(input())

    return (left_border, right_border, tolerance)


def bisection_method():
    left_border, right_border, tolerance = get_input()
    while True:
        mid_point = (left_border + right_border) / 2
        if abs(bisection_func(mid_point)) < tolerance:
            return mid_point
        if (bisection_func(mid_point) < 0):
            left_border = mid_point
        else:
            right_border = mid_point

def golden_section():
    left_border, right_border, tolerance = get_input()
    phi = (1 + np.sqrt(5)) / 2  # Golden ratio
    resphi = 2 - phi

    x1 = left_border + resphi * (right_border - left_border)
    x2 = right_border - resphi * (right_border - left_border)
    f1 = golden_section_func(x1)
    f2 = golden_section_func(x2)

    while (right_border - left_border) > tolerance:
        if f1 < f2:
            right_border = x2
            x2 = x1
            f2 = f1
            x1 = left_border + resphi * (right_border - left_border)
            f1 = golden_section_func(x1)
        else:
            left_border = x1
            x1 = x2
            f1 = f2
            x2 = right_border - resphi * (right_border - left_border)
            f2 = golden_section_func(x2)

    x_min = (left_border + right_border) / 2
    f_min = golden_section_func(x_min)
    return float(x_min), float(f_min)

def gradient_ascent():
    x0, alpha, N = get_input()
    x = x0

    for _ in range(int(N)):
        grad = gradient_ascent_derivative(x)
        x = x + alpha * grad

    x_max = x
    f_max = gradient_ascent_func(x_max)
    return float(x_max), float(f_max)

if __name__ == "__main__":
    print(bisection_method())
    print(golden_section())
    print(gradient_ascent())