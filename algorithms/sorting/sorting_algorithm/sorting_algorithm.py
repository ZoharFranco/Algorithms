from abc import abstractmethod
from typing import Any, List

from algorithms.algorithm.algorithm import Algorithm
from algorithms.sorting.sorting_algorithm.sorting_algorithm_input import SortingAlgorithmInput
from algorithms.sorting.sorting_algorithm.sorting_algorithm_output import SortingAlgorithmOutput
from utils.types_utils.lists_utils import ListUtils


class SortingAlgorithm(Algorithm):
    def __init__(self, algorithm_input: SortingAlgorithmInput):
        """
        Initialize the algorithm
        Args:
            algorithm_input: scheduling algorithm input
        """
        super().__init__(algorithm_input)
        self.algorithm_input = algorithm_input
        self.algorithm_output = SortingAlgorithmOutput(sorted_list=algorithm_input.list_to_sort[:])

    @abstractmethod
    def sort_list(self) -> SortingAlgorithmOutput:
        """
        Check if the algorithm is done
        Returns:
        """
        raise NotImplementedError

    def run(self) -> SortingAlgorithmOutput:
        """
        Run the algorithm
        Returns: the algorithm output
        """
        self.sort_list()
        return self.algorithm_output

    def iteration(self):
        self.algorithm_output.total_iterations += 1

    @property
    def lst(self) -> List[Any]:
        return self.algorithm_output.sorted_list

    @property
    def n(self) -> int:
        return len(self.lst)

    def set_lst(self, lst: List[Any]):
        self.algorithm_output.sorted_list = lst

    def swap_lst_items(self, i: int, j: int):
        ListUtils.swap_items(self.lst, i, j)
