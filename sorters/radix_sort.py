from sorters.base import SortingStrategy, Sorter
from sorters.counting_sort import CountingSort


class RadixSort(SortingStrategy):
    def sort(self, data):
        counting_sort = CountingSort()
        largest = max(data)
        exp = 1

        while largest / exp >= 1:
            self.radix_counting_sort(data, exp)
            exp *= 10
        return data

    def radix_counting_sort(self, data, exp):
        n = len(data)
        output = [0] * (n)
        count = [0] * (10)

        for i in range(0, n):
            index = data[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]
        i = n - 1
        while i >= 0:
            index = data[i] // exp
            output[count[index % 10] - 1] = data[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(0, len(data)):
            data[i] = output[i]

        return data

    def __str__(self):
        return "RadixSort"
