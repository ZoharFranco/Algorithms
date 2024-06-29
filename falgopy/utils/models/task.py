from dataclasses import dataclass


@dataclass
class Task:
    name: str
    remaining_time: int


@dataclass
class WeightTask(Task):
    weight: float


@dataclass
class TaskRun:
    task: Task
    running_time: int
