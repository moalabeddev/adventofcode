import math
from raw_data import rotation_text
from library import (
    parse_rotations_to_signed_values, 
    cumulative_rotation_modulo_100, 
    count_zero_positions,
    find_revolution_indices,
    revolution_count_map,
    revolution_count_list,
    count_revolutions
)

rotation_commands = rotation_text.splitlines()

signed_rotations = parse_rotations_to_signed_values(rotation_commands)

wrapped_positions = cumulative_rotation_modulo_100(signed_rotations)

zero_count = count_zero_positions(wrapped_positions)
print(zero_count)

revolution_indices = find_revolution_indices(signed_rotations)

revolution_count_map=revolution_count_map(revolution_indices, rotation_commands)

revolution_count_list=revolution_count_list(revolution_count_map)

revolution_count=count_revolutions(revolution_count_list)

print(revolution_count)

print(zero_count+revolution_count)
