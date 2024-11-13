from math import pi
import unittest
import sys

sys.path.append("/Users/kirillkockin/Desktop/isrpo/second-isrpo/geometric_lib")
from circle import area, perimeter


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Arrange
        radius = 3
        expected_area = pi * 3**2

        # Act
        result = area(radius)

        # Assert
        assert result == expected_area, f"Expected {expected_area}, but got {result}"


class TestCirclePerimeter(unittest.TestCase):
    def test_area(self):
        radius = 3
        expected_perimeter = pi * 3 * 2

        result = perimeter(radius)

        assert (
            result == expected_perimeter
        ), f"Expected {expected_perimeter}, but got {result}"
