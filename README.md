# How to use

```

# Binary search example
from falgopy.searching.searching_algorithm.searching_algorithm_input import SearchingAlgorithmInput
from falgopy.searching.algorithms.binary_search.binary_search import BinarySearch
print(BinarySearch(SearchingAlgorithmInput(list_to_search=[1, 2, 3], target=2)).target_index)


# Round rubin example
from falgopy.scheduling.algorithms.round_robin.round_robin import RoundRobin
from falgopy.scheduling.algorithms.round_robin.round_robin_input import RoundRobinInput
from falgopy.utils.models.task import Task

print(RoundRobin(RoundRobinInput(pool=[
            Task(name="Task 1", remaining_time=10),
            Task(name="Task 2", remaining_time=5),
            Task(name="Task 3", remaining_time=3),
            Task(name="Task 4", remaining_time=1),
        ])).algorithm_output.queue)

```


# Algorithms

- Base classes (utils)
- Fundamentals ideas
- Variety of algorithms implementations

Abstract algorithm

```
class Algorithm:

    def __init__(self, algorithm_input: AlgorithmInput):

    @abstractmethod
    def run(self) -> AlgorithmOutput:

    def check_run_time(self):
```

## Algorithms types

### Search

Searching abstract algorithm

```

class SearchingAlgorithm(Algorithm):
    def __init__(self, algorithm_input: SearchingAlgorithmInput):
        
    @abstractmethod
    def search(self) -> SearchingAlgorithmOutput:
        
    def run(self) -> SearchingAlgorithmOutput:
        """
        Run the algorithm
        Returns: return searching algorithm output
        """
        algoritm_output = self.search()
        self.logger.info(f"Total iterations: {algoritm_output.total_search_iterations}")
        return algoritm_output
```

Examples

- Binary search
-

### Sort

Sorting abstract algorithm

```
class SortingAlgorithm(Algorithm):
    def __init__(self, algorithm_input: SortingAlgorithmInput):
        
    @abstractmethod
    def get_sorted_list(self) -> SortingAlgorithmOutput:
        
    def run(self) -> SortingAlgorithmOutput:
        """
        Run the algorithm
        Returns: yield next value in schedule
        """
        return self.get_sorted_list()
```

Examples

- Binary Sort
- Bubble Sort
- Sort

### Scheduling

Sorting abstract algorithm

```
class SchedulingAlgorithm(Algorithm):
    def __init__(self, algorithm_input: SchedulingAlgorithmInput):
        
    @abstractmethod
    def is_done(self):
        
    @abstractmethod
    def schedule_next(self):
        
    def run(self) -> SchedulingAlgorithmOutput:
        """
        Run the algorithm
        Returns: yield next value in schedule
        """

        while not self.is_done():
            self.schedule_next()
            self.logger.info(
                f"Pool: {self.algorithm_input.pool}, "
                f"Queue: {self.algoritm_output.queue}, "
                f"Total time: {self.algoritm_output.total_time}"
            )
        return self.algoritm_output
```

Examples

- Round Robin
- 


