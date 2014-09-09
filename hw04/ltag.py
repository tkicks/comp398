"""
Does the work for converting <li>.
"""

def the_work(text):
    """
        This function takes in the text from convert
        then checks each word for a + or - character.
        If one is found it removes the character and either initiates
        or closes a list.
        After, returns the new text to convert().

        NOTE: Does not support * indicators or nested lists
              Slight bug with initiating an ol - first number outside tag
    """

    new_text = ""       # string for new text
    last_word = ""      # string for the last word
    in_ulist = False    # is in ul
    in_olist = False    # is in ol

    for word in text:

        # if it's inside an ul
        if in_ulist == True:
            # if current word is indicator and last word was newline
            if ((word == "+" or word == "-") and last_word == "\n"):
                # add tag to new string
                new_text = new_text + "<li>"
            # if the current word is not an indicator and last word was newline
            elif ((word != "+" or word != "-") and last_word == "\n"):
                # add ul close and current word to new string (not indicator)
                # declare not in ul
                new_text = new_text + "</ul>" + word
                in_ulist = False
            # if word is list text
            else:
                # add word to new list
                new_text = new_text + word

        # if it's inside an ol
        elif in_olist == True:
            # check if list continues
            if word == "." and last_word.isdigit() == True:
                # add list tag
                new_text = new_text + "<li>"
            # if last word was a number and current word isn't indicator
            # case: it's part of the list
            elif word != "." and last_word.isdigit() == True:
                # add number to list
                new_text = new_text + last_word
            # if the list is over
            elif word.isdigit() == False and last_word == "\n":
                # close list, add current word, declare out of olist
                new_text = new_text + "</ol>" + word
                in_olist = False
            # default case
            else:
                # add word to list text
                new_text = new_text + word

        # not in any list
        else:
            # if current word is ul indicator
            if ((word == "+" or word == "-") and last_word == "\n"):
                # add tags to new string, declare in ul
                new_text = new_text + "<ul><li>"
                in_ulist = True

            # ordered lists
            # if the current word is a digit and the last char was newline
            elif word.isdigit() == True and last_word == "\n":
                # store current word not add in case it isn't ol
                last_word = word
            # if current word is . and last word was number
            elif word == "." and last_word.isdigit() == True:
                # add tags to new string, declare in ol
                new_text = new_text + "<ol><li>"
                in_olist = True
            # if the last word was a digit but it's not an ol
            elif word != "." and last_word.isdigit() == True:
                # add last word and word to new string
                new_text = new_text + word
            # if there are no indicators
            else:
                # add word to new string and change last word
                new_text = new_text + word

        last_word = word

    return new_text
