from sorters.base import SortingStrategy

class SelectionSort(SortingStrategy):
    def sort(self, data):
        for i in range(0,len(data)-1):
            min_index = i
            for j in range(i+1, len(data)):
                if data[min_index] > data[j]:
                    min_index = j

            if min_index != i:
                holder = data[min_index]
                data[min_index] = data[i]
                data[i] = holder
            print(data)
