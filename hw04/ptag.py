def theWork(text):
	"""
		This function takes in the text from getFile()
		then checks each word for a line break character.
		If one is found it removes the character and closes
		the current <p> and starts up a new one. After, returns
		the new text to getFile().

		TODO: md line break == "  br"
		FOR THE MOMENT: does NOT remove endline char
	"""
	# last_word = ""
	# two_words = ""
	new_text = "<p>"
	for word in text:
		"""
		Testing for md line break
		if word == " ":
			two_words = last_word
			last_word = word
		if (word == "\n" and last_word == " " and two_words == " "):
			new_text = new_text + "</p>"
			"""
		if word == "\n":
			new_text = new_text + "</p>" + "<p>"
		else:
			new_text = new_text + word
	print new_text
	return new_text
