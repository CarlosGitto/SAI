from sai.utils import dataset_generator, SorterFactory, Sorter, save_df_to_parquet
from sai.globals import RANGES, SIZES, RESULT_COLUMNS, DATASET_COLUMNS, REPEAT_NUM
from sai.logs_handler import Logger
import asyncio
import pandas as pd
import uuid
import sys
import time

st = time.time()


def sort_data(sorter: Sorter, data: list):
    return sorter.sort_data(data.copy())


async def create_coroutine(func, *args, **kwargs):
    return func(*args, **kwargs)


async def run_task_group(cors):
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(cor) for cor in cors]
    return [t.result() for t in tasks]


# PATHs
UNIQUE_ID = uuid.uuid4()
OUT_PATH = f"./analysis/results/{UNIQUE_ID}.parquet"
LOG_PATH = f"./analysis/logs/{UNIQUE_ID}.log"
logg = Logger(LOG_PATH).logger

# Create sorter based on sorter type
sorters = SorterFactory().create_all_sorters()

# Init result dataframe
result_df = pd.DataFrame(columns=RESULT_COLUMNS)
config_data = []

try:
    for (dataset, sorted_dataset), *dataset_config in dataset_generator(
        ranges=RANGES, sizes=SIZES, repeat=REPEAT_NUM
    ):
        corr = (
            # Coroutines for dataset
            [
                create_coroutine(sort_data, sorter=sorter, data=dataset)
                for sorter in sorters
            ]
            +
            # Coroutines for sorted dataset
            [
                create_coroutine(sort_data, sorter=sorter, data=sorted_dataset)
                for sorter in sorters
            ]
        )

        # Run group of coroutines
        results = asyncio.run(run_task_group(corr))

        # Concat results in a result_df
        result_df = pd.concat(
            [result_df, pd.DataFrame(results, columns=RESULT_COLUMNS)],
            ignore_index=True,
        )

        # Save config used
        config_data.extend((dataset_config,) * len(corr))
except KeyboardInterrupt:
    logg.warning(
        f"Cancel before all experiments were completed.",
    )
    logg.info(
        f"Saving results on {OUT_PATH}.",
    )
except Exception as e:
    logg.error("HEllo")
    logg.error(str(e))
except:
    logg.error("NO HEllo")


# Set config df
config_df = pd.DataFrame(config_data, columns=DATASET_COLUMNS)

# Add configs to result_df
df = pd.concat([result_df, config_df], axis=1)


save_df_to_parquet(df, OUT_PATH)

logg.info(f"Elapsed time {time.time()-st} seconds.")
logg.info(f"A complete log of this run can be found in {OUT_PATH}")
sys.exit(0)
