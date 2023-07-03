from sorters.base import SortingStrategy


class ShellSort(SortingStrategy):
    def sort(self, data):
        n = len(data)
        interval = n // 2
        while interval > 0:
            for i in range(interval, n):
                temp = data[i]
                j = i
                while j >= interval and data[j - interval] > temp:
                    data[j] = data[j - interval]
                    j -= interval

                data[j] = temp
            interval //= 2
        return data

    def __str__(self):
        return "ShellSort"
