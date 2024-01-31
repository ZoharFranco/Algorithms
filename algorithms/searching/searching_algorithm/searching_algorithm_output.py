from dataclasses import dataclass
from typing import Any

from algorithms.algorithm.algorithm_output import AlgorithmOutput


@dataclass
class SearchingAlgorithmOutput(AlgorithmOutput):
    total_search_iterations: int = 0
    result_index: int = None
    result: Any = None
