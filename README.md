# Sorting Algorithms Analysis

This project aims to provide a comprehensive analysis and insights into various sorting algorithms. It offers a collection of sorting algorithms implemented in Python, along with features for performance evaluation, data visualization, and data analysis. The project is designed to help users understand the characteristics, efficiency, and trade-offs of different sorting methods.

## Features

- **Implemented Sorting Algorithms:** The project includes several popular sorting algorithms, such as Bubble Sort, Insertion Sort, Selection Sort, Merge Sort, Heap Sort, Quick Sort, etc.

- **Performance Evaluation:** Users can measure and compare the time efficiency of different sorting algorithms using provided datasets. Execution time, memory usage, and other relevant metrics can be analyzed to determine the efficiency of each algorithm.

- **Data Analysis:** The project allows users to perform data analysis on the sorted outputs. Insights can be gained by analyzing patterns, trends, and outliers in the sorted data.

- **Data Visualization:** Visualizations are provided to illustrate the sorting process and outcomes. Animations and graphs help users better understand how the elements move and the performance characteristics of each algorithm.

- **Insights and Recommendations:** Detailed explanations, strengths, weaknesses, and best-case/worst-case scenarios are provided for each sorting algorithm. Users can gain insights into the behavior and suitability of algorithms for different data distributions.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/sorting-algorithms-analysis.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Explore the different sorting algorithm classes in the codebase.

## How to use

```sh
python setup.py develop
python -m sai
```

## Run

```bash
cat './sai/experiment_args.txt' |
parallel --bar --colsep ' ' "python -m sai {}"
```

## Results

Go to [results](./analysis/analysis.ipynb)

WIP
