from sorters.base import SortingStrategy
from sorters.base import swap_elements


class HeapSort(SortingStrategy):
    def sort(self, data):
        n = len(data)
        self.build_max_heap(data)

        for i in range(n - 1, 0, -1):
            swap_elements(data, i, 0)
            self.heapify(data, 0, i)
        return data

    def heapify(self, data, i, n):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[left] > data[largest]:
            largest = left

        if right < n and data[right] > data[largest]:
            largest = right

        if largest != i:
            swap_elements(data, i, largest)
            self.heapify(data, largest, n)

    def build_max_heap(self, data):
        n = len(data)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(data, i, n)

    def __str__(self):
        return "HeapSort"
