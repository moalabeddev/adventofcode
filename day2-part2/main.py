from input_puzzle import input_puzzle 
from tqdm import tqdm #تقدم 
import re

INVALID_PATTERN_ID_1 = r'^(\d+)\1$'
INVALID_PATTERN_ID_2 = r'^(\d+)(\1)+$'


def invalid_sum():
    product_ids=[]
    invalid_sum=0
    invalid_product_ids=[]
    for product_id_range in tqdm(input_puzzle, desc="Processing Puzzle Ranges"):
        lower_bound, upper_bound = product_id_range
        product_ids+= list(range(lower_bound, upper_bound+1))
    for i, product_id in enumerate(product_ids):
        if re.search(INVALID_PATTERN_ID_2, str(product_id)) is not None:
            invalid_sum +=int(product_id)
            invalid_product_ids.append((i, product_id))
                
    return "{0}\n {1}".format(invalid_sum , invalid_product_ids)
    
    
if __name__ == "__main__":
   
   print(invalid_sum())
