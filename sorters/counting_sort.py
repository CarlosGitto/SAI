from sorters.base import SortingStrategy


class CountingSort(SortingStrategy):
    def sort(self, data):
        # Find the maximum element in the array
        max_value = max(data)

        # Create a counting array of size max_value+1 filled with zeros
        count = [0] * (max_value + 1)

        # Count the occurrences of each element
        for val in data:
            count[val] += 1

        # Generate the sorted output
        sorted_arr = []
        for i in range(len(count)):
            sorted_arr.extend([i] * count[i])

        return sorted_arr

    def __str__(self):
        return "CountingSort"
