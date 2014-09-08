"""
Does the work for converting <h>
"""
def the_work(text):
    """
        This function takes in the text from getFile()
        then checks each word for header indicators.
        If one is found it removes the character and puts an
        appropriate <h>. After, returns the new text to getFile().

        to do: underlined headers
    """

    new_text = ""
    in_header = False   # bool to look for closing header tags
    htag = 0


    for word in text:

        if in_header == True:
            # if there's currently a header in the text

            if word == "\n":    # header ends at endline
                new_text = new_text + "</h" + str(htag) + ">"
                in_header = False

            elif word == "#":
                new_text = new_text + "</h" + str(htag) + ">"
                in_header = False

            else:
                new_text = new_text + word

        # h1
        else:

            if word == "#":
                word = "<h1>"
                htag = 1
                in_header = True

            new_text = new_text + word

    return new_text
