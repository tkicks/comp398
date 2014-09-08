"""
Does the work for converting <a href>
"""
def the_work(text):
    """
        This function takes in the text from convert()
        then checks each word for link indicators.
        If one is found it removes the character and puts a
        <a href>. After, returns the new text to convert().
    """

    new_text = ""       # string for new text
    holder_text = ""    # text inside [url]
    has_link = False    # has [
    has_end = False     # has ]

    for word in text:

        if has_link == True and has_end == False:
            # if there's already been a link indicator
            if word == "]":
                # if it's closing the shown text
                # add closing <a> to holder_text and declare end
                holder_text = holder_text + "</a>"
                has_end = True
            else:
                # default
                # add word to hodler string
                holder_text = holder_text + word

        elif has_link == True and has_end == True:
            # if it's on to the url
            if word == "(":
                # remove the (
                pass
            elif word == ")":
                # if word is closing url close <a and add the url (holder_text)
                # reset the holder text to empty
                new_text = new_text + "\">" + holder_text
                holder_text = ""
                has_link = False
                has_end = False
            else:
                # default
                # add word to new string
                new_text = new_text + word

        else:
            # default
            if word == "[":
                # if it's a link initiator open <a>
                # declare looking for a link
                new_text = new_text + "<a href=\""
                has_link = True
            else:
                # default
                # add word to new string
                new_text = new_text + word

    return new_text
