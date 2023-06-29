from sorters.base import SortingStrategy

class CountingSort(SortingStrategy):
    def sort(self, data, exp: int = 1, is_radix: bool = False):
        n = len(data)
        output = [0] * (n)
        if is_radix:
            count = [0] * (10)
        else:
            count = [0] * max(data)

        for i in range(0,n):
            index = data[i] // exp
            count[index % 10] +=1
        
        for i in range(1,10):
            count[i] += count[i-1]
        i = n-1
        while i>=0:
            index = data[i] // exp
            output[count[index % 10] - 1] = data[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(0, len(data)):
            data[i] = output[i]

        return data
            
    def __str__(self):
        return "CountingSort"