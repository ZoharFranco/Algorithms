import logging
from unittest import TestCase

from algorithms.scheduling.algorithms.round_robin.round_robin import RoundRobin
from algorithms.scheduling.algorithms.round_robin.round_robin_input import RoundRobinInput
from algorithms.scheduling.scheduling_algorithm.scheduling_algorithm_output import SchedulingAlgorithmOutput
from algorithms.searching.algorithms.binary_search.binary_search import BinarySearch
from algorithms.searching.searching_algorithm.searching_algorithm_input import SearchingAlgorithmInput
from algorithms.searching.searching_algorithm.searching_algorithm_output import SearchingAlgorithmOutput
from utils.logger.logger import logger
from utils.models.task import Task

logger.setLevel(logging.ERROR)


class TestRoundRobin(TestCase):
    def test_search_iteration(self):
        for test_input, test_output in self.get_inputs():
            result = RoundRobin(test_input).run()
            self.assertListEqual(result.queue, test_output.queue)
            self.assertEqual(result.total_time, test_output.total_time)
            self.assertEqual(result.total_iterations, test_output.total_iterations)

    @staticmethod
    def get_inputs():
        return [(RoundRobinInput(pool=[
            Task(name="Task 1", remaining_time=10),
            Task(name="Task 2", remaining_time=5),
            Task(name="Task 3", remaining_time=3),
            Task(name="Task 4", remaining_time=1),
        ], time_slice=6),
                 SchedulingAlgorithmOutput(
                     total_iterations=5,
                     queue=[Task(name="Task 1", remaining_time=0), Task(name="Task 2", remaining_time=0),
                            Task(name="Task 3", remaining_time=0), Task(name="Task 4", remaining_time=0),
                            Task(name="Task 1", remaining_time=0)],
                     total_time=19)),
        ]
