"""Test cases for distributed running median."""
import unittest

from distributed_running_median import MedianCalcSystem, MedianWorkerMachine
from heap import Heap
import running_median


class TestMedianCalcSystem(unittest.TestCase):
    """Test setting up and class methods of MedianCalcSystem."""

    def setUp(self):
        """Create objects for testing."""
        self.median_calc_system = MedianCalcSystem(
            number_of_workers=10,
            max_worker_size=1000
        )

    def test_left_middle_worker_id(self):
        """Make sure correct value is returned."""
        self.assertEquals(
            self.median_calc_system.left_middle_worker_id(),
            5
        )

    def test_right_middle_worker_id(self):
        """Make sure correct value is returned."""
        self.assertEquals(
            self.median_calc_system.right_middle_worker_id(),
            6
        )

    def test_insert_first_value(self):
        """Make sure the first value is inserted correctly."""
        self.median_calc_system.insert(5)
        self.assertEqual(
            self.median_calc_system.get_median(),
            5
        )

    def test_insert_second_value(self):
        """Make sure the first two values are inserted correctly."""
        self.median_calc_system.insert(5)
        self.median_calc_system.insert(10)
        self.assertEqual(
            self.median_calc_system.get_median(),
            7.5
        )


if __name__ == '__main__':
    unittest.main()
