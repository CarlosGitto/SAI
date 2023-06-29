from sorters.base import SortingStrategy
from sai.utils import swap_elements

class SelectionSort(SortingStrategy):
    def sort(self, data):
        for i in range(0,len(data)-1):
            min_index = i
            for j in range(i+1, len(data)):
                if data[min_index] > data[j]:
                    min_index = j

            if min_index != i:
                swap_elements(data, i, min_index)
        return data
    
    def __str__(self):
        return "SelectionSort"