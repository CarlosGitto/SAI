from abc import ABC, abstractmethod
from time import perf_counter


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

    def sort_data(self, data):
        t1_start = perf_counter()
        sorted_data = self.strategy.sort(data)
        t1_stop = perf_counter()

        return sorted_data, t1_stop - t1_start
