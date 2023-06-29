from sorters.base import SortingStrategy
from sai.utils import swap_elements

class InsertionSort(SortingStrategy):
    def sort(self, data):
        for i in range(0, len(data)):
            j = i
            while j > 0 and data[j-1] > data[j]:
                swap_elements(data, j, j-1)                
                j = j-1
        return data
    
    def __str__(self):
         return "InsertionSort"