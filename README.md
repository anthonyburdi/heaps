# Heaps

Just some messing around with heap data structures

 * Implement Heap (min and max), running_median
 * Some tests (run `python test_heap.py` or `python test_running_median.py`)

#### Example usage:
```
from heap import Heap
import running_median
min_heap = Heap(heap_type='min')
max_heap = Heap(heap_type='max')

for value in range(1, 11):
    running_median.insert(min_heap, max_heap, value)

print running_median.get_median(min_heap, max_heap) # 5.5
```

#### Simple case in slow motion

Run `python running_median.py`