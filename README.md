# Sorting Algorithms Insights (SAI)

🚩🚩🚩 This project is under development 🚩🚩🚩

## Introduction:

The Sorting Algorithms Insights (SAI) project aims to analyze and gain insights into the behavior of different sorting algorithms under various parameters. The project explores nine commonly used sorting algorithms, including bubble sort, merge sort, heap sort, insertion sort, radix sort, counting sort, quicksort, selection sort, and shell sort. By examining the algorithms' performance across different sample sizes and ranges of minimum and maximum values, the project seeks to provide valuable insights on the optimal usage scenarios for each sorting algorithm.

To conduct the analysis, a series of experiments are run using a Python script called "sai". This script generates random arrays based on the specified parameters and applies the selected sorting algorithm to sort the arrays. The elapsed time for each sorting operation is recorded, along with the size, minimum value, maximum value, and a flag indicating the success of the sorting process. The results of each experiment are saved in separate CSV files for each sorting algorithm.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/sorting-algorithms-analysis.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Explore the different sorting algorithm classes in the codebase.

## How to use

```sh
python setup.py develop
python ./sai/data_generation.py
```

```bash
cat './sai/experiment_args.txt' |
parallel --bar --colsep ' ' "python -m sai {}"
```

## Results

Go to [results](./analysis/analysis.ipynb)
