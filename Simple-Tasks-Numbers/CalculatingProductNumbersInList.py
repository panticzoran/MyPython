# Calculating the product of all numbers in a list

def calculate_product(number_list, print_switch):

    multiplied_number = 1
    for item in number_list:
        multiplied_number *= item

    if print_switch:
        print(multiplied_number)

    return multiplied_number

calculate_product([2,4,6,23,34], True)

print("\n")