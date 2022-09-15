pdv = int(input("Quel est le prix de vente de votre produit? "))
pdf = int(input("Quel est le prix de fabrication de votre produit? "))

profit = pdv - pdf
perte = pdf - pdv
if(pdv > pdf):
    print("Vous faites un profit de {}$ avec chaque vente.".format(profit))
elif(pdf > pdv):
    print("Vous perdez {}$ avec chaque vente.".format(perte))
else:
    print("Vous perdez ni gagnez rien avec chaque vente.")
