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
result = sorter.sort_data(dataset)

# Write results to corresponding file
path = f"./analysis/results/{str(sorter)}.csv"
paths = glob.glob(path)
if len(paths) > 0:
    with open(path, "a") as f:
        f.write(
            f"{size},{min_value},{max_value}"
            + ",".join(str(item) for item in result)
            + "\n"
        )

else:
    with open(path, "w+") as f:
        f.write(
            "size,min_value,max_value,elapsed_time,memory_size,memory_peak,success,inp_sorted,out_sorted,success,error\n"
        )
        f.write(
            f"{size},{min_value},{max_value}"
            + ",".join(str(item) for item in result)
            + "\n"
        )
