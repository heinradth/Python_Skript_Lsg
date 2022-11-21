def aufzaehlen(newList):
	
	print(newList[0])
	print(newList[1])
	print(newList[2])

def sort(a, b, c):

	liste = [a, b, c]

	if (liste[0] >= liste[1]): 
		liste[0], liste[1] = b, a

	if (liste[1] >= liste[2]):
		liste[2], liste[1] = liste[1], c

	if (liste[0] >= liste[1]):
		liste[0], liste[1] = liste[1], liste[0]

	aufzaehlen(liste)
				







