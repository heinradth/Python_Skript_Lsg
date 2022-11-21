def autotest(kosten, klima):
	if(kosten < 20000):
		if (klima): 
			print("Auto wird gekauft")
		else: 
			print("Auto hat keine Klimaanlage")
	elif(klima == True):
		print("Auto ist zu teuer")
	else:
		print("Auto ist zu teuer und hat keine Klimaanlage")


