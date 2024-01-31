from dataclasses import dataclass, field
from typing import List, Any

from algorithms.algorithm.algorithm_output import AlgorithmOutput


@dataclass
class SortingAlgorithmOutput(AlgorithmOutput):
    sorted_list: List[Any] = field(default_factory=list)
    total_iterations: int = 0
