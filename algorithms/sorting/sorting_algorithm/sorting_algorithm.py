from abc import abstractmethod

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
        self.algorithm_input = algorithm_input
        self.algoritm_output = SortingAlgorithmOutput()

    @abstractmethod
    def get_sorted_list(self) -> SortingAlgorithmOutput:
        """
        Check if the algorithm is done
        Returns:
        """
        raise NotImplementedError

    def run(self) -> SortingAlgorithmOutput:
        """
        Run the algorithm
        Returns: yield next value in schedule
        """
        return self.get_sorted_list()
