class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        """
        push: Adds an item to the end of the collection
        """
        self.data.append(item)

    def pop(self):
        """
        pop: Removes the last item from the collection and returns it
        """
        value = self.data.pop()
        return value

    def peek(self):
        """
        peek: Observes the last item in the collection without removing it
        """
        value = self.data[-1]
        return value

    def is_empty(self):
        """
        is_empty: Returns whether the stack is empty or not (boolean)
        """
        return len(self.data) == 0

    def __contains__(self, value):
        return value in self.data
