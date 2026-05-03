
Earned_Income= float(input("Enter the amount of income you earned in 2023: "))
Marital_Status = str(input("Are you married or single?"))
taxOwed = 0
if Marital_Status =='s':
	if 0<= Earned_Income < 11000:
		taxOwed = Earned_Income * 0.10
	elif 11001<=Earned_Income < 44725:
		taxOwed = 11000* 0.1+ ((Earned_Income - 11000) * 0.12)
	elif Earned_Income < 95375:
		taxOwed= (11000*0.1) +((44725-11000) *0.12) + ((Earned_Income - 44725) * 0.22)			
	
	else :
		print('Income too high')
	print(f'This year you owe {taxOwed:.2f} in taxes')
if Marital_Status =='m':
	if 0 <= Earned_Income < 22000:
			taxOwed= Earned_Income * 0.10
	elif 22001 <= Earned_Income < 89450:
			taxOwed = 22000* 0.1+ ((Earned_Income - 22000) * 0.12)
	elif 89451 <= Earned_Income < 190750:
		taxOwed= (22000*0.1)+((89450 - 22000) *0.12) + ((Earned_Income - 89450) * 0.22)
	else:
		print('Income too high')
	print(f'This year you owe {taxOwed:.2f} in taxes')
