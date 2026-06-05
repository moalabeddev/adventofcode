from puzzle_input import puzzle_input

_dict = {
    str(segment): {
        number 
        for number in list(range(segment[0], segment[1] + 1))
    }
    for segment in puzzle_input
}

print(_dict)
