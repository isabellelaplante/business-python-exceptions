def get_customer_age():
    while True:
        try:
            #print(age_value)  # This will raise a NameError since age_value is not defined
            age = int(input("Please enter the customer's age: "))
            if age <= 0:
                print("Age must be a positive integer. Please enter a valid age.")
                continue
            return age

        except ValueError:
            print("Invalid input. Please enter a whole number for age.")
        
        except NameError:
            print("A variable was referenced incorrectly.")


def main():
    age = get_customer_age()
    if age >= 18:
        print("Customer is eligible for age restricted promotions.")
    else:
        print("Customer is not eligible for age restricted promotions.")
   
main()