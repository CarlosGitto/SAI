from sorters.base import SortingStrategy
from sai.utils import swap_elements
class BubbleSort(SortingStrategy):
    def sort(self, data):
        for i in range(1,len(data)):
            for j in range(0,len(data)-1):
                if data[j] > data[j+1]:
                    swap_elements(data, j, j+1)
        return data
    def __str__(self):
         return "BubbleSort"