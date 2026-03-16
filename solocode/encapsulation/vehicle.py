class Vehicle:
    def __init__(self, mode, fuel_capacity, cost_per_gallon, miles_per_gallon):
        self._mode = mode
        self._fuel_capacity = fuel_capacity
        self._cost_per_gallon = cost_per_gallon
        self._miles_per_gallon = miles_per_gallon
    
    @property
    def range(self):
        return self._fuel_capacity * self._miles_per_gallon
    
    @property
    def cost_per_miles(self):
        return self._cost_per_gallon / self._miles_per_gallon