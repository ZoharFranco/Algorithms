from abc import abstractmethod
from copy import deepcopy
from typing import List, Any

from algorithms.algorithm.algorithm import Algorithm
from algorithms.scheduling.scheduling_algorithm.scheduling_algorithm_input import SchedulingAlgorithmInput
from algorithms.scheduling.scheduling_algorithm.scheduling_algorithm_output import SchedulingAlgorithmOutput


class SchedulingAlgorithm(Algorithm):
    def __init__(self, algorithm_input: SchedulingAlgorithmInput):
        """
        Initialize the algorithm
        Args:
            algorithm_input: scheduling algorithm input
        """
        super().__init__(algorithm_input)
        self.algorithm_input = deepcopy(algorithm_input)
        self.algorithm_output = SchedulingAlgorithmOutput()

    @abstractmethod
    def is_done(self):
        """
        Check if the algorithm is done to end running
        Returns:
        """
        raise NotImplementedError

    @abstractmethod
    def schedule_next(self):
        """
        Run one iteration of scheduling
        Returns:
        """
        raise NotImplementedError

    def run(self) -> SchedulingAlgorithmOutput:
        """
        Run the algorithm
        Returns: return scheduling algorithm output
        """
        self.logger.info(f"Scheduling Input: {self.algorithm_input}")
        while not self.is_done():
            self.schedule_next()
        self.logger.info(f"Scheduling Output: {self.algorithm_output}")
        return self.algorithm_output

    @property
    def pool(self) -> List[Any]:
        return self.algorithm_input.pool

    @property
    def queue(self) -> List[Any]:
        return self.algorithm_output.queue

    @property
    def total_time(self) -> int:
        return self.algorithm_output.total_time

    def time_passed(self, time: int):
        self.algorithm_output.total_time += time
