
from typing import Any, List

from falgopy.algorithm.utils import iteration
from falgopy.searching.algorithms.binary_search.binary_search import BinarySearch
from falgopy.searching.searching_algorithm.searching_algorithm_input import SearchingAlgorithmInput
from falgopy.sorting.sorting_algorithm.sorting_algorithm import SortingAlgorithm
from falgopy.sorting.sorting_algorithm.sorting_algorithm_input import SortingAlgorithmInput


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
        self.lst = self.lst[:j] + [self.lst[i]] + self.lst[j:i] + self.lst[i + 1:]

    @staticmethod
    def run_binary_search(list_to_search: List[Any], target: Any) -> int:
        binary_search = BinarySearch(SearchingAlgorithmInput(list_to_search=list_to_search, target=target))
        return binary_search.run().target_index

