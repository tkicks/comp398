#!/usr/bin/env python
import converter
import converter2

def main():
	"""
		Runs the converter file

		No input
	"""
	#test_text = converter.getFile()
	test_text = converter2.getFile()
	test_text = converter2.convert(test_text)
	#test_text = converter.ptags("Test text")

	with open("test.html", 'w') as html_file:
		html_file.write(str(test_text))





if __name__ == "__main__":
    main()
