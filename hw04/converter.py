"""
This program will open the file the user asks for and read it to a string,
then return the string. It will also call the other functions to convert
the markdown to html.
"""
import ptag
import htag
import btag
import etag
import ltag
import atag
def main():
    """
        pass
    """
    pass

def ptags(text):
    """
    Calls function from other file to convert <p>
    """
    return ptag.the_work(text)

def htags(text):
    """
    Calls function from other file to convert <h>
    """
    return htag.the_work(text)

def btags(text):
    """
    Calls function from other file to convert <blockquote>
    """
    return btag.the_work(text)

def etags(text):
    """
    Calls function from other file to convert <em>
    """
    return etag.the_work(text)

def ltags(text):
    """
    Calls function from other file to convert <li>
    """
    return ltag.the_work(text)

def atags(text):
    """
    Calls function from other file to convert <a href>
    """
    return atag.the_work(text)

def get_file():
    """
    Reads file from input
    """
    file_name = raw_input("\nEnter a file name: ")
    file_text = ""
    with open(file_name, 'r') as input_file:
        for word in input_file:
            file_text = str(file_text) + str(word)

    return file_text

def convert(file_text):
    """
    Calls all helper functions
    """
    file_text = btags(str(file_text))
    file_text = ltags(str(file_text))
    file_text = ptags(str(file_text))
    file_text = htags(str(file_text))
    file_text = etags(str(file_text))
    file_text = atags(str(file_text))
    return file_text




if __name__ == "__main__":
    main()
