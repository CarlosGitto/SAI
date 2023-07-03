import os
from sai.utils import get_int_data_1
import random
from sai.utils import STRAT_TO_CLASS

ranges = [
    -10_000,
    -1_000,
    -100,
    -10,
    0,
    10,
    100,
    1_000,
    10_000,
]
sizes = [
    1,
    10,
    100,
    1_000,
    # 10_000,
    # 100_000,
    # 1_000_000
]
arg = ""
for i in sizes:
    for id, j in enumerate(ranges):
        if id + 1 < len(ranges):
            for k in ranges[id + 1 :]:
                if k != j:
                    arg += f"{j} {k} {i}\n"

with open("./sai/experiment_args.txt", "w+") as f:
    f.write(arg)
