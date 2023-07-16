import sys
from sai.utils import generate_dataset, SorterFactory
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
    print(f"Correct usage of SAI is: python -m sai MIN MAX DATASET_SIZE SORTER_NAME")
    sys.exit(1)

# Generate Dataset
dataset = generate_dataset(min_value, max_value, size)

# Create sorter based on sorter type
sorter = SorterFactory().create_sorter(strat)

# Sort generated data
sorted_data, elapsed_time, success, curr_mem_size, peak_memory_usage = sorter.sort_data(
    dataset
)

# Write results to corresponding file
path = f"./analysis/results/{str(sorter)}.csv"
paths = glob.glob(path)
if len(paths) > 0:
    with open(path, "a") as f:
        f.write(
            f"{elapsed_time}, {size}, {min_value}, {max_value}, {success}, {curr_mem_size}, {peak_memory_usage}\n"
        )
else:
    with open(path, "w+") as f:
        f.write(
            "elapsed_time,size,min_value,max_value,success,memory_size,memory_peak\n"
        )
        f.write(
            f"{elapsed_time}, {size}, {min_value}, {max_value}, {success}, {curr_mem_size}, {peak_memory_usage}\n"
        )
