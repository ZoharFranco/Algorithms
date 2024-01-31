from dataclasses import dataclass, field
from typing import List, Any

from algorithms.algorithm.algorithm_output import AlgorithmOutput


@dataclass
class SchedulingAlgorithmOutput(AlgorithmOutput):
    queue: List[Any] = field(default_factory=list)
    total_time: int = 0
