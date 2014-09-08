"""
Does the work for converting <code>
"""
def the_work(text):
    """
        This function takes in the text from convert()
        then checks each word for code indicators.
        If one is found it removes the character and puts a
        <code>. After, returns the new text to convert().
    """

    new_text = ""       # string holding text with changes made to it
    has_code = False    # has ` without a closing `

    for word in text:

        if has_code == True:
            # if there's already been a code indicator
            if word == "`":
                new_text = new_text + "</code>"
                has_code = False
            else:
                # default
                # add the word to the new text string
                new_text = new_text + word

        else:
            # default
            if word == "`":
                # if there's a code indicator begin <code>
                # indicate that there needs to be a </code>
                new_text = new_text + "<code>"
                has_code = True
            else:
                # default
                # add the word to the new text string
                new_text = new_text + word

    return new_text
