"""
Does the work for converting <li>.
"""
def the_work(text):
    """
        This function takes in the text from convert
        then checks each word for a + or - character.
        If one is found it removes the character and either initiates
        or closes a list.
        After, returns the new text to getFile().
    """

    new_text = ""
    # check to see if the list is over at each newline
    last_word = ""
    in_ulist = False
    # in_olist = False
    for word in text:

        if in_ulist == True:
            if word == "+" or word == "-":
                new_text = new_text + "<li>"
                last_word = word
            # needs () to compare correctly
            elif ((word != "+" or word != "-") and last_word == "\n"):
                new_text = new_text + "</ul>" + word
                in_ulist = False
                last_word = word
            else:
                new_text = new_text + word
                last_word = word

        # elif in_olist == True:
        #   if last_word.isdigit() == True and word == ".":
        #       new_text = new_text + "<li>"
        #       last_word = word
        #   elif word.isdigit() == False and last_word == "\n":
        #       new_text = new_text + "</ol>" + word
        #       sin_olist = False
        #       last_word = word
        #   else:
        #       new_text = new_text + word
        #       last_word = word

        # ols not supported. bug with compatability with btags

        else:
            if word == "+" or word == "-":
                new_text = new_text + "<ul><li>"
                in_ulist = True
                last_word = word
            # elif word.isdigit() == True:
            #   new_text = new_text + "<ol><li>"
            #   in_olist = True
            #   last_word = word
            else:
                new_text = new_text + word
                last_word = word

    return new_text
