from sai.utils import dataset_generator, SorterFactory, Sorter, save_df_to_parquet
from sai.globals import RANGES, SIZES, RESULT_COLUMNS, DATASET_COLUMNS, REPEAT_NUM
from sai.logs_handler import Logger
import pandas as pd
import uuid
import sys
import time

st = time.time()


def sort_data(sorter: Sorter, data: list):
    return sorter.sort_data(data.copy())


# PATHs
UNIQUE_ID = uuid.uuid4()
OUT_PATH = f"./analysis/results/{UNIQUE_ID}.parquet"
LOG_PATH = f"./analysis/logs/{UNIQUE_ID}.log"
logg = Logger(LOG_PATH).logger

# Create all sorters instances
sorters = SorterFactory().create_all_sorters()

# Init result dataframe
result_df = pd.DataFrame(columns=RESULT_COLUMNS)
config_data = []

try:
    for (dataset, sorted_dataset), *dataset_config in dataset_generator(
        ranges=RANGES, sizes=SIZES, repeat=REPEAT_NUM
    ):
        results = []
        for sorter in sorters:
            results.append(sort_data(sorter, dataset))
            results.append(sort_data(sorter, sorted_dataset))

        # Concat results in a result_df
        result_df = pd.concat(
            [result_df, pd.DataFrame(results, columns=RESULT_COLUMNS)],
            ignore_index=True,
        )

        # Save config used
        config_data.extend((dataset_config,) * len(results))
except KeyboardInterrupt:
    logg.warning(
        f"Cancel before all experiments were completed.",
    )
    logg.info(
        f"Saving results on {OUT_PATH}.",
    )
except Exception as e:
    logg.info("An exception ocurr")
    logg.error(str(e))

except:
    logg.info("Unexpected error happened")
finally:
    # Set config as a df
    config_df = pd.DataFrame(config_data, columns=DATASET_COLUMNS)

    # Add configs_df to result_df
    df = pd.concat([result_df, config_df], axis=1)

    # Save experiments as parquet files
    save_df_to_parquet(df, OUT_PATH)

    logg.info(f"Elapsed time {time.time()-st} seconds.")
    logg.info(f"A complete log of this run can be found in {OUT_PATH}")
    sys.exit(0)
