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

    wrapped_positions.insert(0,50) #initial position before application of signed rotations
    return wrapped_positions

def count_crossings(signed_rotations, wrapped_positions):
    crossing_counter=0
    for i in range(len(signed_rotations)):
        #print(i, "Index") #debugging
        if signed_rotations[i]>0:
            #print("=",signed_rotations[i], "signed_rotations") #debugging
            applied_rotations=0
            
            while applied_rotations<signed_rotations[i]:
                
                if (wrapped_positions[i]+applied_rotations)%100 == 0:
                    crossing_counter +=1
                    #print("===",crossing_counter, "crossing_counter!!!") #debugging
                applied_rotations +=1
                #print("==",applied_rotations, "applied_rotations") #debugging
        else:
            #print("=",signed_rotations[i],"signed_rotations") #debugging
            applied_rotations=0
            
            while applied_rotations< -(signed_rotations[i]):
                
                if (wrapped_positions[i]-applied_rotations)%100 == 0:

                    crossing_counter+=1
                    #print("===",crossing_counter, "crossing_counter!!!") #debugging
                applied_rotations +=1
                #print("==",applied_rotations, "applied_rotations") #debugging
    return crossing_counter
