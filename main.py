from math import sqrt
import argparse


def solve_equation(*coeffs):
    a, b, c = coeffs[0]

    if a == 0:
        return -(c / b)
    d = b * b - 4 * a * c
    if d < 0:
        raise ArithmeticError('D < 0, complex roots are not supported')
    elif d == 0:
        return -b / (2 * a)
    else:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return x1, x2


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve quadratic equation')
    parser.add_argument('-k', type=int, nargs=3,
                        help='equation coefficients')

    args = parser.parse_args()
    res = solve_equation(args.k)
    print(res)
