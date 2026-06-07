from input_puzzle import input_puzzle


# todo use a generator
def generate_product_ids():
    product_ids = []
    for product_id_range in input_puzzle:
        boundary_start, boundary_end = product_id_range
        for element in list(range(boundary_start, boundary_end + 1)):
            product_ids.append(element)

    return product_ids


product_ids = generate_product_ids()

data = {
    product_id: len(str(product_id))
    for product_id in product_ids
    if len(str(product_id)) % 2 == 0
}


def tandem_number_count():
    counter = 0
    for number in product_ids:
        number = str(number)
        length = len(number)
        midpoint = int(length / 2)

        if number[0:midpoint] == number[midpoint:]:
            flag = True
            counter += int(number)

    return counter


answer = tandem_number_count()
print(answer)
