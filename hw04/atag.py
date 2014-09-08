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

    new_text = ""
    holder_text = ""    # text inside []
    has_link = False    # has [
    has_end = False     # has ]

    for word in text:

        if has_link == True and has_end == False:
            # if there's already been a link indicator
            if word == "]":
                holder_text = holder_text + "</a>"
                has_end = True
            else:
                holder_text = holder_text + word

        elif has_link == True and has_end == True:
            # if it's on to the url
            if word == "(":
                pass
            elif word == ")":
                new_text = new_text + "\">" + holder_text
                has_link = False
                has_end = False
            else:
                # default
                new_text = new_text + word

        else:
            if word == "[":
                new_text = new_text + "<a href=\""
                has_link = True
            else:
                new_text = new_text + word

    return new_text
