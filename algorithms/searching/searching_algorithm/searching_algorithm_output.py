from dataclasses import dataclass

from algorithms.algorithm.algorithm_output import AlgorithmOutput


@dataclass
class SearchingAlgorithmOutput(AlgorithmOutput):
    total_iterations: int = 0
    target_index: int = None
