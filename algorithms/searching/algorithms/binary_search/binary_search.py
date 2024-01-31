from algorithms.searching.searching_algorithm.searching_algorithm import SearchingAlgorithm
from algorithms.searching.searching_algorithm.searching_algorithm_input import SearchingAlgorithmInput


class BinarySearch(SearchingAlgorithm):
    def search(self):
        l, h = 0, len(self.algorithm_input.list_to_search) - 1

        while l < h:
            mid = (l + h) // 2

            if self.algorithm_input.list_to_search[mid] == self.algorithm_input.target:
                self.algoritm_output.result = target
                self.algoritm_output.result_index = mid
                break

            elif self.algorithm_input.list_to_search[mid] < self.algorithm_input.target:
                l = mid + 1

            else:
                h = mid - 1

        return self.algoritm_output

    def __init__(self, algorithm_input: SearchingAlgorithmInput):
        super().__init__(algorithm_input)
        self.algorithm_input = algorithm_input


if __name__ == '__main__':
    list_to_search = [1, 2, 3, 4, 7, 12]
    target = 4
    binary_search_input = SearchingAlgorithmInput(list_to_search=list_to_search, target=target)

    out_put = BinarySearch(binary_search_input).run()
    print(out_put)
