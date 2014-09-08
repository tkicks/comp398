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

    new_text = ""
    has_block = False

    for word in text:

        if word == ">":
            new_text = new_text + "<blockquote>"
            has_block = True
        elif word == "\n" and has_block == True:
            new_text = new_text + "</blockquote>" + word
        else:
            new_text = new_text + word

    return new_text
