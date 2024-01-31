from abc import abstractmethod

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
        self.algorithm_input = algorithm_input
        self.algoritm_output = SchedulingAlgorithmOutput()

    @abstractmethod
    def is_done(self):
        """
        Check if the algorithm is done
        Returns:
        """
        raise NotImplementedError

    @abstractmethod
    def schedule_next(self):
        """
        Check if the algorithm is done
        Returns:
        """
        raise NotImplementedError

    def run(self) -> SchedulingAlgorithmOutput:
        """
        Run the algorithm
        Returns: yield next value in schedule
        """

        while not self.is_done():
            self.schedule_next()
            self.logger.info(
                f"Pool: {self.algorithm_input.pool}, "
                f"Queue: {self.algoritm_output.queue}, "
                f"Total time: {self.algoritm_output.total_time}"
            )
        return self.algoritm_output
