def get_salary(prompt):

    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value for salary.")

def main():
    # Get current salary
    salary = get_salary("Enter current salary: ")
    # Get adjustment percentage with custom checks
    while True:
        percentage = get_salary("Enter adjustment percentage(0-100): ")
        if percentage < 0:
            print("Percentage cannot be negative. Please enter a valid percentage.")
            continue
        if percentage > 100:
            print("Percentage cannot exceed 100%. Please enter a valid percentage.")
            continue
    
        break

    new_salary = salary + (salary * (percentage / 100))
    print(f"New salary after adjustment: {new_salary:.2f}")

main()