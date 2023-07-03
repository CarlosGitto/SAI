from sorters.base import SortingStrategy
import random
from sorters.base import swap_elements


class RandomizedQuickSort(SortingStrategy):
    def sort(self, data, low: int = 0, high: int = None):
        if high is None:
            high = len(data) - 1
        if low < high:
            p = self.random_partition(data, low, high)
            self.sort(data, low, p - 1)
            self.sort(data, p + 1, high)
        return data

    def random_partition(self, data, low, high):
        random_pivot = random.randrange(low, high)
        swap_elements(data, low, random_pivot)

        return self.partition(data, low, high)

    def partition(self, data, low, high):
        pivot = low

        i = low + 1

        for j in range(low + 1, high + 1):
            if data[j] <= data[pivot]:
                swap_elements(data, i, j)
                i = i + 1
        swap_elements(data, pivot, i - 1)
        pivot = i - 1
        return pivot

    def __str__(self):
        return "RandomizedQuickSort"
