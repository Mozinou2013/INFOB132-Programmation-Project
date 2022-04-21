
for key in player_A :
        if player_A[key]['type'] == 'omega':
            life_omega_A = player_A[key]['life']
            pos_omega_A = key

        if player_A[key]['type']== 'alpha':
            life_alpha_A = player_A[key]['life']
            pos_alpha_A = key 


for key in player_B :
        if player_B[key]['type'] == 'omega':
            life_omega_B = player_B[key]['life']
            pos_omega_B = key

        if player_B[key]['type']== 'alpha':
            life_alpha_B = player_B[key]['life']
            pos_alpha_B = key 

pos_alpha_omega_A = {pos_alpha_A : 'alpha', pos_omega_A : 'omega'}