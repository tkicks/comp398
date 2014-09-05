import ptag2
import htag2
def main():
	"""
		pass
	"""
	pass

def ptags(text):
	return ptag2.theWork(text)

def htags(text):
	return htag2.theWork(text)

def getFile():
	file_name = raw_input("\nEnter a file name: ")
	file_text = ""
	with open(file_name, 'r') as input_file:
		for word in input_file:
			file_text = str(file_text) + str(word)

	return file_text

def convert(file_text):
	file_text = htags(str(file_text))
	file_text = ptags(str(file_text))
	return file_text




if __name__ == "__main__":
    main()
