import tracemalloc
from abc import ABC, abstractmethod
from time import perf_counter


def profiler(sorter_func):
    def wrapper(*args, **kwargs):
        sorter_name = args[0]
        list_to_sort = args[1].copy()

        # Start time
        time_start = perf_counter()

        # Get memory befor start
        tracemalloc.start()
        print(tracemalloc.get_traced_memory())
        # Sort
        sorted_data = sorter_func(*args, **kwargs)

        # Calculate consumed memory
        print(tracemalloc.get_traced_memory())
        curr_size, peak = tracemalloc.get_traced_memory()
        # Get elapsed time
        elapsed_time = perf_counter() - time_start

        # Get success status
        success = sorted_data == sorted(list_to_sort)

        # Show insights as logs
        print(
            f"""{sorter_name}\n\tCurrent size memory: {curr_size} bytes.\n\tPeak memory usage: {peak}\n\tSuccess: {success}.\n\tElapsed Time: {round(elapsed_time,4)} seconds.\n\t"""
        )

        return sorted_data, elapsed_time, success, curr_size, peak

    return wrapper


def swap_elements(l1: list, i1: int, i2: int):
    l1[i1], l1[i2] = l1[i2], l1[i1]
    return l1


class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass


class Sorter:
    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy

    def __str__(self):
        return str(self.strategy)

    def set_strategy(self, strategy: SortingStrategy):
        self.strategy = strategy

    @profiler
    def sort_data(self, data):
        return self.strategy.sort(data)
