from itertools import combinations, product
import numpy as np
import time

st = time.time()
ranges = [
    0,
    1,
    10,
    100,
    1_000,
    10_000,
    100_000,
]
min_max_comb = list(combinations(ranges, 2))
matrix = np.array(min_max_comb)
sizes = np.array(
    [1, 10, 100, 1_000, 3_000, 5_000, 10_000, 15_000, 35_000, 50_000, 75_000, 100_000]
)
sorters = [
    "bubble",
    "merge",
    "heap",
    "insertion",
    "radix",
    "counting",
    "quick",
    "selection",
    "shell",
]

# Compute the combinations of sizes and sorters
pos_combinations = list(product(sizes, sorters))
print("Step 1 completed.")
# Repeat the matrix rows to match the number of combinations
repeated_matrix = np.repeat(matrix, len(pos_combinations), axis=0)
print("Step 2 completed.")

# Tile the combinations to match the number of rows in the repeated matrix
tiled_combinations = np.tile(pos_combinations, (len(matrix), 1))
print("Step 3 completed.")

# Combine the repeated matrix and tiled combinations along the columns
result = np.concatenate((repeated_matrix, tiled_combinations), axis=1)
print("Step 4 completed.")

experiments_args = np.repeat(result, 1000, axis=0)
print("Step 5 completed.")

file_path = "./sai/experiment_args.txt"
np.savetxt(file_path, experiments_args, delimiter=" ", fmt="%s")
print("Step 6 completed.")
et = time.time()


print(
    f"\nArguments generated: {experiments_args.shape[0]:_}\nTime to complete: {round(et-st, 4)} seconds.\nArguments file path: {file_path}"
)
