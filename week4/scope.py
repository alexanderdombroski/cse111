# Week 2 R 2 Prep variable scope & parameters

import math

def calc_cone_volume(r, h):
    return math.pi * r * r * h / 3

def main():
    ex_radius = 2.8
    ex_height = 3.2
    ex_vol = calc_cone_volume(ex_radius, ex_height)

    # Print several lines that describe this program.
    print("This program computes the volume of a right")
    print("circular cone. For example, if the radius of a")
    print(f"cone is {ex_radius} and the height is {ex_height}")
    print(f"then the volume is {ex_vol:.1f}\n")

    radius = float(input("Please enter the radius of the cone: "))
    height = float(input("Please enter the height of the cone: "))

    vol = calc_cone_volume(radius, height)

    print(f"Radius: {radius}")
    print(f"Height: {height}")
    print(f"Volume: {vol:.1f}")

main()
    

