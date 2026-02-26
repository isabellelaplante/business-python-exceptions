def main():

    while True:
        try:
            profit = float(input("Enter profit: "))
            revenue = float(input("Enter revenue: "))
            ratio = (profit / revenue) * 100
        except ValueError:
            # Silent reprompt
            pass
        except ZeroDivisionError:
            print("Revenue cannot be zero.")
        else:
            print(f"Profit margin: {ratio:.2f}%")
            break
main()