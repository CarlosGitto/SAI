from sorters.base import SortingStrategy

class BubbleSort(SortingStrategy):
    def sort(self, data):
        for i in range(1,len(data)):
            for j in range(0,len(data)-1):
                if data[j] > data[j+1]:
                    holder = data[j]
                    data[j] = data[j+1]
                    data[j+1] = holder
                    print(data)
            
   
