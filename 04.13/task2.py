# Create a class called MyQueue that has __bool__, __repr__ and __len__ methods defined.

# The __bool__ method should return True if the queue has any items and False if it is empty.
# The __repr__ method should return a string in the format MyQueue(items) where items is the list of items in the queue.
# The __len__ method should return the number of items in the queue.

from typing import List , Optional


class MyQueue:
    def __init__(self) -> None:
        self.queue: List[Optional[int]]  = []

    def __bool__(self) -> bool:
        return bool(self.queue)

    def __repr__(self) -> str:
        return f"MyQueue({self.queue})"

    def __len__(self) -> int:
        return len(self.queue)


eile = MyQueue()
eile.queue.append(1)
eile.queue.append(3)
print(bool(eile))
print(repr(eile))
print(len(eile))
