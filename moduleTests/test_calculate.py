import unittest
from math import pi
import sys

sys.path.append("/Users/kirillkockin/Desktop/isrpo/second-isrpo/geometric_lib")
from calculate import calc


class TestCalcPerimeter(unittest.TestCase):
    def test_calc_circle_perimeter(self):
        # Arrange
        fig = "circle"
        func = "perimeter"
        size = [3]
        expected_result = pi * 3 * 2

        # Act
        result = calc(fig, func, size)

        # Assert
        self.assertEqual(result, expected_result)

    def test_calc_square_perimeter(self):
        fig = "square"
        func = "perimeter"
        size = [3]
        expected_result = 12

        result = calc(fig, func, size)

        self.assertEqual(result, expected_result)

    def test_calc_triangle_perimeter(self):
        fig = "triangle"
        func = "perimeter"
        size = [10, 12, 15]
        expected_result = 37

        result = calc(fig, func, size)

        self.assertEqual(result, expected_result)


class TestCalcArea(unittest.TestCase):
    def test_calc_circle_area(self):
        fig = "circle"
        func = "area"
        size = [5]
        expected_result = 25 * pi

        result = calc(fig, func, size)

        self.assertEqual(result, expected_result)

    def test_calc_square_area(self):
        fig = "square"
        func = "area"
        size = [10]
        expected_result = 100

        result = calc(fig, func, size)

        self.assertEqual(result, expected_result)

    def test_calc_triangle_area(self):
        fig = "triangle"
        func = "area"
        size = [9, 12, 15]
        expected_result = 54

        result = calc(fig, func, size)

        self.assertEqual(result, expected_result)


class TestCalcInvalidFigure(unittest.TestCase):
    def test_calc_invalid_figure(self):
        fig = "tetrahedron"
        func = "area"
        size = [4]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)


class TestCalcInvalidFunction(unittest.TestCase):
    def test_calc_invalid_function(self):
        fig = "circle"
        func = "height"
        size = [1]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)


class TestCalcIntegerNegative(unittest.TestCase):
    def test_calc_invalid_size_values_triangle(self):
        fig = "triangle"
        func = "area"
        size = [-3, 4, 5]
        expected_result = "Размеры должны быть положительными числами"

        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

        self.assertEqual(str(context.exception), expected_result)

    def test_calc_invalid_size_values_circle(self):
        fig = "circle"
        func = "area"
        size = [-3]
        expected_result = "Размеры должны быть положительными числами"

        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

        self.assertEqual(str(context.exception), expected_result)

    def test_calc_invalid_size_values_square(self):
        fig = "square"
        func = "area"
        size = [-5]
        expected_result = "Размеры должны быть положительными числами"

        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

        self.assertEqual(str(context.exception), expected_result)


class TestCalcInvalidCountSize(unittest.TestCase):
    def test_calc_invalid_count_size(self):
        fig = "triangle"
        func = "area"
        size = [5]
        expected_result = "Ожидается 3 параметров для triangle и функции area"

        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

        self.assertEqual(str(context.exception), expected_result)

    def test_calc_invalid_count_size_null(self):
        fig = "square"
        func = "perimeter"
        size = []
        expected_result = "Ожидается 1 параметров для square и функции perimeter"

        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

        self.assertEqual(str(context.exception), expected_result)
