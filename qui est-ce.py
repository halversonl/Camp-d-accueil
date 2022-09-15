import random

yeux_bleus = input('Ton personnage a-t-il des yeux bleus? ').lower()


if(yeux_bleus == 'oui'):
    cheveux_rouges = input('Ton personnage a-t-il les cheveux rouges? ').lower()

    #Steven ou Anita, en se basant sur les cheveux rouges
    if(cheveux_rouges == 'oui'):
        print('Ton personnage est Steven.')
    elif(cheveux_rouges == 'non'):
        print('Ton personnage est Anita.')


elif(yeux_bleus == 'non' or 'NON'):
    cheveux = input('Ton personnage a-t-il des cheveux sur la tete? ').lower()

    #Charles ou pas Charles, en se basant sur les cheveux
    if(cheveux == 'non'):
        print('Ton personnage est Charles.')
    

    elif(cheveux == 'oui'):
        lunettes = input('Ton personnage porte-il des lunettes? ').lower()

        #Max ou pas Max, en se basant sur les lunettes
        if(lunettes == 'non'):
            print('Ton personnage est Max.')


       
        elif(lunettes == 'oui'):
            chapeau = input('Ton peronnage porte-il un chapeau? ')

            #Paul ou Sarah, en se basant sur le chapeau
            if(chapeau == 'oui'):
                print('Ton personnage est Sarah.')
            elif(chapeau == 'non'):
                print('Ton personnage est Paul')
        

