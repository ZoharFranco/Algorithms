from algorithms.searching.searching_algorithm.searching_algorithm import SearchingAlgorithm
from algorithms.searching.searching_algorithm.searching_algorithm_input import SearchingAlgorithmInput


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
        while left <= right:
            self.iteration()

            mid = (left + right) // 2
            current = self.lst[mid]

            if current > self.target:
                right = mid - 1
            elif current < self.target:
                left = mid + 1
            else:
                self.set_result_index(mid)
                break

        self.set_result_index(left)


if __name__ == '__main__':
    list_to_search = [-6, -1, 9, 21, 30]
    target = -4
    binary_search_input = SearchingAlgorithmInput(list_to_search=list_to_search, target=target)

    out_put = BinarySearch(binary_search_input).run()
    print(out_put)
