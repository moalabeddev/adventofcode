from input_puzzle import input_puzzle
import re

banks = input_puzzle.strip().splitlines()

def version_1():
    answer=0
    for bank in banks:
        unique_voltages=set(bank)
        print("="*20)
        print(sorted(list(unique_voltages)),"\n")
        print(sorted(list(unique_voltages))[-2:],"\n")
        print(sorted(list(unique_voltages))[-2:],"\n")    
        max_unique_voltages = sorted(list(unique_voltages))[-2:]
        print(list(map(int,max_unique_voltages)))
        print(sum(map(int,max_unique_voltages)))
        print("="*20)
        answer+=sum(map(int,max_unique_voltages))
    return answer
    
    
def version_2():
    answer=0
    for bank in banks:
        print("="*20)
        print(bank, "\n")
        print(sorted(list(bank)),"\n")
        print(sorted(list(bank))[-2:],"\n")
        print(sorted(list(bank))[-2:],"\n")    
        max_voltages = sorted(list(bank))[-2:]
        print(list(map(int,max_voltages)))
        print(sum(map(int,max_voltages)))
        print("="*20)
        answer+=sum(map(int,max_voltages))
    return answer

def sanity_check():
    import math
    max_bank_count= -math.inf
    min_bank_count= +math.inf
    
    input_puzzle_length = len(input_puzzle)
    split_and_stripped_banks_count = len(banks)
    
    total_character_count=0
    for bank in banks:
        if len(bank)> max_bank_count:
            max_bank_count=len(bank)
        
        if len(bank)< min_bank_count:
            min_bank_count=len(bank)
            
        total_character_count+=len(bank)
    return "{0} == {1} * {2} ? max={3} min={4}".format(input_puzzle_length,split_and_stripped_banks_count , total_character_count ,min_bank_count, max_bank_count)
    
if __name__ == "__main__":
    version_1()
    version_2()
    print(sanity_check())
