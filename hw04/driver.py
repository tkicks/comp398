#!/usr/bin/env python
"""
The driver program

NOTE: Before running, check .css file to ensure that img and h1 tags are not
      changing the alignment. h1 should inline by default for all and that's it
"""
import converter

def main():
    """
        Runs the converter file

        No input
    """

    # set up html document to allow for css inclusion
    html_setup = ("<head>\n<link rel=\"stylesheet\" type=\"text/css\" "
        "href=\"stylesheet.css\"/>\n</head>\n")

    # get the text and convert md to html
    test_text = converter.get_file()
    test_text = converter.convert(test_text)

    # choose where to save file to
    file_name = raw_input("Enter a file name to save to: ")
    file_name = file_name

    # write to chosen file
    with open(file_name, 'w') as html_file:
        html_file.write(html_setup)
        html_file.write(str(test_text))


if __name__ == "__main__":
    main()
