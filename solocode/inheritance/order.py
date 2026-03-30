class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.calculate_cost()
        return total
    
    def get_items(self):
        return self.items

    def __len__(self):
        return len(self.items)