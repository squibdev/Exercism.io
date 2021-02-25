def is_leap_year(year):
	pass
	# check if year is divisible by 4
	if year % 4 == 0:
		# check if year is divisible by 100
		if year % 100 == 0:
			# check if year is divisible by 400
			if year % 400 == 0:
				return True
			return False
		return True
	else:
		return False