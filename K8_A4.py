def handytest(kosten, kameras, akku, model):
	curModel = {
		"Samsung": True,
		"Apple": True
	}
			
	if(kosten < 1000 and kameras >= 3 and akku >= 2 and curModel.get(model, False)):
		print("Handy kaufen")
	else:
		print("Handy durchgefallen")