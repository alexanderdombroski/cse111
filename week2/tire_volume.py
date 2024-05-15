# Alex Dombroski 1/11/24

import math
from datetime import datetime

def AD_get_valid_number(p_input_prompt):
    AD_invalid_input = True
    while AD_invalid_input:
        AD_input_value = input(p_input_prompt)
        try:
            float(AD_input_value)
        except:
            print("Please input a valid number")
        else:
            AD_invalid_input = False
    return AD_input_value

def AD_compute_tire_volume(p_width, p_aspect_ratio, p_diameter):
    return math.pi * p_width * p_width * p_aspect_ratio * (p_width * p_aspect_ratio + 2540 * p_diameter) / 10000000000

def AD_display_tire_volume(p_tire_volume):
    print(f"\nThe approximate volume is {p_tire_volume:.2f} liters.\n")

def AD_get_purchase_consent():
    AD_response = ""
    while AD_response.lower() not in("yes", "no"):
        AD_response = input("Would you like to purchase a tire with these dimensions? ")
    return AD_response

def AD_get_phone():
    return input("What is your phone number? ")

def AD_record_tire_data(p_tire_width, p_aspect_ratio, p_wheel_diameter, p_tire_volume, p_tire_data):
    print(f"{datetime.now():%Y-%m-%d}, {p_tire_width}, {p_aspect_ratio}, {p_wheel_diameter}, {p_tire_volume:.2f}", file=p_tire_data, end="")

def AD_record_phone_number(p_phone, p_tire_data):
    print(f", {p_phone}", file=p_tire_data, end="")

def AD_record_finalize(p_tire_data):
    print("", file=p_tire_data)

def main():
    
    # Get tire information
    print()
    AD_tire_width = AD_get_valid_number("Enter the width of the tire in mm (ex 205): ")
    AD_aspect_ratio = AD_get_valid_number("Enter the aspect ratio of the tire (ex 60): ")
    AD_wheel_diameter = AD_get_valid_number("Enter the diameter of the wheel in inches (ex 15): ")

    # Run Calculations
    AD_tire_volume = AD_compute_tire_volume(float(AD_tire_width), float(AD_aspect_ratio), float(AD_wheel_diameter))
    AD_display_tire_volume(AD_tire_volume)

    # Record data in a file
    with open("volumes.txt", mode="at") as AD_tire_data:
        AD_record_tire_data(AD_tire_width, AD_aspect_ratio, AD_wheel_diameter, AD_tire_volume, AD_tire_data)
        AD_response = AD_get_purchase_consent()
        if AD_response.lower() == "yes":
            AD_phone = AD_get_phone()
            AD_record_phone_number(AD_phone, AD_tire_data)
        AD_record_finalize(AD_tire_data)

main()