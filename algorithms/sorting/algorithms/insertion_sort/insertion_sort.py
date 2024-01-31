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
        for i in range(self.n):
            self.iteration()

            searching_input = SearchingAlgorithmInput(list_to_search=self.lst[:i], target=self.lst[i])
            binary_result = BinarySearch(searching_input).run()
            j = binary_result.result_index

            self.set_lst(self.lst[:j] + [self.lst[i]] + self.lst[j:i] + self.lst[i + 1:])


if __name__ == '__main__':
    list_to_sort = [1, 6, 2, 3, 4, 7, 12]
    binary_sort_input = SortingAlgorithmInput(list_to_sort=list_to_sort)
    out_put = InsertionSort(binary_sort_input).run()

