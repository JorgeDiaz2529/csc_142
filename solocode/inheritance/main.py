from order import Order
from product import *
from tabulate import tabulate

receipt = Order()

#adding the items
receipt.add_item(Grapes("Grape", 4.0))
receipt.add_item(Banannas("Bananna", 5.0))
receipt.add_item(Oranges("Orange", 10))
receipt.add_item(Cantaloupes("Cantaloupe", 3))

# Printing everything out
print(f"Total: ${receipt.calculate_total()}")
print(f"# of Items: {len(receipt)}")

# printing items & their costs
header = ["Item", "Cost"]
data = []
for item in receipt.get_items():
    data.append([item.name, item.calculate_cost()])

print(tabulate(data, headers=header, tablefmt="grid", floatfmt=".2f"))

