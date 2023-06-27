from sorters.base import SortingStrategy

class MergeSort(SortingStrategy):
    def sort(self, data):
        return self.merge_sort(data)
    
    def merge_sort(self, data):
        data_len = len(data)
        if data_len == 1:
            return data
        
        div_point = data_len // 2
        left = data[0:div_point]
        right = data[div_point:]

        sorted_left = self.merge_sort(left)
        sorted_right = self.merge_sort(right)

        return self.merge(sorted_left, sorted_right)

    def merge(self, left, right):
        merge_array = []
        while len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                merge_array.append(right[0])
                right.pop(0)
            else:
                merge_array.append(left[0])
                left.pop(0)

        while len(left) > 0:
            merge_array.append(left[0])
            left.pop(0)
        
        while len(right) > 0:
            merge_array.append(right[0])
            right.pop(0)

        return merge_array
   