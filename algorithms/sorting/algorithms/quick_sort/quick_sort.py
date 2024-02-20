from typing import Any, List

from algorithms.algorithm.utils import iteration
from algorithms.sorting.sorting_algorithm.sorting_algorithm import SortingAlgorithm
from algorithms.sorting.sorting_algorithm.sorting_algorithm_input import SortingAlgorithmInput


class QuickSort(SortingAlgorithm):
    """
    Quick sort - quick sorting algorithm
    https://en.wikipedia.org/wiki/Quicksort
    """

    def __init__(self, algorithm_input: SortingAlgorithmInput):
        super().__init__(algorithm_input)

    def sort_list(self):
        self.lst = self.sort_rec(self.lst)

    @iteration(verbose=True)
    def sort_rec(self, lst: List[Any]):
        pivot = lst[0] if lst else []
        less = self.sort_rec([i for i in lst[1:] if i <= pivot]) if lst[1:] else []
        greater = self.sort_rec([i for i in lst[1:] if i > pivot]) if lst[1:] else []
        return less + [pivot] + greater if pivot else less + greater
