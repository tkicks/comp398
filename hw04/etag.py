"""
Does the work for converting <em>
NOTE:
Needs () in if/elif statements to compare correctly.
"""
def the_work(text):
    """
    This function replaces asterisks and underlines with <em>.
    Does not currently support <strong>
    """

    new_text = ""
    has_em = False

    for word in text:

        if ((word == "*"  or word == "_") and has_em == False):
            new_text = new_text + "<em>"
            has_em = True
        elif ((word == "*" or word == "_") and has_em == True):
            new_text = new_text + "</em>"
            has_em = False
        else:
            new_text = new_text + word

    return new_text


"""
# attempt to check for strong
def theWork(text):
    new_text = ""
    last_word = ""
    has_em = False
    # see if it's the first instance of an indicator (last_word != indicator)
    check_em = False
    has_strong = False

    for word in text:

        if ((word == "*" or word == "_") and (last_word != "*" or last_word != "_") and has_em == False and has_strong == False and check_em == True):
            new_text = new_text + "<em>"
            check_em = False
            has_em = True

        # these two are coupled to stop mistaking of strong for em
        # elif word == "*" or word == "_" and last_word != "*" or last_word != "_" and has_em == False and check_em == False:
        #   check_em = True
        # elif word != "*" or word != "_" and last_word == "*" or last_word == "_" and has_em == False and check_em == True:
        #   check_em = False
        #   has_em = True
        #   new_text = new_text + "<em>"

        elif word == "*" or word == "_" and has_em == True:
            new_text = new_text + "</em>"
            has_em = False
        elif last_word == "*" or last_word == "_" and word == "*" or word == "_" and has_strong == False:
            new_text = new_text + "<strong>"
            has_strong = True
        elif last_word == "*" or last_word == "_" and word == "*" or word == "_" and has_strong == True:
            new_text = new_text + "</strong>"
            has_strong = False
        else:
            new_text = new_text + word

        last_word = word

    return new_text
"""
