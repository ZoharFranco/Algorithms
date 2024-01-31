from dataclasses import dataclass


@dataclass
class Task:
    name: str
    remaining_time: int
