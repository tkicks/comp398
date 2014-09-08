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
import itag
import ctag
import os
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

def itags(text):
    """
    Calls function from other file to convert <img>
    """
    return itag.the_work(text)

def ctags(text):
    """
    Calls function from other file to convert <code>
    """
    return ctag.the_work(text)

def get_file():
    """
    Reads file from file name input to string
    """
    file_name = raw_input("\nEnter a file name to open: ")
    file_text = ""

    # check if the file exists
    if os.path.isfile(file_name) == True:
        # if it does read file to string
        with open(file_name, 'r') as input_file:
            for word in input_file:
                file_text = str(file_text) + str(word)

            return file_text
    else:
        # if it doesn't try again
        print "Could not find file. Try again."
        return get_file()

def convert(file_text):
    """
    Calls all helper functions
    """
    file_text = btags(str(file_text))
    file_text = ctags(str(file_text))
    file_text = ltags(str(file_text))
    file_text = ptags(str(file_text))
    file_text = htags(str(file_text))
    file_text = etags(str(file_text))
    file_text = itags(str(file_text))
    file_text = atags(str(file_text))
    return file_text




if __name__ == "__main__":
    main()
