#As a replacement for  (find_revolution_indices, revolution_count_map,revolution_count_list, count_revolutions)
def revolution_counter(wrapped_positions, signed_rotations):
    revolution_counter=0
    for index in range(len(wrapped_positions)):
        if signed_rotations[index]<0:
            while wrapped_positions[index+1]-wrapped_positions[index]>0:
                if wrapped_positions[index+1]-wrapped_positions[index] ==0:
                    revolution_counter+=1
                continue
                
        else:
            while wrapped_positions[index+1]-wrapped_positions[index]!=0:
            if wrapped_positions[index+1]-wrapped_positions[index] ==0:
                revolution_counter+=1
