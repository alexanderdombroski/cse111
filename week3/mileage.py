# Prep week 2 L1

def mph(gallons, mileage_start, mileage_end):
    return (mileage_end - mileage_start) / gallons

def lp100k_from_mpg(mpg):
    return 235.2 / mpg

def main():
    print()

    start = float(input("Enter the first odometer reading (miles): "))
    end = float(input("Enter the second odometer reading (miles): "))
    fuel = float(input("Enter the amount of fuel used (gallons): "))

    gas_mileage = mph(fuel, start, end)
    print(f"{gas_mileage:.1f} miles per gallon")
    print(f"{lp100k_from_mpg(gas_mileage):.2f} liters per 100 kilometers")

main()