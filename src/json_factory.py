# json_factory.py

from tree_strategy import TreeDisplayStrategy
from rectangle_strategy import RectangleDisplayStrategy

class JSONFactory:
    def create_strategy(self, style):
        if style == 'tree':
            return TreeDisplayStrategy()
        elif style == 'rectangle':
            return RectangleDisplayStrategy()


class JSONTreeFactory(JSONFactory):
    def create_strategy(self):
        return TreeDisplayStrategy()


class JSONRectangleFactory(JSONFactory):
    def create_strategy(self):
        return RectangleDisplayStrategy()
