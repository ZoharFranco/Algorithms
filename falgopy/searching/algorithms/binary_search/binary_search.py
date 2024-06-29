from falgopy.algorithm.utils import iteration
from falgopy.searching.searching_algorithm.searching_algorithm import SearchingAlgorithm
from falgopy.searching.searching_algorithm.searching_algorithm_input import SearchingAlgorithmInput


class BinarySearch(SearchingAlgorithm):
    """
    Binary search algorithm - finding the index of the target by using binary splitting of the list
    https://en.wikipedia.org/wiki/Binary_search_algorithm
    """

    def __init__(self, algorithm_input: SearchingAlgorithmInput):
        super().__init__(algorithm_input)
        self.algorithm_input = algorithm_input

    def search(self):
        left, right, mid = 0, self.n - 1, 0

        while left < right and self.lst[left] != self.target:
            left, right = self.search_iteration(left, right)

        self.target_index = left

    @iteration(verbose=True)
    def search_iteration(self, left: int, right: int):
        mid = (left + right) // 2
        current = self.lst[mid]

        if current > self.target:
            right = mid - 1
        elif current < self.target:
            left = mid + 1
        elif current == self.target:
            left = mid
            self.target_index = mid

        return left, right
