def scheSteiPap(a):
	liste = {
		"Schere": "Schere",
		"Stein": "Stein",
		"Papier": "Papier"
	}
	print(liste.get(a, "Weder noch"), "wurde gewählt.")