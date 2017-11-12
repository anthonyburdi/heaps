"""Compute the running median as values are coming in from a stream."""

# Create a min heap and max heap
# Insert into the max heap if the value is less than the median
# Insert into the min heap if the value is greater than the median
# Keep the min and max heap in balance (within 1 value)
# Then the median is either:
# The average of the root of the min heap and max heap if they are equal size
# The root of the larger tree if they are not

import time

from heap import Heap


def insert(min_heap, max_heap, value, verbose=False):
    """Insert new value."""
    # Compare to current median
    current_median = get_median(min_heap, max_heap)
    # If greater, put into min_heap. If less, put in the max_heap.
    if value >= current_median:
        min_heap.insert(value)
    else:
        max_heap.insert(value)

    # Compare sizes of heaps
    while abs(min_heap.length() - max_heap.length()) > 1:
        # Rebalance
        if verbose:
            print '=====> Rebalancing, current status:'
            print 'Min Heap: {}'.format(min_heap.heap)
            print 'Max Heap: {}'.format(max_heap.heap)
        if min_heap.length() - max_heap.length() > 1:
            root_of_min_heap = min_heap.pop_top()
            if verbose:
                print 'Moving {} from min_heap to max_heap'.format(
                    root_of_min_heap
                )
            max_heap.insert(root_of_min_heap)
            if verbose:
                print 'Move completed, now:'
                print 'Min Heap: {}'.format(min_heap.heap)
                print 'Max Heap: {}'.format(max_heap.heap)
                print '-----------------------'
        else:
            root_of_max_heap = max_heap.pop_top()
            if verbose:
                print 'Moving {} from max_heap to min_heap'.format(
                    root_of_max_heap
                )
            min_heap.insert(root_of_max_heap)
            if verbose:
                print 'Move completed, now:'
                print 'Min Heap: {}'.format(min_heap.heap)
                print 'Max Heap: {}'.format(max_heap.heap)
                print '-----------------------'


def get_median(min_heap, max_heap):
    """Get current median value."""
    # Check to make sure there are enough values:
    if min_heap.peek() and not max_heap.peek():
        return min_heap.peek()
    if max_heap.peek() and not min_heap.peek():
        return max_heap.peek()
    if not (min_heap.peek() and max_heap.peek()):
        return 0

    # Average of both roots if they are equal size
    if min_heap.length() == max_heap.length():
        return (min_heap.peek() + max_heap.peek()) / 2.0

    # If unequal, return the root of the larger heap
    if min_heap.length() > max_heap.length():
        return min_heap.peek()
    else:
        return max_heap.peek()


if __name__ == '__main__':
    # Let's show a simple case in slow motion as numbers are inserted

    # Initialize
    verbose = True
    slow_output = True
    output_step_time = 0.1
    min_heap = Heap(heap_type='min')
    max_heap = Heap(heap_type='max')

    values_to_insert = range(1, 101)
    import random
    random.shuffle(values_to_insert)

    for value in values_to_insert:
        if verbose:
            print 'Inserting: {}'.format(value)
        insert(min_heap, max_heap, value, verbose)
        if verbose:
            print 'Min Heap: {}'.format(min_heap.heap)
            print 'Max Heap: {}'.format(max_heap.heap)
            print 'Median: {}'.format(get_median(min_heap, max_heap))
        if slow_output:
            time.sleep(output_step_time)

    if verbose:
        print 'Final Min Heap: {}'.format(min_heap.heap)
        print 'Final Max Heap: {}'.format(max_heap.heap)
    print 'Final Median: {}'.format(get_median(min_heap, max_heap))
