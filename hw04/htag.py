def theWork(text):
	"""
		This function takes in the text from getFile()
		then checks each word for header indicators.
		If one is found it removes the character and puts an
		appropriate <h>. After, returns the new text to getFile().

		TODO: underlined headers
	"""
	
	new_text = ""
	check_text = ""
	in_header = False	# bool to look for closing header tags
	htag = 0


	for word in text:

		if in_header == True:
			# if there's currently a header in the text

			if word == "\n":	# header ends at endline
				new_text = new_text + "</h" + str(htag) + ">"
				in_header = False

			elif word == "#":
				new_text = new_text + "</h" + str(htag) + ">"
				in_header = False
		
			elif word == "##":
				new_text = new_text + "</h" + str(htag) + ">"
				in_header = False

			elif word == "###":
				new_text = new_text + "</h" + str(htag) + ">"
				in_header = False

			elif word == "####":
				new_text = new_text + "</h" + str(htag) + ">"
				in_header = False

			elif word == "#####" and in_header == True:
				new_text = new_text + "</h" + str(htag) + ">"
				in_header = False

			elif word == "######" and in_header == True:
				new_text = new_text + "</h" + str(htag) + ">"
				in_header = False

		# h1
		elif word == "#" and in_header == False:
			new_text = new_text + "<h1>"
			htag = 1
			in_header = True
		
		# h2
		elif word == "##" and in_header == False:
			new_text = new_text + "<h2>"
			htag = 2
			in_header = True

		# h3
		elif word == "###" and in_header == False:
			new_text = new_text + "<h3>"
			htag = 3
			in_header = True

		# h4
		elif word == "####" and in_header == False:
			new_text = new_text + "<h4>"
			htag = 4
			in_header = True

		# h5
		elif word == "#####" and in_header == False:
			new_text = new_text + "<h5>"
			htag = 5
			in_header = True

		# h6
		elif word == "######" and in_header == False:
			new_text = new_text + "<h6>"
			htag = 6
			in_header = True

		else:
			new_text = new_text + word

	return new_text
