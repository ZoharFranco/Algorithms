import abc
import dataclasses


@dataclasses.dataclass
class AlgorithmOutput(abc.ABC):
    total_iterations: int = 0
