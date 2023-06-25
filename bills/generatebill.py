import os

class Bill:
    def __init__(self, name):
        self.name = name
        self.items = {}
    

    def format(self):
        result = "Bill Breakdown: \n"
        total = 0

        for item, price in self.items.items():
            result += f"{item: <25} ... ${price}\n"
            total += price

        result += f"Total: {total}"
        return result
    
    def add_item(self, name, price):
        self.items[name] = price

def create_bill():
    name = input("Create new bill name: ")
    bill = Bill(name)
    print("Created the bill - ", bill.name)
    return bill

def save_bill(bill):
    data = bill.format()
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, bill.name + ".txt")
    with open(file_path, "w") as file:
        file.write(data)
    print("Bill was saved to file")

def prompt_options(bill):
    while True:
        option = input("Chose an option (add - add items, save - save bill): ")
        if option == "add":
            name = input("Item name: ")
            price = float(input("Item price: "))
            bill.add_item(name, price)
            print("Item added -", name, price)
        elif option == "save":
            save_bill(bill)
            print("saved the bill", bill.name)
            break
        else:
            print("That was not a valid option...")

bill = create_bill()
prompt_options(bill)
print(bill.format())