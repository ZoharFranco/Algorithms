import dataclasses
from typing import List, Any

from algorithms.algorithm.algorithm_input import AlgorithmInput


@dataclasses.dataclass
class SchedulingAlgorithmInput(AlgorithmInput):
    pool: List[Any]
