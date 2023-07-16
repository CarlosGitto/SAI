import random
import numpy as np
import time

from sorters.bubble_sort import BubbleSort
from sorters.counting_sort import CountingSort
from sorters.shell_sort import ShellSort
from sorters.insertion_sort import InsertionSort
from sorters.heap_sort import HeapSort
from sorters.merge_sort import MergeSort
from sorters.radix_sort import RadixSort
from sorters.randomized_quick_sort import RandomizedQuickSort
from sorters.selection_short import SelectionSort
from sorters.base import Sorter

STRAT_TO_CLASS = {
    "bubble": BubbleSort,
    "merge": MergeSort,
    "heap": HeapSort,
    "insertion": InsertionSort,
    "radix": RadixSort,
    "counting": CountingSort,
    "quick": RandomizedQuickSort,
    "selection": SelectionSort,
    "shell": ShellSort,
}

random.seed(0)


class SorterFactory:
    def create_sorter(self, strategy: str) -> Sorter:
        if strategy not in STRAT_TO_CLASS:
            raise KeyError(
                f"Not a valid Sorter Strategy({strategy}) - {list(STRAT_TO_CLASS.keys())}"
            )
        return Sorter(STRAT_TO_CLASS[strategy]())


def get_random_number(min, max):
    yield random.randint(min, max)


def get_int_data_1(min_value: int, max_value: int, size: int) -> np.ndarray:
    return np.random.randint(min_value, max_value + 1, size=size)


def get_float_data(min: float, max: float, size: int, repeat: bool) -> list[float]:
    if repeat:
        return [random.randint(min, max) for i in range(0, size)]
    return [random.randint(min, max) for i in range(0, size)]


def generate_dataset(min: int, max: int, size: int) -> list:
    st = time.time()
    print("Generating dataset...")
    experiment_data_np = get_int_data_1(min, max, size)
    experiment_data = experiment_data_np.tolist()
    print(
        f"Data loaded in ---- {round(time.time() - st,4)}seconds.\n",
    )
    return experiment_data
