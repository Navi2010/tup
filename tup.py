def calculate_product(num_tuple):
    product = 1
    for num in num_tuple:
        product *= num
    return product

numbers = (2, 3, 4, 5)

result = calculate_product(numbers)

print("the product of the numbers in the tuple is: ", result)
