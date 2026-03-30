from item import ByWeightItem, ByQuanitityItem

#ByWeightItem Subclasses
class Grapes(ByWeightItem):
    def __init__(self, name, weight, cost_per_pound=1.75):
        super().__init__(name, weight, cost_per_pound)
        #self.cost_per_pound = 1.75

class Banannas(ByWeightItem):
    def __init__(self, name, weight, cost_per_pound=0.65):
        super().__init__(name, weight, cost_per_pound)
        #self.cost_per_pound = 0.65

#ByQuantityItem Subclasses
class Oranges(ByQuanitityItem):
    def __init__(self, name, quantity, cost_each=3.0):
        super().__init__(name, quantity, cost_each)
        #self.cost_each = 1.54

class Cantaloupes(ByQuanitityItem):
    def __init__(self, name, quantity, cost_each=3.0):
        super().__init__(name, quantity, cost_each)
        #self.cost_each = 3.00

