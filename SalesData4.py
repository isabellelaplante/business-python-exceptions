def validnumber(prompt,num):

    while True:
        try:
            value = num(input(prompt))
            return value
        except ValueError:
            print("Invalid Input. Please enter a valid number.")

def main():       
    units = validnumber("Enter number of units sold: ", int) 
    price = validnumber("Enter price per unit: ", float)

    total_revenue = (units) * (price)
    print(f"\nTotal revenue: ${total_revenue:.2f}")

main()
                
