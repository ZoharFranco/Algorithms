from unittest import TestCase

from falgopy.searching.algorithms.binary_search.binary_search import BinarySearch
from falgopy.searching.searching_algorithm.searching_algorithm_input import SearchingAlgorithmInput
from falgopy.searching.searching_algorithm.searching_algorithm_output import SearchingAlgorithmOutput


class TestBinarySearch(TestCase):
    def test_search_iteration(self):
        for test_input, test_output in self.get_inputs():
            self.assertEqual(BinarySearch(test_input).run().target_index, test_output.target_index)
            self.assertEqual(BinarySearch(test_input).run().total_iterations, test_output.total_iterations)

    @staticmethod
    def get_inputs():
        return [(SearchingAlgorithmInput(list_to_search=[-100, -6, -5, -4, -1, 9, 21, 30, 100, 101, 200], target=-4),
                 SearchingAlgorithmOutput(target_index=3, total_iterations=3)),
                (SearchingAlgorithmInput(list_to_search=[-100, -6, -5, -4, -1, 9, 21, 30, 100, 101, 200], target=9),
                 SearchingAlgorithmOutput(target_index=5, total_iterations=1))]
