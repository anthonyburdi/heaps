"""Simple implementation of a distributed approach to the running median."""
from heap import Heap
import running_median

# Worker machine class, with type of heap contained, top node accessable
# New number compared to current median (is current median if first number)
# If greater than median, then compared to 2 machines right of middle
# Machines to right of middle are min heaps
# If lower than min of machine 2 over, insert into machine 1 over
# If larger than min of machine 2 over, compare to machine 3 over until
# it fits or run out of machines
# Move similarly to the left if num less than median
# Rebalance between two sets of machines
# Median is avg of top 2 middle nodes, or top node of larger

# System class which instantiates and coordinates all workers
# Spawn new workers and rebalance if size is too big
# (Let's keep this simple since it's all running on one machine)


class MedianCalcSystem(object):
    """A system of workers to calculate running medians."""

    def __init__(
        self,
        number_of_workers=10,
        max_worker_size=1000,
        allowable_offset=2
    ):
        """System parameters and initialization."""
        self.number_of_workers = number_of_workers
        self.max_worker_size = max_worker_size
        self.allowable_offset = allowable_offset
        self.current_median = None

        # Set up workers. Lower half max heaps, upper half min heaps
        max_workers = [
            MedianWorkerMachine(
                id_num=n, max_size=self.max_worker_size, heap_type='max'
            )
            for n in range(1, (self.number_of_workers + 1) / 2 + 1)
        ]
        min_workers = [
            MedianWorkerMachine(
                id_num=n, max_size=self.max_worker_size, heap_type='min'
            )
            for n in range(
                (self.number_of_workers + 1) / 2 + 1,
                self.number_of_workers + 1
            )
        ]

        self.workers = dict(zip(
            range(1, number_of_workers + 1), max_workers + min_workers
        ))

    def left_middle_worker_id(self):
        """Return the id of the worker to the left of the middle."""
        return self.number_of_workers / 2

    def right_middle_worker_id(self):
        """Return the id of the worker to the right of the middle."""
        return self.number_of_workers / 2 + 1

    def get_median(self):
        """Get the median value."""
        return running_median.get_median(
            self.workers[self.left_middle_worker_id()].heap,
            self.workers[self.right_middle_worker_id()].heap
        )

    def rebalance_check(self, allowable_offset):
        """Check to see if a rebalance is needed."""
        pass

    def rebalance(self):
        """Rebalance workers."""
        pass

    def check_if_worker_nearing_capacity(self, worker_id, capacity_limit=0.9):
        """Test if a worker is at capacity limit % of max size."""
        pass

    def check_if_any_worker_nearing_capacity(self, capacity_limit=0.9):
        """Check all workers for any nearing capacity."""
        pass

    def add_workers(self, num_to_add):
        """Add more workers (in multiples of 2)."""
        pass

    def insert(self, value):
        """Insert a value into the system."""
        # if this is the first value, just insert it to the left of middle
        if not self.current_median:
            self.workers[self.left_middle_worker_id()].heap.insert(value)
            return

        if value >= self.current_median:
            # Find worker to right of middle for it
            for worker_id in range(self.right_middle_worker_id(), self.number_of_workers + 1):
                next_worker_id = worker_id + 1

                if next_worker_id > self.number_of_workers:
                    break

                # if worker at worker_id is empty, just insert
                if self.workers[worker_id].size() == 0:
                    self.workers[worker_id].insert(value)
                    break

                # if value is greater than root of worker_id but lower than
                # root of next_worker_id, then insert into






class MedianWorkerMachine(object):
    """A worker machine for calculating running median."""

    def __init__(self, id_num, max_size, heap_type):
        """Initialize worker."""
        self.id_num = id_num
        self.max_size = max_size
        self.heap_type = heap_type
        self.heap = Heap(heap_type=heap_type)

    def size(self):
        """Return the current size of the worker heap."""
        return self.heap.length()


if __name__ == '__main__':

    system = MedianCalcSystem()

    for idx, worker in system.workers.iteritems():
        print idx, worker.heap_type
