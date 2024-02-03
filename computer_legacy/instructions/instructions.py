"""
Instruction module
"""
from abc import ABC, abstractmethod


class Instruction(ABC):
    """
    Base class for instructions
    """
    @abstractmethod
    def execute(self, cpu):
        """
        Execute the intruction        
        """
