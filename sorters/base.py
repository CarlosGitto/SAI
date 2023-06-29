from abc import ABC, abstractmethod

class SortingStrategy(ABC):

    @abstractmethod
    def sort(self, data):
        pass

class Sorter:
    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self.strategy = strategy

    def sort_data(self, data):
        return self.strategy.sort(data)
