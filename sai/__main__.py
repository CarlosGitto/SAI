import random 
from sorters.base import Sorter
from sorters.merge_sort import MergeSort

data = random.sample(range(1, 100), 21)
# data = [2,8,5,3,9,4,1]
print(data)
x = Sorter(MergeSort())
y = x.sort_data(data)
print(y)

