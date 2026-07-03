from input_puzzle import input_puzzle

battery_banks = input_puzzle.splitlines(keepends = False)
battery_banks = battery_banks[1:]

result =0

class BatteryBankSlice(dict):
    def __str__(self):
        return "\n".join( ("{0}:{1}").format(k,v) for k,v in self.items())
        


def battery_bank_slices_per_possible_leading_battery(battery_bank)-> BatteryBankSlice:
    battery_bank_slice=BatteryBankSlice()
    for max_digit in range(9,0,-1):
        # print("max_digit",max_digit)
        for index, battery in enumerate(battery_bank[::-1]):
            # print(index, battery)
            if max_digit == int(battery):
                battery_bank_slice[index,max_digit] =battery_bank[-index:]
    return battery_bank_slice

def maximum_second_battery(battery_bank_slice):
    combinations = [ int(str(k[1])+max(v)) for k,v in battery_bank_slice.items()]
    return(max(combinations))

def total_voltage(battery_banks):
    for i, battery_bank in enumerate(battery_banks):
        chops = battery_bank_slices_per_possible_leading_battery(battery_bank)
        
        global result
        result+=maximum_second_battery(chops)
        print(i,maximum_second_battery(chops))
    print(result)

total_voltage(battery_banks)


