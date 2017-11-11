"""Unit tests for MinHeap and MaxHeap."""
import unittest

from heap import Heap


class TestMaxHeap(unittest.TestCase):
    """Test setting up and modifying a heap, not considering edge cases."""

    def setUp(self):
        """Create objects for testing."""
        self.test_heap = Heap(heap_type='max')
        values_to_insert = [55, 47, 42, 31, 32, 33, 34, 25, 26]
        for value in values_to_insert:
            self.test_heap.insert(value)

    def test_output(self):
        """Make sure heap is created successfully."""
        self.assertEqual(
            self.test_heap.heap,
            [55, 47, 42, 31, 32, 33, 34, 25, 26]
        )

    def test_pop_top(self):
        """Test popping the top of the heap."""
        top_node_value = self.test_heap.pop_top()
        self.assertEqual(top_node_value, 55)
        self.assertEqual(self.test_heap.peek(), 47)
        self.assertEqual(self.test_heap.heap, [47, 32, 42, 31, 26, 33, 34, 25])

        # let's pop again and check
        top_node_value = self.test_heap.pop_top()
        self.assertEqual(top_node_value, 47)
        self.assertEqual(self.test_heap.peek(), 42)
        self.assertEqual(self.test_heap.heap, [42, 32, 34, 31, 26, 33, 25])

    def test_insert(self):
        """Test inserting several values."""
        self.test_heap.insert(100)
        self.test_heap.insert(15)
        self.test_heap.insert(38)
        self.assertEqual(
            self.test_heap.heap,
            [100, 55, 42, 31, 47, 38, 34, 25, 26, 32, 15, 33]
        )


class TestMinHeap(unittest.TestCase):
    """Test setting up and modifying a heap, not considering edge cases."""

    def setUp(self):
        """Create objects for testing."""
        self.test_heap = Heap(heap_type='min')
        values_to_insert = [55, 47, 42, 31, 32, 33, 34, 25, 26]
        for value in values_to_insert:
            self.test_heap.insert(value)

    def test_output(self):
        """Make sure heap is created successfully."""
        self.assertEqual(
            self.test_heap.heap,
            [25, 26, 33, 31, 42, 47, 34, 55, 32]
        )

if __name__ == '__main__':
    unittest.main()
