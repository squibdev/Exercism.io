def abbreviate(words):
	pass

	# Creeate an output string for the result to be stored in
	output = ""

	# Loop through every word
	for i in words.upper().split():
		if i[0].isalpha() == True:
			output += i[0]
		else:
			output += i[1]