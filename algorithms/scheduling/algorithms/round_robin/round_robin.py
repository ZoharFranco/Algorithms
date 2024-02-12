from copy import deepcopy

from algorithms.algorithm.utils import iteration
from algorithms.scheduling.algorithms.round_robin.round_robin_input import RoundRobinInput
from algorithms.scheduling.scheduling_algorithm.scheduling_algorithm import SchedulingAlgorithm
from utils.models.task import Task, TaskRun


class RoundRobin(SchedulingAlgorithm):
    """
    Round-robin scheduling algorithm for tasks scheduling
    https://en.wikipedia.org/wiki/Round-robin_scheduling
    """

    def __init__(self, algorithm_input: RoundRobinInput):
        super().__init__(algorithm_input)
        self.algorithm_input = deepcopy(algorithm_input)

    def is_done(self) -> bool:
        return not bool(self.pool)

    @iteration(verbose=True)
    def schedule_next(self) -> None:
        current_task = self.pool.pop(0)
        self.queue.append(self.run_task(current_task))
        if current_task.remaining_time:
            self.pool.append(current_task)

    def run_task(self, current_task: Task) -> TaskRun:
        running_time = min(self.time_slice, current_task.remaining_time)
        current_task.remaining_time -= running_time
        self.time_passed(running_time)
        self.logger.info(f"Running {current_task.name} for {running_time} units")
        return TaskRun(task=current_task, running_time=running_time)

    @property
    def time_slice(self):
        return self.algorithm_input.time_slice
