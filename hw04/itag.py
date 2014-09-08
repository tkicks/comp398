"""
Does the work for converting <img>
"""
def the_work(text):
    """
        This function takes in the text from convert()
        then checks each word for image indicators.
        If one is found it removes the character and puts a
        <img>. After, returns the new text to convert().
    """

    new_text = ""       # string holding text with changes made to it
    holder_text = ""    # text inside [alt text]
    has_image = False   # has [
    has_end = False     # has ]

    for word in text:

        if has_image == True and has_end == False:
            # if there's already been an image indicator
            if word == "[":
                # pass on the alt text opening bracket
                pass
            elif word == "]":
                # close the alt text
                holder_text = holder_text + " />"
                has_end = True
            else:
                # default
                # add the word to the alt text holder string
                holder_text = holder_text + word

        elif has_image == True and has_end == True:
            # if the path is next
            if word == "(":
                # pass on the path (
                pass
            elif word == ")":
                # close the path text and add the alt text to the tag
                new_text = new_text + "\"" + " alt=\""  + holder_text + "\" />"
                holder_text = ""
                has_image = False
                has_end = False
            else:
                # default
                # put the word into the new_text variable
                new_text = new_text + word

        else:
            # default
            if word == "!":
                # if there's an image indicator begin <img>
                # has_image = True to take alt and path strings
                new_text = new_text + "<img src=\""
                has_image = True
            else:
                # default
                # add the word to the new text string
                new_text = new_text + word

    return new_text
