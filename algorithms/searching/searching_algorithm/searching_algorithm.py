from abc import abstractmethod
from copy import deepcopy
from typing import List, Any

from algorithms.algorithm.algorithm import Algorithm
from algorithms.searching.searching_algorithm.searching_algorithm_input import SearchingAlgorithmInput
from algorithms.searching.searching_algorithm.searching_algorithm_output import SearchingAlgorithmOutput


class SearchingAlgorithm(Algorithm):
    def __init__(self, algorithm_input: SearchingAlgorithmInput):
        """
        Initialize the algorithm
        Args:
            algorithm_input: searching algorithm input
        """
        super().__init__(algorithm_input)
        self.algorithm_input = deepcopy(algorithm_input)
        self.algorithm_output = SearchingAlgorithmOutput()

    @abstractmethod
    def search(self):
        """
        Search for the target, change the algorithm output result index
        Returns: return searching algorithm output
        """
        raise NotImplementedError

    def run(self) -> SearchingAlgorithmOutput:
        """
        Run the algorithm, change the algorithm output
        """

        self.logger.info(f"Searching Input: {self.algorithm_input}")
        self.search()
        self.logger.info(f"Searching Output: {self.algorithm_output}")

        return self.algorithm_output

    @property
    def lst(self) -> List[Any]:
        return self.algorithm_input.list_to_search

    @property
    def target(self):
        return self.algorithm_input.target

    @property
    def n(self) -> int:
        return len(self.lst)

    @property
    def target_index(self):
        return self.algorithm_output.target_index

    @target_index.setter
    def target_index(self, index: int):
        self.algorithm_output.target_index = index
