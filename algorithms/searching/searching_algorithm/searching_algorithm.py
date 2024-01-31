from abc import abstractmethod

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
        self.algorithm_input = algorithm_input
        self.algoritm_output = SearchingAlgorithmOutput()

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
        algoritm_output = self.search()
        self.logger.info(f"Total iterations: {algoritm_output.total_search_iterations}")
        return algoritm_output
