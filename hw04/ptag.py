"""
Does the work for converting <p>
"""
def the_work(text):
    """
        This function takes in the text from convert()
        then checks each word for a line break character.
        If one is found it closes the current <p> and starts
        up a new one. After, returns the new text to convert().
    """

    last_word = ""      # hold the last word
    two_words = ""      # hold two words ago
    new_text = "<p>"    # new text string initiated with a <p>

    for word in text:

        if word == "\n" and last_word == " " and two_words == " ":
            # if the last two characters before a newline char were spaces
            # add the new text as well as closing and opening <p>
            new_text = new_text + "</p>" + "<p>" + word
            two_words = last_word
            last_word = word
        else:
            # default
            # add the word to the new_text string
            new_text = new_text + word
            two_words = last_word
            last_word = word

    return new_text
