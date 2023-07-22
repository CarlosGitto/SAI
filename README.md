# Sorting Algorithms Insights (SAI)

🚩🚩🚩 This project is under development 🚩🚩🚩

## Introduction:

The Sorting Algorithms Insights (SAI) project aims to analyze and gain insights into the behavior of different sorting algorithms under various parameters. The project explores nine commonly used sorting algorithms, including `bubble sort`, `merge sort`, `heap sort`, `insertion sort`, `radix sort`, `counting sort`, `quicksort`, `selection sort`, and `shell sort`. By examining the algorithms' performance across different sample sizes and ranges of minimum and maximum values, the project seeks to provide valuable insights on the optimal usage scenarios for each sorting algorithm.

All the algorithms mention abobe can be found on the directory ./sorters each in their own file, under their own name.

To conduct the analysis, a series of experiments are run using a Python script called "sai". This script generates random arrays based on the specified parameters and applies all the sorting algorithms to sort to each generated array. The elapsed time for each sorting operation is recorded, along with the size, minimum value, maximum value, peak of memory used by the sorting algorithm, if the input was sorted, if the output was sorted, and a flag indicating the success or not of the algorithm, if the success flag is false, it means an error ocurr while running the sorting algorithm, this error will also be recorded. The results of the experiments will be store in a **.parquet** file with an unique id as name on the directory **./analysis/results** (this id is generated with `uuid` module from python, more specificly `uuid.uuid4()`).

Its also worth to mention that if any system interruption ocurr during the excecution of the experiments, python will try to write the obtained results so far to the results directory mentioned earlier.

## About the program

As mention before this program takes some parameters, generates a dataset and run all different sorting allgorithms over this dataset. Each result of each sorting algorithm is stored in a single dataframe than then is stored as a parquet file.

Is important to notice that the times toked by each algorithm may bary depending on the equipment used to run SAI, and the time is heavily impacted by the use of the tracemalloc module. This module is necessary to trace the peak of memory reach when doing experiments.

You can opt tu run this program normal or taking advantage of GNU parallel multiprocessing, this program is written with the intention to do so. All the operations done are done single threaded.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/sorting-algorithms-analysis.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Explore the different sorting algorithm classes in the codebase.

## Config

There are three main variables that you can play with to manage the size and values of the generated datasets, and and number of repetition.

`SIZES` -> A list that represents all the sizes you want to test, size is reffered as the length of a generated dataset

`RANGES` -> Is the combination of min and max value a dataset can take, the correct structure should be `list[tuple[int, int]]`, where the first value of the tuple represents the min value, and the second represent the max value of a dataset. This variable can also be modified by adding new values to `RANGE_VALUES` then this array will be use to generate the corresponding ranges.

`REPEAT_NUM` -> An integer that represents the number of times an experiment is repeated. This means that each combination of size and ranges, will be repeated `x` number of times, each time with a new generated dataset but with the same characteristics(same size, and ranges). This variable must be a value greater than 1.

All of this can be found [here](./sai/globals.py).

## Quickstart

```sh
python setup.py develop
```

```bash
# Normal run
python -m sai

# Run with GNU parallel
N=10
parallel --bar --termseq INT,1000,TERM,2000 python -m sai ::: {0..$N}
```

- After running experiments `logs` can be found [here](./analysis/logs), and `result files` [here](./analysis/results).

## How to Analyse

A complete analysis over the generated results can done using this [Jupyter notebook](./analysis/analysis.ipynb)
