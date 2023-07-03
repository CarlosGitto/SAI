import random
import time
from sorters.base import Sorter
from sorters.bubble_sort import BubbleSort
from sorters.counting_sort import CountingSort
from sorters.heap_sort import HeapSort
from sorters.insertion_sort import InsertionSort
from sorters.merge_sort import MergeSort
from sorters.randomized_quick_sort import RandomizedQuickSort
from sorters.radix_sort import RadixSort
from sorters.selection_short import SelectionSort
from sorters.shell_sort import ShellSort


def test_booble_sort():
    data = random.sample(range(0, 1000), 1000)
    solution = sorted(data)
    sorter = Sorter(BubbleSort())
    sorted_data, _ = sorter.sort_data(data)
    assert sorted_data == solution, "BubbleSort failed"


def test_counting_sort():
    data = random.sample(range(0, 1000), 1000)
    solution = sorted(data.copy())
    sorter = Sorter(CountingSort())
    sorted_data, _ = sorter.sort_data(data.copy())
    assert sorted_data == solution, f"CountingSort failed"


def test_heap_sort():
    data = random.sample(range(0, 1000), 1000)
    solution = sorted(data)
    sorter = Sorter(HeapSort())
    sorted_data, _ = sorter.sort_data(data)
    assert sorted_data == solution, "HeapSort failed"


def test_insertion_sort():
    data = random.sample(range(0, 1000), 1000)
    solution = sorted(data)
    sorter = Sorter(InsertionSort())
    sorted_data, _ = sorter.sort_data(data)
    assert sorted_data == solution, "InsertionSort failed"


def test_merge_sort():
    data = random.sample(range(0, 1000), 1000)
    solution = sorted(data)
    sorter = Sorter(MergeSort())
    sorted_data, _ = sorter.sort_data(data)
    assert sorted_data == solution, "MergeSort failed"


def test_randomized_quick_sort():
    data = random.sample(range(0, 1000), 1000)
    solution = sorted(data)
    sorter = Sorter(RandomizedQuickSort())
    sorted_data, _ = sorter.sort_data(data)
    assert sorted_data == solution, "RandomizedQuickSort failed"


def test_selection_sort():
    data = random.sample(range(0, 1000), 1000)
    solution = sorted(data)
    sorter = Sorter(SelectionSort())
    sorted_data, _ = sorter.sort_data(data)
    assert sorted_data == solution, "SelectionSort failed"


def test_radix_sort():
    data = random.sample(range(0, 1000), 1000)
    solution = sorted(data)
    sorter = Sorter(RadixSort())
    sorted_data, _ = sorter.sort_data(data)
    assert sorted_data == solution, "RadixSort failed"


def test_shell_sort():
    data = random.sample(range(0, 1000), 1000)
    solution = sorted(data)
    sorter = Sorter(ShellSort())
    sorted_data, _ = sorter.sort_data(data)
    assert sorted_data == solution, "ShellSort failed"
