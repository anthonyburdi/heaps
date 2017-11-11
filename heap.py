"""Implementations of a heap."""
import math


class Heap(object):
    """Min or Max heap."""

    def __init__(self, heap_type):
        """Initialize the heap."""
        self.heap = []
        self.heap_type = heap_type

    def length(self):
        """Return the number of nodes in the heap."""
        return len(self.heap)

    def levels(self):
        """Return 0 indexed number of levels of heap."""
        return int(math.log(self.length(), 2))

    def insert(self, value):
        """Insert a node, then re-heapify."""
        self.heap.append(value)
        self.heapify_up()

    def peek(self):
        """Look at the top node without removing."""
        return self.heap[0]

    def pop_top(self):
        """Remove the top node and re-heapify."""
        popped_value = self.heap.pop(0)
        # Move last node up to top
        self.heap.insert(0, self.heap.pop())
        # Shift down if necessary
        self.heapify_down()
        return popped_value

    def parent_position(self, position):
        """Position of the node's parent given node position."""
        return int((position - 1) / 2)

    def left_child_position(self, position):
        """Position of the node's left child given node position."""
        return int(2 * position + 1)

    def right_child_position(self, position):
        """Position of the node's right child given node position."""
        return int(2 * position + 2)

    def has_parent(self, position):
        """Check if parent exists."""
        return self.parent_position(position) >= 0

    def has_left_child(self, position):
        """Check if left child exists."""
        return self.left_child_position(position) < self.length()

    def has_right_child(self, position):
        """Check if right child exists."""
        return self.right_child_position(position) < self.length()

    def parent_value(self, position):
        """Get the parent value."""
        return self.heap[self.parent_position(position)]

    def left_child_value(self, position):
        """Get the left_child value."""
        return self.heap[self.left_child_position(position)]

    def right_child_value(self, position):
        """Get the right_child value."""
        return self.heap[self.right_child_position(position)]

    def swap(self, position_1, position_2):
        """Swap the value at position_1 with the value at position_2."""
        temp = self.heap[position_1]
        self.heap[position_1] = self.heap[position_2]
        self.heap[position_2] = temp

    def check_node_vs_parent(self, current_position, heap_type):
        """Check node vs parent. Bigger than parent if max, smaller if min."""
        if self.heap_type == 'max':
            return (
                self.heap[current_position] >
                self.parent_value(current_position)
            )
        elif self.heap_type == 'min':
            return (
                self.heap[current_position] <
                self.parent_value(current_position)
            )

    def swap_left_child_bool(self, current_position, heap_type):
        """Check node vs left child, True if should be swapped."""
        current_larger_than_left = (
            self.heap[current_position] >
            self.left_child_value(current_position)
        )
        if heap_type == 'max':
            return not current_larger_than_left
        if heap_type == 'min':
            return current_larger_than_left

    def largest_or_smallest_child(self, current_position, heap_type):
        """Position of largest (max heap) or smallest (min heap) child."""
        if (
            self.left_child_value(current_position) >
            self.right_child_value(current_position)
        ):
            if self.heap_type == 'max':
                return self.left_child_position(current_position)
            elif self.heap_type == 'min':
                return self.right_child_position(current_position)

        else:
            if self.heap_type == 'max':
                return self.right_child_position(current_position)
            if self.heap_type == 'min':
                return self.left_child_position(current_position)

    def heapify_up(self):
        """Make sure heap property is satisfied after insert."""
        # Initialize current position and make sure current node has a parent
        current_position = self.length() - 1
        if not self.has_parent(current_position):
            return

        while (
            # check if last node entered is bigger or smaller than it's parent
            # based on min or max heap type
            self.check_node_vs_parent(current_position, self.heap_type) and
            self.has_parent(current_position)
        ):
            # if so, swap
            self.swap(
                current_position,
                self.parent_position(current_position)
            )
            current_position = self.parent_position(current_position)

    def heapify_down(self):
        """Make sure heap property is satisfied after popping top node."""
        current_position = 0

        # Swap nodes based on heap type
        while self.has_left_child(current_position):

            # Check if it has right child, if so swap with appropriate child
            if self.has_right_child(current_position):
                child_to_swap_position = self.largest_or_smallest_child(
                    current_position,
                    self.heap_type
                )

                self.swap(current_position, child_to_swap_position)

                # New current_node is swapped child position
                current_position = child_to_swap_position
                continue

            else:
                # If no right child, then check if should swap with left child
                if self.swap_left_child_bool(
                    current_position,
                    self.heap_type
                ):
                    self.swap(
                        current_position,
                        self.left_child_position(current_position)
                    )

                # There should be no lower nodes in this case.
