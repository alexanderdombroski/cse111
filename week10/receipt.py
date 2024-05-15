import csv
from datetime import datetime

def read_dictionary(p_filename, p_key_column_index=0):
    with open(p_filename, "rt") as file:
        next(file)
        file = csv.reader(file)

        return_dict = {}
        for line in file:
            return_dict[line[p_key_column_index]] = line

        return return_dict

REQUEST_PRODUCT_ID_INDEX = 0
REQUEST_PRODUCT_AMOUNT_INDEX = 1

PRODUCT_ID_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2

def main():
    print("\nWalco Family Shopping Center\n")
    
    try:
        read_dictionary("products.csv")
    except FileNotFoundError:
        raise FileNotFoundError("The products file is missing.") from None
    
    products = read_dictionary("products.csv")

    try:
        with open("request.csv") as request_file:
            next(request_file)
            request = csv.reader(request_file)

            number_of_items = 0
            subtotal = 0
            
            for line in request:
                try:
                    products[line[REQUEST_PRODUCT_ID_INDEX]]
                except KeyError as key_error:
                    raise KeyError(f"The product id {key_error} does not match any product.")            
                else:
                    product_details = products[line[REQUEST_PRODUCT_ID_INDEX]]
                    print(f"{product_details[PRODUCT_NAME_INDEX].title()}: {line[REQUEST_PRODUCT_AMOUNT_INDEX]} @ {product_details[PRODUCT_PRICE_INDEX]}")
                    number_of_items += int(line[REQUEST_PRODUCT_AMOUNT_INDEX])
                    subtotal += int(line[REQUEST_PRODUCT_AMOUNT_INDEX]) * float(product_details[PRODUCT_PRICE_INDEX])


            print(f"\nNumber of Items: {number_of_items}")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Sales Tax: ${subtotal * 0.06:.2f}")
            print(f"Total: ${subtotal * 1.06:.2f}")
            

            current_datetime = datetime.now()

            if f"{current_datetime:%a}" in ["Tue", "Wed"]:
                print("\nIt's one of our discount days!")
                print(f"Your total dropped to ${subtotal * 1.06 * 0.9:.2f}!")

            print("\nThank you for shopping at Walco")
            print(f"{current_datetime:%a %b %d %T %Y}\n")
    except FileNotFoundError as file_error:
        print(f"{file_error}: Request file is either missing, misnamed, or in the wrong folder\n")


if __name__ == "__main__":
    main()