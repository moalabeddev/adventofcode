from input_puzzle import input_puzzle

#todo use a generator
def generate_product_ids():

    product_ids=[]
    for product_id_range in input_puzzle:
        boundary_start, boundary_end =product_id_range
        for element in list(range(boundary_start,boundary_end+1)):
            product_ids.append(element)
            
    return product_ids


product_ids = generate_product_ids()

data= {product_id:len(str(product_id)) for product_id in product_ids if len(str(product_id))%2 ==0 }



for number in data.keys():
    print("="*10)
    number=str(number)
    print(number)
    length = len(number)
    print(length)
    midpoint = int(len(number)/2)
    print(midpoint)
    
    flag=True
    for index in range(len(number)):
        print(index)
        if number[0+index] == number[midpoint+index]:
            flag*=True
        
    print("is valid flag:",flag)
