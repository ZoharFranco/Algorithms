from logging import DEBUG
from typing import Any, List

from algorithms.algorithm.utils import iteration
from algorithms.searching.algorithms.binary_search.binary_search import BinarySearch
from algorithms.searching.searching_algorithm.searching_algorithm_input import SearchingAlgorithmInput
from algorithms.sorting.sorting_algorithm.sorting_algorithm import SortingAlgorithm
from algorithms.sorting.sorting_algorithm.sorting_algorithm_input import SortingAlgorithmInput


class InsertionSort(SortingAlgorithm):
    """
    Insertion sort - using binary search for finding the right place to insert the next element
    https://en.wikipedia.org/wiki/Insertion_sort
    """

    def __init__(self, algorithm_input: SortingAlgorithmInput):
        super().__init__(algorithm_input)

    def sort_list(self):
        for i in range(1, self.n):
            self.sort_iteration(i)

    @iteration(verbose=True)
    def sort_iteration(self, i: int):
        j = self.run_binary_search(list_to_search=self.lst[:i], target=self.lst[i])
        self.logger.debug(f"Insertion Sort Iteration: {i}, List: {self.lst}, Target: {self.lst[i]}, Target Index: {j}")
        self.lst = self.lst[:j] + [self.lst[i]] + self.lst[j:i] + self.lst[i + 1:]

    @staticmethod
    def run_binary_search(list_to_search: List[Any], target: Any) -> int:
        binary_search = BinarySearch(SearchingAlgorithmInput(list_to_search=list_to_search, target=target))
        return binary_search.run().target_index


if __name__ == '__main__':
    list_to_sort = [1, 6, 2, 3, 4, 7, 12]
    binary_sort_input = SortingAlgorithmInput(list_to_sort=list_to_sort)
    out_put = InsertionSort(binary_sort_input).run()
