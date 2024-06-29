import logging
from unittest import TestCase

from falgopy.scheduling.algorithms.round_robin.round_robin import RoundRobin
from falgopy.scheduling.algorithms.round_robin.round_robin_input import RoundRobinInput
from falgopy.scheduling.scheduling_algorithm.scheduling_algorithm_output import SchedulingAlgorithmOutput
from falgopy.utils.logger.logger import logger
from falgopy.utils.models.task import Task, TaskRun

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
                     queue=[
                         TaskRun(task=Task(name="Task 1", remaining_time=0), running_time=6),
                         TaskRun(task=Task(name="Task 2", remaining_time=0), running_time=5),
                         TaskRun(task=Task(name="Task 3", remaining_time=0), running_time=3),
                         TaskRun(task=Task(name="Task 4", remaining_time=0), running_time=1),
                         TaskRun(task=Task(name="Task 1", remaining_time=0), running_time=4),
                     ],
                     total_time=19)),
        ]
