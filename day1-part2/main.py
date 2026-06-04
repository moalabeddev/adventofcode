from raw_data import rotation_text
from library import (
    parse_rotations_to_signed_values, 
    cumulative_rotation_modulo_100, 
    count_crossings,
)


rotation_commands = rotation_text.splitlines()

signed_rotations = parse_rotations_to_signed_values(rotation_commands)

wrapped_positions = cumulative_rotation_modulo_100(signed_rotations)


print(count_crossings(signed_rotations, wrapped_positions))
