"""
Does the work for converting <h>
"""
def the_work(text):
    """
        This function takes in the text from getFile()
        then checks each word for header indicators.
        If one is found it removes the character and puts an
        appropriate <h>. After, returns the new text to getFile().

        NOTE: Does not support underlined headers or headers other than h1
    """

    new_text = ""       # string to hold new text
    in_header = False   # is there a closing tag?
    htag = 0            # var to hold what type of htag (not useful as is)


    for word in text:

        # if in an <h>
        if in_header == True:

            # if the current word is an endline or closing symbol (md)
            if word == "\n" or word == "#":
                # add a closing tag to new string and declare out of header
                new_text = new_text + "</h" + str(htag) + ">"
                in_header = False

            # if it's just another word
            else:
                # add it to new string
                new_text = new_text + word

        # if it's not inside a header
        else:

            # if the current word is a header initiation character
            if word == "#":
                # change word to h1 tag (only supported), declare htag to 1
                # declare in header
                word = "<h1>"
                htag = 1
                in_header = True

            # add current word to new text regardless of <h> or not
            new_text = new_text + word

    return new_text
