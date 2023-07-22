import random
import numpy as np
import time
from itertools import count
import pandas as pd

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

    def create_all_sorters(self) -> list[Sorter]:
        return [Sorter(strat()) for strat in STRAT_TO_CLASS.values()]


def save_df_to_parquet(df: pd.DataFrame, path: str) -> None:
    df.to_parquet(path)


def get_random_number(min_value, max_value):
    yield random.randint(min_value, max_value)


def get_int_data_1(min_value: int, max_value: int, size: int) -> np.ndarray:
    return np.random.randint(min_value, max_value + 1, size=size)


def dataset_generator(ranges: list[tuple[int, int]], sizes: int, repeat: int = 1):
    if repeat < 1:
        raise ValueError(f"Repeat value must be grater than 0, but {repeat} was found.")

    for size in sizes:
        for mn, mx in ranges:
            for i in range(repeat):
                yield generate_dataset(
                    min_value=mn, max_value=mx, size=size
                ), size, mn, mx


def open_file(path: str = None, mode: str = "r"):
    if path is None:
        raise ValueError
    return open(path, mode)


def get_float_data(
    min_value: float, max_value: float, size: int, repeat: bool
) -> list[float]:
    if repeat:
        return [random.randint(min_value, max_value) for i in range(0, size)]
    return [random.randint(min_value, max_value) for i in range(0, size)]


def generate_dataset(min_value: int, max_value: int, size: int) -> list:
    st = time.time()
    print(f"Generating dataset...(mn:{min_value}, mx:{max_value}, s:{size})")
    experiment_data_np = get_int_data_1(min_value, max_value, size)
    experiment_data = experiment_data_np.tolist()
    print(
        f"Data loaded in ---- {round(time.time() - st,4)}seconds.\n",
    )
    return experiment_data, sorted(experiment_data.copy())
