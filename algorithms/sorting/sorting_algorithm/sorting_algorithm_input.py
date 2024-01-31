import dataclasses
from typing import List, Any

from algorithms.algorithm.algorithm_input import AlgorithmInput


@dataclasses.dataclass
class SortingAlgorithmInput(AlgorithmInput):
    list_to_sort: List[Any]
