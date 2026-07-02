from input_puzzle import input_puzzle

battery_banks = input_puzzle.splitlines(keepends = False)
battery_banks = battery_banks[1:]

    
def search_two_highest_batteries(battery_bank):

    highest_battery= max(battery_bank)

    new_battery_bank = remove_highest_voltage_battery(battery_bank, highest_battery)
    
    second_highest_battery = max(new_battery_bank)
    
    two_highest_batteries = arrange_two_highest_batteries(battery_bank, highest_battery , second_highest_battery)
    
    return two_highest_batteries
    
    
def remove_highest_voltage_battery(battery_bank,highest_battery):
    new_battery_bank =list(filter(lambda x : x!= highest_battery, battery_bank))
    return new_battery_bank
    
def arrange_two_highest_batteries(battery_bank, highest_battery , second_highest_battery):
    highest_battery_index = battery_bank.index(highest_battery)
    second_highest_battery_index = battery_bank.index(second_highest_battery)
    if highest_battery_index < second_highest_battery_index:
        return "".join((highest_battery, second_highest_battery))
    else:
        return "".join((second_highest_battery, highest_battery))
        
if __name__ == "__main__":
    for i , battery_bank in enumerate(battery_banks):
        print(i, (sorted(battery_bank)[-2:], search_two_highest_batteries(battery_bank)))
        
    print("="*60)
    
    result=sum(int(search_two_highest_batteries(battery_bank)) for battery_bank in battery_banks )
    print(result)
