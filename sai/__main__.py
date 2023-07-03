import sys
from sai.utils import get_int_data_1, SorterFactory
import time
import numpy as np
import glob

args = sys.argv

try:
    min_value = int(args[1])
    max_value = int(args[2])
    size = int(args[3])
    strat = args[4]
except:
    print(f"Correct usage of SAI is: python -m sai MIN MAX SAMPLE_SIZE SORTER_NAME")
    sys.exit(1)

st = time.time()

print("Loading data...")
experiment_data_np = get_int_data_1(min_value, max_value, size)
print()
experiment_data = experiment_data_np.tolist()
print(
    f"\tData loaded in ---- {round(time.time() - st,4)}seconds",
)
sorter = SorterFactory().create_sorter(strat)
sorted_data, elapsed_time = sorter.sort_data(experiment_data.copy())
success = sorted_data == sorted(experiment_data.copy())
print(f"\tSorter: {str(sorter)}")
print(f"\tSuccess: {success}\n\tElapsed Time: {round(elapsed_time, 4)} seconds.\n\n")
path = f"./analysis/results/{str(sorter)}.csv"
paths = glob.glob(path)
if len(paths) > 0:
    with open(path, "a") as f:
        f.write(f"{elapsed_time}, {size}, {min_value}, {max_value} {success}\n")
else:
    with open(path, "a+") as f:
        f.write("elapsed_time,size,min_value,max_value,success\n")
        f.write(f"{elapsed_time}, {size}, {min_value}, {max_value} {success}\n")
