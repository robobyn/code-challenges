def is_palindrome(word):
	"""Check string and return boolean for whether or not str is palindrome"""

	if word != word[::-1]:
		return False

	return True