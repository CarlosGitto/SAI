from sorters.base import SortingStrategy, Sorter
from sorters.counting_sort import CountingSort

class RadixSort(SortingStrategy):
    def sort(self, data):
        counting_sort = CountingSort()
        largest = max(data)
        exp = 1
        
        while largest / exp >=1:
            counting_sort.sort(data, exp, is_radix=True)
            exp *= 10
        return data

    def __str__(self):
        return "RadixSort"