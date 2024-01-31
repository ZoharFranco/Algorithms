from algorithms.scheduling.algorithms.round_robin.round_robin_input import RoundRobinInput
from algorithms.scheduling.scheduling_algorithm.scheduling_algorithm import SchedulingAlgorithm
from utils.models.task import Task


class RoundRobin(SchedulingAlgorithm):
    """
    Round-robin scheduling algorithm for tasks scheduling
    https://en.wikipedia.org/wiki/Round-robin_scheduling
    """

    def __init__(self, algorithm_input: RoundRobinInput):
        super().__init__(algorithm_input)
        self.algorithm_input = algorithm_input

    def is_done(self) -> bool:
        return not bool(self.algorithm_input.pool)

    def schedule_next(self) -> None:
        current_task = self.algorithm_input.pool.pop(0)
        self.algoritm_output.queue.append(current_task)
        self.run_task(current_task)
        if current_task.remaining_time:
            self.algorithm_input.pool.append(current_task)

    def run_task(self, current_task: Task) -> None:
        running_time = min(self.algorithm_input.time_slice, current_task.remaining_time)
        current_task.remaining_time -= running_time
        self.algoritm_output.total_time += running_time
        self.logger.info(f"Running {current_task.name} for {running_time} units")


if __name__ == '__main__':
    tasks = [
        Task(name="Task 1", remaining_time=10),
        Task(name="Task 2", remaining_time=5),
        Task(name="Task 3", remaining_time=3),
    ]

    out_put = RoundRobin(RoundRobinInput(pool=tasks, time_slice=2)).run()
