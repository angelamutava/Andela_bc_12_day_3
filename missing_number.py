def find_missing(first_array, second_array):

	"""This is a simple function that finds the missing value between the two
	 lists and returns that value
      else returns zero.
	"""
	first_array = set(first_array)
	second_array = set(second_array)
	if first_array != second_array:
		new_array = list(second_array - first_array)
		return new_array[0]
	else:
return 0