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
        # Sort
        sorted_data, error = sorter_func(*args, **kwargs)

        # Calculate consumed memory
        curr_size, peak = tracemalloc.get_traced_memory()
        # Get elapsed time
        elapsed_time = perf_counter() - time_start

        # Get success status
        start_sorted = list_to_sort == sorted(list_to_sort)
        end_sorted = sorted_data == sorted(list_to_sort)
        success = error == None

        # Show insights as logs
        print(
            f"""{sorter_name}\n\tCurrent size memory: {curr_size} bytes.\n\tPeak memory usage: {peak} bytes.\n\tInput Data Sorted: {start_sorted}.\n\tOutput Data Sorted: {end_sorted}.\n\tSuccess: {success}.\n\tError: {error}\n\tElapsed Time: {round(elapsed_time,4)} seconds.\n\t"""
        )

        return (elapsed_time, curr_size, peak, start_sorted, end_sorted, success, error)

    return wrapper


def swap_elements(l1: list, i1: int, i2: int):
    if i1 == i2:
        raise IndexError(f"Indexes to swap should not be equal (i1:{i1} i2:{i2})")
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
        e = None
        try:
            sorted_data = self.strategy.sort(data)
        except RecursionError as error:
            sorted_data = data
            e = error
        except ValueError as error:
            sorted_data = data
            e = error
        except IndexError as error:
            sorted_data = data
            e = error
        return sorted_data, e
