import timeit
from abc import abstractmethod

from algorithms.algorithm.algorithm_input import AlgorithmInput
from algorithms.algorithm.algorithm_output import AlgorithmOutput
from utils.logger.logger import logger


class Algorithm:

    def __init__(self, algorithm_input: AlgorithmInput):
        """
        Initialize the algorithm
        Args:
            algorithm_input: the input of the algorithm to be run in the form of AlgorithmInput
        """
        self.algorithm_input = algorithm_input
        self.logger = logger

    @abstractmethod
    def run(self) -> AlgorithmOutput:
        """
        Run the algorithm
        Returns:
        """
        raise NotImplementedError

    def check_run_time(self):
        """
        Check the run time of the algorithm
        Returns:
        """
        return timeit.timeit(self.run, number=1)
