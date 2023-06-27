from sorters.base import SortingStrategy

class InsertionSort(SortingStrategy):
    def sort(self, data):
        for i in range(0, len(data)):
            j = i
            while j > 0 and data[j-1] > data[j]:
                
                holder = data[j-1]
                data[j-1] = data[j]
                data[j] = holder
                j = j-1
                print("->",data)
            print(data)
         