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
        elif 'omega a moins de 40 de vie ou un seul loup dans un rayon de 3-4 cases':
            'omega se recule avec alpha'
        
        if 'autres loups normaux pas venus en défense à moins de une case de alpha ou omega adverses':
            'attaque'
        else:
            if 'omega adverse plus de 40 pv':
                'loups normaux se deplacent vers omega'
            else: 'omega adverse moins de 40':
                'se déplacent vers alpha'
        
    else: 'loups adverses à plus de deux cases de alpha et omega':

        if 'alpha ou omega ne sont pas à 100':
            'manger ou se déplacer ensemble vers la source de nourriture la plus proche'

        else:

            if 'loup adverses à moins de 5 cases de distances':
                'reculent ensemble'

            else:

                 if 'pas de source de nourriture à moins de une case':
                    'se déplacent vers une source de nourriture pour plus tard'

                 else:'si nourriture autour'
                     'ne bougent pas'
        
        if 'autres loups normaux à moins de 20 pv':
            if 'nourriture à une case de distance':
                'mangent'
            else:
                'se déplacent vers nourriture la plus proche'
        else:
            if 'alpha ou omega à moins d une case de distance':
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
                    if 'loups normaux a 100 pv':
                        'se rapprochent de alpha'
                    elif 'loups normaux moins de 100':
                        if 'nourriture à une case de distance':
                            'mangent'
                        else:
                            'se rapprochent de alpha'
