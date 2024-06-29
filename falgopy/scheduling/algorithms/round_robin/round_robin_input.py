from dataclasses import dataclass, field
from typing import List

from falgopy.scheduling.scheduling_algorithm.scheduling_algorithm_input import SchedulingAlgorithmInput
from falgopy.utils.models.task import Task


@dataclass
class RoundRobinInput(SchedulingAlgorithmInput):
    pool: List[Task] = field(default_factory=list)
    time_slice: int = 1
