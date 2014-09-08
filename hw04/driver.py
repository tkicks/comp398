#!/usr/bin/env python
"""
The driver program
"""
import converter

def main():
    """
        Runs the converter file

        No input
    """

    html_setup = ("<head>\n<link rel=\"stylesheet\" type=\"text/css\" "
        "href=\"stylesheet.css\"/>\n")
    test_text = converter.get_file()
    test_text = converter.convert(test_text)

    with open("test.html", 'w') as html_file:
        html_file.write(html_setup)
        html_file.write(str(test_text))


if __name__ == "__main__":
    main()
