def get_price():
    while True:
        price_input = input("Enter price: ")
        try:
            price = float(price_input)
            return price
        except ValueError:
            print("Invalid decimal number. Please try again.")

def get_quantity():
    while True:
        quantity_input = input("Enter quantity: ")
        try:
            quantity = int(quantity_input)
            return quantity
        except ValueError:
            print("Invalid integer. Please try again.")

def main():
    print("The Invoice Line Item Calculator")
    
    while True:
        price = get_price()
        quantity = get_quantity()
        total = price * quantity

        print(f"PRICE:\n{price:.2f}")
        print(f"QUANTITY: {quantity}")
        print(f"TOTAL:\n{total:.2f}")

        again = input("Enter another line item? (y/n): ").lower()
        if again != 'y':
            print("Bye!")
            break

    input("Press any key to continue...")

if __name__ == "__main__":
    main()
