from abc import abstractmethod
from typing import List, Any

from algorithms.algorithm.algorithm import Algorithm
from algorithms.searching.searching_algorithm.searching_algorithm_input import SearchingAlgorithmInput
from algorithms.searching.searching_algorithm.searching_algorithm_output import SearchingAlgorithmOutput
from utils.types_utils.lists_utils import ListUtils


class SearchingAlgorithm(Algorithm):
    def __init__(self, algorithm_input: SearchingAlgorithmInput):
        """
        Initialize the algorithm
        Args:
            algorithm_input: searching algorithm input
        """
        super().__init__(algorithm_input)
        self.algorithm_input = algorithm_input
        self.algorithm_output = SearchingAlgorithmOutput()

    @abstractmethod
    def search(self) -> SearchingAlgorithmOutput:
        """
        Search
        Returns: return searching algorithm output
        """
        raise NotImplementedError

    def run(self) -> SearchingAlgorithmOutput:
        """
        Run the algorithm
        Returns: return searching algorithm output
        """
        self.search()
        return self.algorithm_output

    @property
    def lst(self) -> List[Any]:
        return self.algorithm_input.list_to_search

    @property
    def target(self):
        return self.algorithm_input.target

    def set_lst(self, lst: List[Any]):
        self.algorithm_output.sorted_list = lst

    @property
    def n(self) -> int:
        return len(self.lst)

    def swap_lst_items(self, i: int, j: int):
        ListUtils.swap_items(self.lst, i, j)

    def iteration(self):
        self.algorithm_output.total_iterations += 1

    def set_result_index(self, index: int):
        self.algorithm_output.result_index = index
