import ptag
import htag
def main():
	"""
		pass
	"""
	pass

def ptags(text):
	return ptag.theWork(text)

def htags(text):
	return htag.theWork(text)

def getFile():
	file_name = raw_input("\nEnter a file name: ")
	file_text = ""
	with open(file_name, 'r') as input_file:
		for word in input_file:
			file_text = str(file_text) + str(word)

	file_text = htags(file_text)
	file_text = ptags(file_text)
	return file_text

	# test to see if getFile works
	# print file_text




if __name__ == "__main__":
    main()
