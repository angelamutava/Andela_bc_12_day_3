def find_missing(first_array, second_array):

	"""This is a simple function that finds the missing value between the two
	 lists and returns that value
      else returns zero.
	"""
	first_array = set(first_array)
	second_array = set(second_array)
	if first_array != second_array:
		new_array = list(second_array - first_array)
		for element in new_array:
			return element
	else:
		return 0