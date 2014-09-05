import ptag
import htag
def main():
	"""
		pass
	"""
	pass

def convert(text):
	new_text = "<p>"
	in_header = False	# bool to look for closing header tags
	header_string = ""
	htag = 0

	for word in text:

		# endline char and in_header == True
		if word == "\n" and in_header == True:
			new_text = new_text + "</h" + str(htag) + ">" + "</p><p>"
		elif word == "#" and in_header == True:
			new_text = new_text + "</h" + str(htag) + ">"
			in_header = False
		elif word == "##" and in_header == True:
			new_text = new_text + "</h" + str(htag) + ">"
			in_header = False

		# if it doesn't have a header
		if in_header == False:

		# h1
		elif word == "#"
			new_text = new_text + "<h1>"
			htag = 1
			in_header = True

		# h2
		elif word == "##"
			new_text = new_text + "<h2>"
			htag = 2
			in_header = True

		# h3
		elif word == "###" and in_header == False:
			new_text = new_text + "<h3>"
			htag = 3
			in_header = True
		elif word == "###" and in_header == True:
			new_text = new_text + "</h" + str(htag) + ">"
			in_header = False

		# h4
		elif word == "####" and in_header == False:
			new_text = new_text + "<h4>"
			htag = 4
			in_header = True
		elif word == "####" and in_header == True:
			new_text = new_text + "</h" + str(htag) + ">"
			in_header = False

		# h5
		elif word == "#####" and in_header == False:
			new_text = new_text + "<h5>"
			htag = 5
			in_header = True
		elif word == "#####" and in_header == True:
			new_text = new_text + "</h" + str(htag) + ">"
			in_header = False

		# h6
		elif word == "######" and in_header == False:
			new_text = new_text + "<h6>"
			htag = 6
			in_header = True
		elif word == "######" and in_header == True:
			new_text = new_text + "</h" + str(htag) + ">"
			in_header = False

		else:
			new_text = new_text + word


def getFile():
	file_name = raw_input("\nEnter a file name: ")
	file_text = ""
	with open(file_name, 'r') as input_file:
		for word in input_file:
			file_text = str(file_text) + str(word)

	return file_text

	# test to see if getFile works
	# print file_text




if __name__ == "__main__":
    main()
