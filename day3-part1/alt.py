from input_puzzle import input_puzzle

battery_banks = input_puzzle.splitlines(keepends = False)
battery_banks = battery_banks[1:]

def index_of_highest_possible_voltage(battery_bank):
    
    for current_available_max_digit in range(9,0,-1):

        for index , battery in enumerate(battery_bank[::-1]):

            chop_index = len(battery) -2

            if current_available_max_digit == int(battery):

                print(index, current_available_max_digit, battery , battery_bank[(chop_index-index):])
                
                lead_battery_index = chop_index - index

                first_battery = battery_bank[lead_battery_index]
                
                return (first_battery, battery_bank[(chop_index-index+1):])

                break
        break
    
print(index_of_highest_possible_voltage(battery_banks[0]))


