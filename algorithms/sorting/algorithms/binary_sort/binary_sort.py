from algorithms.scheduling.algorithms.round_robin.round_robin_input import RoundRobinInput
from algorithms.sorting.sorting_algorithm.sorting_algorithm import SortingAlgorithm
from algorithms.sorting.sorting_algorithm.sorting_algorithm_input import SortingAlgorithmInput
from algorithms.sorting.sorting_algorithm.sorting_algorithm_output import SortingAlgorithmOutput
from utils.models.task import Task


class BinarySort(SortingAlgorithm):
    def get_sorted_list(self) -> SortingAlgorithmOutput:
        pass

    def sort_list(self):
        l, h = 0, len(self.algorithm_input.list_to_sort) - 1
        while l < h:
            mid = (l + h) // 2


    def __init__(self, algorithm_input: SortingAlgorithmInput):
        super().__init__(algorithm_input)
        self.algorithm_input = algorithm_input


if __name__ == '__main__':
    tasks = [
        Task(name="Task 1", remaining_time=10),
        Task(name="Task 2", remaining_time=5),
        Task(name="Task 3", remaining_time=3),
    ]

    out_put = BubbleSort(RoundRobinInput(pool=tasks, time_slice=2)).run()
