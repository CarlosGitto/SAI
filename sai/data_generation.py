import os
from sai.utils import get_int_data_1
import random
from sai.utils import STRAT_TO_CLASS

ranges = [
    # -10_000,
    # -1_000,
    # -100,
    # -10,
    0,
    1,
    10,
    100,
    1_000,
    10_000,
    100_000,
    1_000_000,
    10_000_000,
    100_000_000,
]
sizes = [1, 10, 100, 1_000, 5_000, 10_000, 15_000, 25_000, 50_000, 75_000, 100_000]
arg = ""
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
for _ in range(5_000):
    for i in sizes:
        for id, j in enumerate(ranges):
            for k in ranges[id + 1 :]:
                for sorter in sorters:
                    if id + 1 < len(ranges):
                        if k != j:
                            arg += f"{j} {k} {i} {sorter}\n"

with open("./sai/experiment_args.txt", "w+") as f:
    f.write(arg)
