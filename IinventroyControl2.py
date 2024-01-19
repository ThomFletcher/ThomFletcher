class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity, price):
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {'quantity': quantity, 'price': price}
        print(f"Added {quantity} {name}(s) to the inventory.")

    def display_inventory(self):
        print("\nCurrent Inventory:")
        print("-------------------")
        for name, details in self.items.items():
            print(f"{name}: {details['quantity']} units - ${details['price']} each")

    def update_quantity(self, name, new_quantity):
        if name in self.items:
            self.items[name]['quantity'] = new_quantity
            print(f"Quantity of {name} updated to {new_quantity}.")
        else:
            print(f"Item '{name}' not found in inventory.")

    def calculate_total_value(self):
        total_value = sum(details['quantity'] * details['price'] for details in self.items.values())
        print(f"\nTotal Inventory Value: ${total_value}")


def main():
    inventory = Inventory()

    while True:
        print("\nInventory Control Program")
        print("1. Add Item")
        print("2. Display Inventory")
        print("3. Update Quantity")
        print("4. Calculate Total Value")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per unit: "))
            inventory.add_item(name, quantity, price)
        elif choice == '2':
            inventory.display_inventory()
        elif choice == '3':
            name = input("Enter item name to update quantity: ")
            new_quantity = int(input("Enter new quantity: "))
            inventory.update_quantity(name, new_quantity)
        elif choice == '4':
            inventory.calculate_total_value()
        elif choice == '5':
            print("Exiting Inventory Control Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
