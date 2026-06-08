def generate_product_ids(input_puzzle:str) ->list[int]:
    product_ids=[]
    for interval in input_puzzle:
        lower_bound, upper_bound = tuple(interval)
        product_ids += (list(range(lower_bound, upper_bound)))
    return product_ids

def stringify_product_ids(product_ids: list[int]) -> list[str]:
    stringified_product_ids = [str(product_id) for product_id in product_ids]
    return stringified_product_ids
