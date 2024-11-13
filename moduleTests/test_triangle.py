import unittest
import sys

sys.path.append("/Users/kirillkockin/Desktop/isrpo/second-isrpo/geometric_lib")
from triangle import area, perimeter


class TestTriangleArea(unittest.TestCase):
    def test_valid_triangle(self):
        # Arrange
        a, b, c = 3, 4, 5
        expected_area = 6

        # Act
        result = area(a, b, c)

        # Assert
        assert result == expected_area, f"Expected {expected_area}, but got {result}"


class TestTrianglePerimeter(unittest.TestCase):
    def test_area(self):
        a, b, c = 3, 4, 5
        expected_perimeter = 12

        result = perimeter(a, b, c)

        assert (
            result == expected_perimeter
        ), f"Expected {expected_perimeter}, but got {result}"
