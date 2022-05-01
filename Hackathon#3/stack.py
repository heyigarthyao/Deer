# This is the Stack class which get the # of guesses the player uses in their game.

class Stack:

    def __init__(self) -> None:
        self.items = []

    def is_empty(self) -> bool:
        return self.items == []

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self) -> None:
        self.items.pop()

