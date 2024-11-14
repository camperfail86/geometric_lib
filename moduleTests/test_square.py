import unittest
import sys

sys.path.append("/Users/kirillkockin/Desktop/isrpo/second-isrpo/geometric_lib")
from square import area, perimeter


class TestSquareArea(unittest.TestCase):
    def test_area(self):
        # Arrange
        side_length = 5
        expected_area = 25

        # Act
        result = area(side_length)

        # Assert
        assert result == expected_area, f"Expected {expected_area}, but got {result}"


class TestSquarePerimeter(unittest.TestCase):
    def test_perimeter(self):
        side_length = 5
        expected_perimeter = 20

        result = perimeter(side_length)

        assert (
            result == expected_perimeter
        ), f"Expected {expected_perimeter}, but got {result}"
