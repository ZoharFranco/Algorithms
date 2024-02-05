from logging import ERROR
from unittest import TestCase

from algorithms.sorting.algorithms.insertion_sort.insertion_sort import InsertionSort
from algorithms.sorting.sorting_algorithm.sorting_algorithm_input import SortingAlgorithmInput
from algorithms.sorting.sorting_algorithm.sorting_algorithm_output import SortingAlgorithmOutput
from utils.logger.logger import logger

logger.setLevel(ERROR)


class TestInsertionSort(TestCase):
    def test_sort(self):
        for test_input, test_output in self.get_inputs():
            self.assertEqual(InsertionSort(test_input).run().sorted_list, test_output.sorted_list)
            self.assertEqual(InsertionSort(test_input).run().total_iterations, test_output.total_iterations)

    @staticmethod
    def get_inputs():
        return [
            (SortingAlgorithmInput(list_to_sort=[-100, -6, 100, -5, 9, -4, -1, 21, 30, 101]),
             SortingAlgorithmOutput(sorted_list=[-100, -6, -5, -4, -1, 9, 21, 30, 100, 101], total_iterations=9))]
