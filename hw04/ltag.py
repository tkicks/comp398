"""
Does the work for converting <li>.
"""
# def the_work(text):
#     """
#         This function takes in the text from convert
#         then checks each word for a + or - character.
#         If one is found it removes the character and either initiates
#         or closes a list.
#         After, returns the new text to getFile().
#     """

#     new_text = ""
#     # check to see if the list is over at each newline
#     last_word = ""
#     in_ulist = False
#     # in_olist = False
#     for word in text:

#         if in_ulist == True:
#             if ((word == "+" or word == "-") and last_word == "\n"):
#                 new_text = new_text + "<li>"
#                 last_word = word
#             # needs () to compare correctly
#             elif ((word != "+" or word != "-") and last_word == "\n"):
#                 new_text = new_text + "</ul>" + word
#                 in_ulist = False
#                 last_word = word
#             else:
#                 new_text = new_text + word
#                 last_word = word

#         else:
#             if ((word == "+" or word == "-") and last_word == "\n"):
#                 new_text = new_text + "<ul><li>"
#                 in_ulist = True
#                 last_word = word
#             else:
#                 new_text = new_text + word
#                 last_word = word

#     return new_text




def the_work(text):
    """
        This function takes in the text from convert
        then checks each word for a + or - character.
        If one is found it removes the character and either initiates
        or closes a list.
        After, returns the new text to convert().

        NOTE: Does not support * indicators or nested lists
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
                # add tag to new string and change last word
                new_text = new_text + "<li>"
                last_word = word
            # if the current word is not an indicator and last word was newline
            elif ((word != "+" or word != "-") and last_word == "\n"):
                # add ul close and current word to new string (not indicator)
                # declare not in ul and change last word
                new_text = new_text + "</ul>" + word
                in_ulist = False
                last_word = word
            # if word is list text
            else:
                # add word to new list and change last word
                new_text = new_text + word
                last_word = word

        # if it's inside an ol
        elif in_olist == True:
            # check if list continues
            if word == "." and last_word.isdigit() == True:
                # add list tag and change last word
                new_text = new_text + "<li>"
                last_word = word
            # if last word was a number and current word isn't indicator
            # case: it's part of the list
            elif word != "." and last_word.isdigit() == True:
                # add number to list
                new_text = new_text + last_word
                last_word = word
            # if the list is over
            elif word.isdigit() == False and last_word == "\n":
                # close list, add current word, declare out of olist
                # change last word
                new_text = new_text + "</ol>" + word
                in_olist = False
                last_word = word
            # default case
            else:
                # add word to list text and change last word
                new_text = new_text + word
                last_word = word

        # not in any list
        else:
            # if current word is ul indicator
            if ((word == "+" or word == "-") and last_word == "\n"):
                # add tags to new string, declare in ul and change last word
                new_text = new_text + "<ul><li>"
                in_ulist = True
                last_word = word
            # if the current word is a digit and the last char was newline
            elif word.isdigit() == True and last_word == "\n":
                # store current word not add in case it isn't ol
                # change last word
                last_word = word
            # if current word is . and last word was number
            elif word == "." and last_word.isdigit() == True:
                # add tags to new string, declare in ol and change last word
                new_text = new_text + "<ol><li>"
                in_olist = True
                last_word = word
            # if the last word was a digit but it's not an ol
            elif word != "." and last_word.isdigit() == True:
                # add last word and word to new string
                # change last word
                new_text = new_text + last_word + word
                last_word = word
            # if there are no indicators
            else:
                # add word to new string and change last word
                new_text = new_text + word
                last_word = word

    return new_text