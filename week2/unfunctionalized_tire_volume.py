# Alex Dombroski 1/9/24

import math
from datetime import datetime

def ADcompute_tire_volume(ADtire_width, ADaspect_ratio, ADwheel_diameter):
    return math.pi * ADtire_width * ADtire_width * ADaspect_ratio * (ADtire_width * ADaspect_ratio + 2540 * ADwheel_diameter) / 10000000000

def ADget_date_ymd():
    return f"{datetime.now():%Y-%m-%d}"

def ADmain():
    ADtire_width = input("\nEnter the width of the tire in mm (ex 205): ")
    ADaspect_ratio = input("Enter the aspect ratio of the tire (ex 60): ")
    ADwheel_diameter = input("Enter the diameter of the wheel in inches (ex 15): ")

    ADtire_volume = ADcompute_tire_volume(float(ADtire_width), float(ADaspect_ratio), float(ADwheel_diameter))

    print(f"\nThe approximate volume is {ADtire_volume:.2f} liters.\n")

    with open("volumes.txt", mode="at") as ADtire_data:
        print(f"{ADget_date_ymd()}, {ADtire_width}, {ADaspect_ratio}, {ADwheel_diameter}, {ADtire_volume:.2f}", file=ADtire_data)

ADmain()