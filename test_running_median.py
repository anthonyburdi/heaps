"""Unit tests for running_median.py."""
import unittest

from heap import Heap
import running_median
# insert(min_heap, max_heap, value, verbose=False)
# get_median(min_heap, max_heap)


class TestRunningMedian(unittest.TestCase):
    """Test setting up and modifying a heap, not considering edge cases."""

    def setUp(self):
        """Create objects for testing."""
        self.min_heap = Heap(heap_type='min')
        self.max_heap = Heap(heap_type='max')

        values_to_insert = range(1, 11)
        for value in values_to_insert:
            running_median.insert(self.min_heap, self.max_heap, value)

        # Let's try another case
        self.min_heap_b = Heap(heap_type='min')
        self.max_heap_b = Heap(heap_type='max')
        values_to_insert = [55, 47, 42, 31, 32, 33, 34, 25, 26]
        for value in values_to_insert:
            running_median.insert(self.min_heap_b, self.max_heap_b, value)

        # Let's try another case with floats
        self.min_heap_float = Heap(heap_type='min')
        self.max_heap_float = Heap(heap_type='max')
        values_to_insert = [
            71.37819952358689,
            38.938194459848106,
            98.38776214046379,
            87.22333338258774,
            26.73249446791074,
            77.30212928674027,
            94.28293805195062,
            92.83993074506832,
            48.933894405944265,
            97.2399013926571
        ]
        for value in values_to_insert:
            running_median.insert(
                self.min_heap_float,
                self.max_heap_float,
                value
            )

    def test_insert(self):
        """Make sure both heaps are formed correctly."""
        self.assertEqual(
            self.min_heap.heap,
            [6, 7, 8, 10, 9]
        )
        self.assertEqual(
            self.max_heap.heap,
            [5, 4, 2, 1, 3]
        )
        self.assertEqual(
            self.min_heap_b.heap,
            [34, 42, 47, 55]
        )
        self.assertEqual(
            self.max_heap_b.heap,
            [33, 31, 32, 25, 26]
        )
        self.assertEqual(
            self.min_heap_float.heap,
            [
                87.22333338258774,
                92.83993074506832,
                94.28293805195062,
                98.38776214046379,
                97.2399013926571
            ]
        )
        self.assertEqual(
            self.max_heap_float.heap,
            [
                77.30212928674027,
                71.37819952358689,
                26.73249446791074,
                38.938194459848106,
                48.933894405944265
            ]
        )

    def test_get_median(self):
        """Make sure heap is created successfully."""
        self.assertEqual(
            running_median.get_median(self.min_heap, self.max_heap),
            5.5
        )
        self.assertEqual(
            running_median.get_median(self.min_heap_b, self.max_heap_b),
            33
        )
        self.assertEqual(
            running_median.get_median(
                self.min_heap_float,
                self.max_heap_float
            ),
            82.26273133466401
        )

if __name__ == '__main__':
    unittest.main()
