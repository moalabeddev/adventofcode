from input_puzzle import input_puzzle , raw_input_
from library import generate_product_ids, stringify_product_ids




# product_ids = generate_product_ids(input_puzzle)
# print(product_ids)

# print("="*62)

# stringified_product_ids=stringify_product_ids(product_ids)
# print(stringified_product_ids)

# def generate_parity_pure_product_ids(stringified_product_ids: list[str]):

for string_product_id in raw_input_:
    print(string_product_id)
    for i in range(len(string_product_id)):
        print((i, string_product_id[i]))
