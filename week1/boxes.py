# Alex Dombroski 1/9/24
import math

'''
In our modern world economy, many items are manufactured in large factories, then packed in boxes and shipped to 
distribution centers and retail stores. A common question for employees who pack items is “How many boxes do we need?”
'''

def main():
    items = int(input("\nEnter the number of items: "))
    box_capacity = int(input("Enter the number of items per box: "))
    print(f"\nFor {items} items, packing {box_capacity} items in each box, you will need {compute_boxes(items, box_capacity)} boxes.")
def compute_boxes(items, box_capacity):
    return math.ceil(items / box_capacity)

main()