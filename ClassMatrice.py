# -*-- coding: utf-8 --*-


#-------------------------------------------------------------#
#   Projet Python - 2020                                    #
#                                                         #
#   CALCUL MATRICIEN                                     #
#                                                        #
#   Auteur : Donatien Dinyad Yeto                         #
#   Version : 1.0                                           #
#--------------------------------------------------------------#


import numpy as np
import copy,random
from fractions import Fraction





class Matrice():
	def __init__(self,nl,nc):
		self.nl = nl
		self.nc = nc
		self.matrix=np.zeros((nl,nc))

	def __str__(self):
		m=str(self.matrix)
		m=" "+m[1:len(m)-1]
		m=m.replace("[","( ")
		m=m.replace("]"," )")

		return m
	def afficher(self):
		for i in range(self.nl):
			for j in range(self.nc):
				a=Fraction(self.matrix[i,j])
				print(a)
			print("\n")



	def setAllCoef(self,coefs):
		""" 
		Les coefficients de la marice
		Entrez les coefficients sous la forme -> coefs:[[..]...[...]].')"""

		self.matrix=np.array(coefs)
		return self;


	def setCoef(self,i,j,n):
		""" Modifier le coefficient d'indice i,j."""
		self.matrix[i][j]=n
		return self;

	def transpose(self):
		"""La transposé"""
		m=copy.copy(self)
		m.nl=self.nc
		m.nc=self.nl
		m.matrix=self.matrix.T
		return m

	def somme(self,b):
		if self.nl == b.nl and self.nc == b.nc :
			m=copy.copy(self)
			m.nl=b.nl
			m.nc=b.nc
			m.matrix=self.matrix+b.matrix
			return m
		else:
			print("Somme impossible :  format = ", b.format(),' +',self.format())

	def soustraction(self,b):
		if self.nl == b.nl and self.nc == b.nc :
			m=copy.copy(self)
			m.nl=b.nl
			m.nc=b.nc
			m.matrix=self.matrix-b.matrix
			return m
		else:
			print("Soustraction impossible : format = ", b.format(),' - ',self.format())

	def produit(self,b,inv=False):
		if not inv:
			if self.nc == b.nl:
				m=copy.copy(self)
				m.nl=self.nl
				m.nc=b.nc
				m.matrix=self.matrix @ b.matrix
				return m
			else:
				print("Produit impossible :  format = ", self.format(),' x ',b.format())

		else :
			if self.nl == b.nc:
				m=copy.copy(self)
				m.nl=b.nl
				m.nc=self.nc
				m.matrix=b.matrix @ self.matrix 
				return m
			else:
				print("Produit impossible : ", b.format(),' x ',self.format())



	def sousMatrice(self,I,J,plus=False):
		"""
		Extraire une sous matrices en supprimant la ligne d'indixe I et la colonne d'indixe J.

		Si plus est true, on il y a possibilité de supprimer pluisieurs lignes et colonnes. 
		Les lignes et les colonnes à extraire sont respectivement fournis respectivement dans I et J qui sont dans ce cas des listes.
		
		"""
		n=0
		a=self.matrix
		if plus:
			nl=self.nl-len(I)
			nc=self.nc-len(J)
			for i in I:
				a=np.delete(a,i-1-n,0)
				n=n+1

			for j in J:
				a=np.delete(a,j-1-n,1)
				n=n+1

		else:
			nl=self.nl-1
			nc=self.nc-1
			a=np.delete(a,I-1,0)
			a=np.delete(a,J-1,1)

		m=copy.copy(self)
		m.nl=nl
		m.nc=nc
		m.matrix=a

		return m


	def mineur(self,i,j):
		if self.nl == self.nc:
			return self.sousMatrice(i,j).determinant()
		else:
			print("Erreur : La matrice n'est pas carrée !")

	def cofacteur(self,i,j):
		if self.nl == self.nc:
			return pow(-1,i+j)*self.mineur(i,j)
		else:
			print("Erreur : La matrice n'est pas carrée !")

	def comatrice(self):
		if self.nl == self.nc:
			m=copy.copy(self)
			m.nl=self.nl
			m.nc=self.nc
			m.matrix=np.zeros((m.nl,m.nc))

			for i in range(m.nl):
				for j in range(m.nc):
					m.matrix[i,j]=self.cofacteur(i+1,j+1)
			return m
		else:
			print("Erreur : La matrice n'est pas carrée !")
	


	def determinant(self):
		if self.nl == self.nc:
			if self.nl == 1: 
				return self.matrix[0]
			elif self.nl == 2:
				return self.matrix[0,0]*self.matrix[1,1]-self.matrix[1,0]*self.matrix[0,1]
			else:
				d=0
				for j in range(self.nc):
					d=d+(self.matrix[0,j])*self.cofacteur(1,j+1)
				return d
		else :
			print("Erreur : La matrice n'est pas carrée !")


	def isInversible(self):
		if self.determinant() == 0 :
			return False
		else:
			return True

	def isCarree(self):
		if self.nl == self.nc:
			return True
		else:
			return False

	def isTriangulaireSup(self):
		t=True
		for i in range(self.nl):
			for j in range(self.nc):
				if i > j:
					if self.matrix[i,j] != 0 :
						t=False

		return t

	def isTriangulaireInf(self):
		t=True
		for i in range(self.nl):
			for j in range(self.nc):
				if i < j:
					if self.matrix[i,j] != 0 :
						t=False

		return t

	def isTriangulaire(self):
		return self.isTriangulaireInf() or self.isTriangulaireSup()


	def isDiagonale(self):
		if self.isCarree():
			for i in range(self.nl):
				for j in range(self.nc):
					if i != j and  self.matrix[i,j] != 0:
						return False
			return True
		else:
			print("Erreur : La matrice n'est pas carrée !")



	def isEchelon(self):
		infNull=True
		for i in range(self.nl):
			if not self.isLigneNull(self.nl-i):
				break
		for j in range(self.nl):
			if self.nl-i > j:
				if self.isLigneNull(j+1):
					infNull=False

		if not infNull:
			return False
		indix=0
		for i in range(self.nl):
			if not self.isLigneNull(i+1):
				for j in range(self.nc):
					if self.matrix[i,j] != 0:
						indix=j
						break
				for k in range(self.nl):
					if k > i:
						if self.matrix[k,indix] != 0:
							return False
				indix=0

		return True

	def isEchelonReduit(self):
		if not self.isEchelon():
			return False

		for i in range(self.nl):
			if not self.isLigneNull(i+1):
				for j in range(self.nc):
					if self.matrix[i,j] != 0:
						if self.matrix[i,j] != 1:
							return False

						for k in range(self.nl):
							if i > k:
								if self.matrix[k,j] != 0:
									return False
						break

		return True

	def echelonner(self):
		m=self.matrix.copy()
		ind=0
		for i in range(self.nl):

			for j in range(self.nc):

				if m[i,j] != 0:
					print("Pivot : (",i,j,') :',m[i,j])
					
					for k in range(self.nl):
						if k > i:
							if m[k,j] != 0:

								m[k]=(m[i,j]*m[k]-m[k,j]*m[i]).copy()
								print(m)
								print("\n")
					break

				else:
					l=self.debutNonNull(m,i+1,j)
					if len(l) != 0:
						h=l[0]
						tmp=m[i].copy()
						m[i]=m[h].copy()
						m[h]=tmp.copy()
						print("Pivot : (",i,j,') :',m[i,j])
						for k in range(self.nl):
							if k > i:
								if m[k,j] != 0:
									m[k]=(m[i,j]*m[k]-m[k,j]*m[i]).copy()
									print(m)
									
									
						break

		for i in range(self.nl):

			for j in range(self.nc):

				if m[i,j] != 0:
					for k in range(i):
						if m[k,j] != 0:
							m[k]=(m[i,j]*m[k]-m[k,j]*m[i]).copy()
					break

		for i in range(self.nl):

			for j in range(self.nc):

				if m[i,j] != 0:
					if m[i,j] != 1:
						m[i]=(m[i]/m[i,j]).copy()
					break


		p=copy.copy(self)
		p.nl=self.nl
		p.nc=self.nc
		p.matrix=m

		return p


	def debutNonNull(self,m,l,c):
		L=[]
		for i in range(self.nl):
			if i >= l:
				if m[i,c] != 0:
					L.append(i)
		return L



	def isLigneNull(self,nl):
		for i in range(self.nc):
			if self.matrix[nl-1,i] != 0:
				return False
		return True




	def inverse(self):
		if self.nl == self.nc:
			if self.isInversible():
				Tcom=self.comatrice().transpose()

				m=copy.copy(self)
				m.nl=self.nl
				m.nc=self.nc
				m.matrix=np.zeros((m.nl,m.nc))

				for i in range(m.nl):
					for j in range(m.nc):
						m.matrix[i,j]=Tcom.matrix[i,j]/self.determinant()
				return m
			else:
				print("La matrice n'est pas inversible !")

		else:
			print("Erreur : La matrice n'est pas carrée !")
		

	def format(self):
		return self.matrix.shape

	def rang(self):
		pass

	def trace(self):
		return self.matrix.trace()

	

def conbinaisonsPossibles(k,seq):
	"""
	Donne toutes les possibilité de conbinaison de k élément dans la liste seq.
	"""
	p = []
	i, imax = 0, 2**len(seq)-1
	while i<=imax:
		s = []
		j, jmax = 0, len(seq)-1
		while j<=jmax:
			if (i>>j)&1==1:
				s.append(seq[j])

			j += 1
		if len(s)==k:
			p.append(s)
		i += 1 
	return p
            


# Queques exemples d'utilisations
#-----------------------------------------------------------
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

	
	

