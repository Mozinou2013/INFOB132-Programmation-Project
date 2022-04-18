def IA_final(player_1, player_2, food, width, height):

    'attribue un numéro à chaque loup pour les distinguer (à voir)'

    if 'loup à moins de 2 cases de alpha:':
        'alpha recule et deux ou trois (ou plus) loups normaux les plus proches viendront en aide'

        if 'loup normaux moins de une case et au moins 20 pv':
            'les deux ou trois (ou plus) loups normaux attaquent'
        else:
            if 'if loups normaux ont plus de 20 pv':
                'loups normaux continuent à se rapprocher'
            else:
                if 'loups normaux près de nourriture':
                    'mange la nourriture'
                else:
                    'se rapproche de la nourriture (si possible dans le sens de l alpha'

        if 'omega a plus de 40 de vie et plus d un loup dans un rayon de 3-4 cases':
            'omega pacifie'
        elif 'omega a moins de 40 de vie ou un seul loup dans un rayon de 3-4 cases': #peut-être mettre "et" à la place de "ou"
            'omega se recule avec alpha'
        
        if 'autres loups normaux pas venus en défense à moins de une case de alpha ou omega adverses':
            'attaque'
        else:
            if 'omega adverse plus de 40 pv':
                'loups normaux se deplacent vers omega'
            else: 'omega adverse moins de 40':
                'se déplacent vers alpha' #attaque oméga adverse et si oméga mort, on attaque alpha 
        
    else: 'loups adverses à plus de deux cases de alpha et omega':

        if 'alpha ou omega ne sont pas à 100':
            'manger ou se déplacer ensemble vers la source de nourriture la plus proche'

        else:

            if 'loup adverses à moins de 5 cases de distances':
                'reculent ensemble' #et pacifie ? 

            else:

                 if 'pas de source de nourriture à moins de une case':
                    'se déplacent vers une source de nourriture pour plus tard'

                 else:'si nourriture autour'
                     'ne bougent pas'
        
        if 'autres loups normaux à moins de 20 pv':
            if 'nourriture à une case de distance': #à maximum une case 
                'mangent'
            else:
                'se déplacent vers nourriture la plus proche' 
        else:
            if 'alpha ou omega à moins d une case de distance': #à 1 case de distance parce qu'on ne peut pas être sur la même case (donc je pense pas que ça doit être à moins d'une case) ?
                'attaquent'
            else:
                if 'omega a plus de 39 pv':
                    if 'loups normaux a 100 pv':
                        'se rapprochent de omega'
                    elif 'loups normaux moins de 100':
                        if 'nourriture à une case de distance':
                            'mangent'
                        else:
                            'se rapprochent de omega'

                else: '(omega moins de 39 pv)':
                    if 'loups normaux a 100 pv': #peut-être mettre de 80 à 100 pv parce que je ne pense pas qu'ils seront souvent à 100 tout pile ?
                        'se rapprochent de alpha'
                    elif 'loups normaux moins de 100':
                        if 'nourriture à une case de distance':
                            'mangent'
                        else:
                            'se rapprochent de alpha' #du coup si oméga adverse a moins de 39 pv, d'après le rapport, on l'attaque lui avant d'aller attaquer l'alpha
