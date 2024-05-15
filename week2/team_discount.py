from datetime import datetime

def get_subtotal():
    return input("What is the subtotal? ")

def display_discount(discount):
    print(f"You have a discount of ${discount:.2f}")

def display_discount_shortage(subtotal):
    print(f"You are ${50-subtotal:.2f} short of receiving your discount")

def display_tax(tax):
    print(f"Your tax is ${tax:.2f}")

def display_total(total):
    print(f"Your total is ${total:.2f}")



def main():
    print()

    subtotal = float(get_subtotal())
    day = datetime.now().weekday()
    # day = 2
    
    discount = 0
    if day == 1 or day == 2:
        if subtotal < 50:
            display_discount_shortage(subtotal)
        else:
            discount = .1 * subtotal
            display_discount(discount)

    untaxed_total = (subtotal - discount)
    
    display_tax(untaxed_total * .06)
    display_total(untaxed_total * 1.06)

    print()

main()