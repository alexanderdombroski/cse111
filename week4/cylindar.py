# team activity Jan 17

# Name	Radius (cm)	Height (cm)	Cost per Can
#1 Picnic	6.83	10.16	$0.28
#1 Tall	    7.78	11.91	$0.43
#2	        8.73	11.59	$0.45
#2.5	    10.32	11.91	$0.61
#3 Cylinder	10.79	17.78	$0.86
#5	        13.02	14.29	$0.83
#6Z	        5.40	8.89	$0.22
#8Z short	6.83	7.62	$0.26
#10	        15.72	17.78	$1.53
#211	    6.83	12.38	$0.34
#300	    7.62	11.27	$0.38
#303	    8.10	11.11	$0.42

import math

def get_data():
    return [
        # [name, radius, height, cost per can]
        ["#1 Picnic", 6.83, 10.16, 0.28],
        ["#1 Tall", 7.78, 11.91, 0.43],
        ["#2", 8.73, 11.59, 0.45],
        ["#2.5", 10.32, 11.91, 0.61],
        ["#3 Cylinder", 10.79, 17.78, 0.86],
        ["#5", 13.02, 14.29, 0.83],
        ["#6Z", 5.40, 8.89, 0.22],
        ["#8Z", 6.83, 7.62, 0.26],
        ["#10", 15.72, 17.78, 1.53],
        ["#211", 6.83, 12.38, 0.34],
        ["#300", 7.62, 11.27, 0.38],
        ["#303", 8.10, 11.11, 0.42]
    ]

def compute_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def compute_volume(radius, height):
    return math.pi * radius * radius * height

def compute_storage_efficiency(volume, surface_area):
    return volume / surface_area

def main():
    print()
    cylinders = get_data()
    best_storage_efficiency = 0
    best_cost_efficiency = 9999
    
    for name, radius, height, cost in cylinders:
        volume = compute_volume(radius, height)
        surface_area = compute_surface_area(radius, height)
        storage_efficiency = compute_storage_efficiency(volume, surface_area)
        if storage_efficiency > best_storage_efficiency:
            best_storage_efficiency = storage_efficiency
            best_can = name
            best_can_cost = cost
        if best_cost_efficiency > cost / volume:
            best_cost_efficiency = cost / volume
            cheapest_can = name
        
        print(f"{name:<11} volume: {round(volume, 1):>7} cubic cm | surface area: {round(surface_area, 1):>6} sqr. cm | efficiency: {storage_efficiency:.1f}")
    input("\nHit ENTER for results")
    print(f"\nThe winning can is {best_can}!")
    print(f"This can costs ${best_can_cost}")

    print('''
           _.---._
        .-"       "-. 
        |-_       _-| 
        |  "~---~"  | 
        |    10!    |
        `._       _.'
           "-----"
    ''')
    print(f"The cheapest can per volume is {cheapest_can}.\n")

if __name__ == "__main__":
    main()