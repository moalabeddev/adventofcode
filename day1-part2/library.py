import math

def parse_rotations_to_signed_values(rotation_commands):
    signed_rotations = []

    for command in rotation_commands:
        if "L" not in command:  # Right rotation
            command = command.replace("R", "")

        command = command.replace("L", "-")

        if command:
            signed_rotations.append(int(command))

    return signed_rotations

def cumulative_rotation_modulo_100(signed_rotations):
    wrapped_positions = []
    current_position = 50

    for rotation in signed_rotations:
        current_position = (current_position + rotation) % 100
        wrapped_positions.append(current_position)

    return wrapped_positions

def find_zero_position_indices(wrapped_positions):
    zero_indices = []

    for index, wrapped_position in enumerate(wrapped_positions):
        if wrapped_position == 0:
            zero_indices.append(index)

    return zero_indices

def count_zero_positions(wrapped_positions):
    zero_count = 0

    for wrapped_position in wrapped_positions:
        if wrapped_position == 0:
            zero_count += 1

    return zero_count

#todo inspect this function
def find_revolution_indices(signed_rotations):
    revolution_indices = []
    wrapped_positions = cumulative_rotation_modulo_100(signed_rotations)

    for index in range(len(signed_rotations)):
        if index == 0:
            effective_rotation = 50
        else:
            effective_rotation = (
                wrapped_positions[index]
                - wrapped_positions[index - 1]
            )

        crossed_boundary = (
            effective_rotation != signed_rotations[index]
            and wrapped_positions[index] != 0
            and index != 0
        )

        if crossed_boundary:
            revolution_indices.append(index)

    return revolution_indices

def revolution_count_map(revolution_indices,rotation_commands):
    signed_rotations = parse_rotations_to_signed_values(rotation_commands)
    revolution_count_map = {
        revolution_index:{
            
            "signed_rotation":signed_rotations[revolution_index], 
            "revolution_count": -(math.floor(signed_rotations[revolution_index]/100)) if signed_rotations[revolution_index]<=0 else math.ceil(signed_rotations[revolution_index]/100)
            
        } for revolution_index in revolution_indices
        
    }
    return revolution_count_map
    
def revolution_count_list(revolution_count_map):
    revolution_count_list=[]
    for key , value in revolution_count_map.items():
        for key, value in value.items():
            if key=="revolution_count":
                revolution_count_list.append(value)
    return revolution_count_list

def count_revolutions(revolution_count_list):
    return sum(revolution_count_list)
