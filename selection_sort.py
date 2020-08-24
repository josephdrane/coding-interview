
import unittest
from typing import List as Array


def findSmallest(arr: Array) -> int:
    """
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    
    return smallest_index


def selectionSort(arr: Array) -> Array:
    """
    """
    newArr = []
    for _ in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    
    return newArr


class TestSelectionSort(unittest.TestCase):

    def test_sort(self):
        input = [5, 3, 6, 2, 10, 45, 33, 23, 14, 77]    
        output = [2, 3, 5, 6, 10, 14, 23, 33, 45, 77]
        self.assertEqual(selectionSort(input), output, "Test fort failed :(")


if __name__ == '__main__':
    unittest.main()