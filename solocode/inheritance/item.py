from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def calculate_cost():
        raise NotImplementedError # it will never run

#SUB CLASSES
class ByWeightItem(Item):
    def __init__(self, name, weight, cost_per_pound):
        super().__init__(name)
        self.weight = weight
        self.cost_per_pound = cost_per_pound
    
    def calculate_cost(self): # implements the abstract method
        return self.weight * self.cost_per_pound

class ByQuanitityItem(Item):
    def __init__(self, name, quantity, cost_each):
        super().__init__(name)
        self.quantity = quantity
        self.cost_each = cost_each
    
    def calculate_cost(self):
        return self.quantity * self.cost_each