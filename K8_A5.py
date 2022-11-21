def kino(regen, freund, guthaben):
	if(regen == True and (freund == True or guthaben >= 20)):
		print("Geht ins Kino.")
	else:
		print("Zu Hause bleiben.")