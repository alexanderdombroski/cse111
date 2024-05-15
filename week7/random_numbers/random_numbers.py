# Team Activity 1/30

from random import *

def display_numbers(list):
    print(list)

def append_random_numbers(list, quantity=1):
    for i in range(quantity):
        list.append(round(uniform(10,99),1))

def main():
    numbers = [16.2, 75.1, 52.3]

    append_random_numbers(numbers)
    display_numbers(numbers)
    
    append_random_numbers(numbers, 3)
    display_numbers(numbers)

    append_random_numbers(numbers, 3)
    display_numbers(numbers)

if __name__ == "__main__":
    main()