from abc import abstractmethod
from copy import deepcopy
from typing import Any, List

from algorithms.algorithm.algorithm import Algorithm
from algorithms.sorting.sorting_algorithm.sorting_algorithm_input import SortingAlgorithmInput
from algorithms.sorting.sorting_algorithm.sorting_algorithm_output import SortingAlgorithmOutput


class SortingAlgorithm(Algorithm):
    def __init__(self, algorithm_input: SortingAlgorithmInput):
        """
        Initialize the algorithm
        Args:
            algorithm_input: scheduling algorithm input
        """
        super().__init__(algorithm_input)
        self.algorithm_input = deepcopy(algorithm_input)
        self.algorithm_output = SortingAlgorithmOutput(sorted_list=algorithm_input.list_to_sort[:])

    @abstractmethod
    def sort_list(self):
        """
        Sort the list to be sorted as wanted
        Returns:
        """
        raise NotImplementedError

    def run(self) -> SortingAlgorithmOutput:
        """
        Run the sorting algorithm
        Returns: the algorithm output
        """

        self.logger.info(f"Sorting Input: {self.algorithm_input}")
        self.sort_list()
        self.logger.info(f"Sorting Output: {self.algorithm_output}")

        return self.algorithm_output

    def iteration(self):
        self.algorithm_output.total_iterations += 1

    @property
    def lst(self) -> List[Any]:
        return self.algorithm_output.sorted_list

    @lst.setter
    def lst(self, lst: List[Any]):
        self.algorithm_output.sorted_list = lst

    @property
    def n(self) -> int:
        return len(self.lst)
