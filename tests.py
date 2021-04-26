import unittest
from main import solve_equation


class TestEquationSolve(unittest.TestCase):
    def test_negative_d(self):
        self.assertRaises(ArithmeticError, solve_equation, 2, 2, 2)

    def test_zero_a(self):
        res = solve_equation(0, 2, 4)
        self.assertEqual(res, -2)

    def test_zero_d(self):
        res = solve_equation(2, 4, 2)
        self.assertEqual(res, -1)

    def test_positive_d(self):
        res = solve_equation(1, 4, 3)
        self.assertEqual(res, (-1, -3))


if __name__ == '__main__':
    unittest.main()
