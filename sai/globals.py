from itertools import combinations

# This values are used as min, max values on RANGES
RANGE_VALUES = sorted(
    [
        0,
        1,
        10,
        100,
        1_000,
        # 10_000,
        # 100_000,
    ]
)


# array like [[min, max], [min, max], ...] between all posible combinations of `range_values`
RANGES = list(combinations(RANGE_VALUES, 2))

# List of sizes use on experiments
SIZES = [
    1,
    10,
    100,
    # 1_000,
    # 3_000,
    # 5_000,
    # 10_000,
    # 15_000,
    # 35_000,
    # 50_000,
    # 75_000,
    # 100_000,
]

REPEAT_NUM = 30

DATASET_COLUMNS = [
    "size",
    "min_value",
    "max_value",
]
RESULT_COLUMNS = [
    "sorter",
    "elapsed_time",
    "memory_size",
    "memory_peak",
    "success",
    "in_sorted",
    "out_sorted",
    "error",
]
