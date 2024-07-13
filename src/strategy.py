# strategy.py

from abc import ABC, abstractmethod

class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, component, indent='', is_last=True, icon_family=None, is_root=False):
        pass
