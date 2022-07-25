from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


class CyclicIterator:
    def __init__(self, iterable_object):
        self.idx = -1
        self.object = iterable_object

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < len(self.object) - 1:
            self.idx += 1
            return self.object[self.idx]
        self.idx = 0
        return self.object[self.idx]


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        tuple_idx = 0
        while tuple_idx < len(self.dates):
            start_date, end_date = self.dates[tuple_idx]
            while start_date <= end_date:
                yield start_date
                start_date += timedelta(days=1)
            tuple_idx += 1
