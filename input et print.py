nom = input('Quel est ton nom?: ')
age = int(input('Quel est ton age?: '))
#output = 'Bonjour {}. Tu as {} ans.'.format(nom,age)
print('Bonjour {}. Tu as {} ans.'.format(nom,age))

if(age > 20):
    print('Tu es vieux')

else: print('Tu es jeune')
