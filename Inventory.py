'''1/1/2023 base code for a inventory system '''
import csv

class Item:
  def __init__(self, name, description, location, value, quantity):
    self.name = name
    self.description = description
    self.location = location
    self.value = value
    self.quantity = quantity

  def __str__(self):
    return 'Item: {}\nDescription: {}\nLocation: {}\nValue: {}\nQuantity: {}'.format(self.name, self.description, self.location, self.value, self.quantity)

  def get_quantity(self):
    return self.quantity

class InventoryList:
  def __init__(self):
    self.items = []

  def add_item(self, item):
    self.items.append(item)

  def remove_item(self, item_name):
    self.items = [item for item in self.items if item.name != item_name]

  def get_item(self, item_name):
    return next((item for item in self.items if item.name == item_name), None)

  def get_value(self):
    return sum(item.value * item.quantity for item in self.items)

  def __str__(self):
    return 'Inventory List:\n\n' + '\n'.join(str(item) for item in self.items)

# Create an inventory list
inventory = InventoryList()

# Create a variable to track whether the user wants to add more items
add_more = True

# Create a loop to add items to the inventory list
while add_more:
  # Prompt the user to enter the item information
  name = input('Enter the item name: ')
  description = input('Enter the item description: ')
  location = input('Enter the item location: ')
  value = int(input('Enter the item value: $'))
  quantity = int(input('Enter the item quantity: '))

  # Create an item and add it to the inventory list
  item = Item(name, description, location, value, quantity)
  inventory.add_item(item)

  # Prompt the user to see if they want to add more items
  add_more = input('Do you want to add more items? (y/n) ') == 'y'

# Print the inventory list
print(inventory)

# Get the value of the inventory
value = inventory.get_value()
print('Total value: ${}'.format(value))
# Open the file in write mode
with open('inventory.csv', 'w', newline='') as csvfile:
  # Create a csv writer object
  writer = csv.writer(csvfile)

  # Write the header row
  writer.writerow(['Name', 'Description', 'Location', 'Value', 'Quantity'])

  # Write the data rows
  for item in inventory.items:
    writer.writerow([item.name, item.description, item.location, item.value, item.quantity])
