import random 
import time
from sorters.base import Sorter
from sorters.bubble_sort import BubbleSort
from sorters.counting_sort import CountingSort
from sorters.heap_sort import HeapSort
from sorters.insertion_sort import InsertionSort
from sorters.merge_sort import MergeSort
from sorters.quick_sort import QuickSort
from sorters.radix_sort import RadixSort
from sorters.selection_short import SelectionSort
from sorters.shell_sort import ShellSort

sorters = [
 BubbleSort,
 CountingSort,
 HeapSort,
 InsertionSort,
 MergeSort,
#  QuickSort,
 RadixSort,
 SelectionSort,
#  ShellSort,
]
data = random.sample(range(0, 100_000), 10)
# data = [2,8,5,3,9,4,1]
solution = sorted(data)
print("DATA LENGTH: ", len(data),"\n\n")
st = time.time()
for sorter in sorters:
    s = time.time()
    w = data.copy()
    x = Sorter(sorter())
    y = x.sort_data(w)
    print(f"{sorter()}\t\t {time.time()-s} seconds")
    if y != solution:
        
        e = '^' * len(str(sorter()))
        print(f'{e} -> Bad solution!')
        print(solution)
        print(y)
    print()

print(f"\n\nTOTAL TIME: {time.time()-st} seconds --\n")