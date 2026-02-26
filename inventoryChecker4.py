
def validInt(prompt):
    
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    while True:
        inventory = validInt("Enter the number of items in inventory: ")
        minthreshold = validInt("Enter the minimum threshold for inventory: ")
        if inventory < minthreshold:
            print("Inventory is below the minimum threshold. Please restock.")
            
        try:
            percentage = (inventory / minthreshold) * 100
            print(f"Inventory is at {percentage:.2f}% of the minimum threshold.")
        except ZeroDivisionError:
            print("Minimum threshold cannot be zero. Please enter a valid number.")
            continue 
        break

main()
