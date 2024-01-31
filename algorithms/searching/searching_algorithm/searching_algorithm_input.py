import dataclasses
from typing import List, Any

from algorithms.algorithm.algorithm_input import AlgorithmInput


@dataclasses.dataclass
class SearchingAlgorithmInput(AlgorithmInput):
    list_to_search: List[Any]
    target: Any
