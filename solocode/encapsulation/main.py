from vehicle import Vehicle
from tabulate import tabulate

#the four vehicles
car = Vehicle("Car", 13, 3.7, 47)
truck = Vehicle("Pickup Truck", 23, 3.7, 20)
motorcycle = Vehicle("Motorcycle", 23, 3.7, 67)
plane = Vehicle("Commercial Airplane", 6875, 6.0, 70)
vehicles = [car, truck, motorcycle, plane]

#printing it all out
headers = ["Mode", "Range", "Cost per Miles"]
data = []
for v in vehicles:
    data.append([v._mode, v.range, v.cost_per_miles])
data.sort(key=lambda vehicle: vehicle[2]) #sorts by cost per mile

print(tabulate(data, headers=headers, tablefmt="github"))