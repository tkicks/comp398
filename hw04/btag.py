"""
Does the work for converting <blockquote>
"""
def the_work(text):
    """
        This function takes in the text from convert()
        then checks each word for block quote indicators.
        If one is found it removes the character and puts a
        <blockquote>. After, returns the new text to convert().
    """

    new_text = ""       # string for new text
    last_word = ""      # the last word checked
    has_block = False   # is inside a blockquote?

    for word in text:

        if word == ">" and last_word == " ":
            # if bq initiator and the last word was a space
            # add a <bq> and declare being in bq
            new_text = new_text + "<blockquote>"
            has_block = True
            last_word = word
        elif word == "\n" and has_block == True:
            # catch an ending bq at the newline char
            # declare being out of bq after closing
            new_text = new_text + "</blockquote>" + word
            has_block = False
            last_word = word
        else:
            # default
            # add word to new text
            new_text = new_text + word
            last_word = word

    return new_text
