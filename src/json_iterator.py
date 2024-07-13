# json_iterator.py

from iterator import Iterator

class JSONCompositeIterator(Iterator):
    def __init__(self, components):
        self.components = components
        self.index = 0

    def has_next(self):
        return self.index < len(self.components)

    def next(self):
        component = self.components[self.index]
        self.index += 1
        return component
