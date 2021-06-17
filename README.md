
# Calcul-Matricien-Python-Numpy



# Queques exemples d'utilisations
#-----------------------------------------------------------
#........

if __name__ == '__main__':

	matrice1=Matrice(6,5)
	
	matrice1.setAllCoef([
	             	[5,0,3,3,7],
	             	[2,1,1,0,2],
	             	[0,4,0,1,0],
	             	[12,5,0,6,1],
	             	[1,3,1,0,11],
	             	[7,1,7,1,0]
	             ])

	matrice2=Matrice(4,5).setAllCoef([
	             	[5,0,3,3,7],
	             	[0,0,0,6,1],
	             	[1,0,1,0,11],
	             	[0,0,7,1,0]
	             ])


	matriceCarre=Matrice(3,3).setAllCoef([
	             	[3,-2,5],
	             	[1,-1.0/3,2.0/5],
	             	[-2,3,1]
	             ])

	# Afficher
	print(matrice1)
	print("____________________\n")

	#Transposé
	print(matrice1.transpose())
	print("____________________\n")

	#Somme
	print(matrice1.produit(matrice2))
	print("____________________\n")


	#Sous matrice
	print(matrice1.sousMatrice(1,2))
	print("\n_____________")
	print(matrice1.sousMatrice([1,2],[2],True))

	#Déterminant
	print(matriceCarre.isCarree())
	print(matriceCarre.isInversible())
	print(matriceCarre.determinant())

	#Inverse
	print("\n_____________")
	print(matriceCarre.inverse())
