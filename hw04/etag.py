"""
Does the work for converting <em> and <strong>
NOTE:
Needs () in if/elif statements to compare correctly.
Ignoring too many branches (13/12) to take care of all cases
"""

def the_work(text):
    """
        This function takes in the text from convert()
        then checks each word for em/strong indicators.
        If one is found it removes the character and puts an
        appropriate <em>/<strong>. After, returns the new text to convert().
    """
    new_text = ""           # string for new text
    check_strong = False    # check for second indicator
    has_em = False          # is an <em>
    has_strong = False      # is <strong>
    has_closing = False     # reached the end of tag

    for word in text:

        # if it's not inside a <strong>
        if has_strong == False:
            # if it's not inside an <em>
            if has_em == False:
                # if the last word wasn't an em/strong indicator
                if check_strong == False:
                    # the current word is an em/strong indicator
                    # check for a strong
                    if word == "*" or word == "_":
                        check_strong = True
                    else:
                        # add word to the new string
                        new_text = new_text + word

                # if the last word was an em/strong indicator
                else:
                    # if the current word is another indicator
                    if word == "*" or word == "_":
                        # put in <strong>, declare inside a <strong>
                        # declare not looking for <strong>
                        new_text = new_text + "<strong>"
                        has_strong = True
                        check_strong = False
                    # if the current word isn't another indicator
                    else:
                        # add <em>, add current word (since not indicator)
                        # declare inside <em> not looking for <strong>
                        new_text = new_text + "<em>" + word
                        has_em = True
                        check_strong = False

            # if it has an <em>
            else:
                # if current word is an indicator
                if word == "*" or word == "_":
                    # close <em>, declare not inside <em>
                    new_text = new_text + "</em>"
                    has_em = False
                else:
                    # add current word to the new string
                    new_text = new_text + word

        # if it's inside a <strong>
        else:
            # if the first indicator has passed through to not include second
            # indicator in the new string
            if has_closing == True:
                # close <strong> and declare not inside <strong>
                # no longer in closing indicator
                new_text = new_text + "</strong>"
                has_strong = False
                has_closing = False
            # if it's only the first indicator
            else:
                # if the current word is a closing indicator
                if word == "*" or word == "_":
                    # declare inside closing indicators
                    has_closing = True
                # if the current word isn't a closing indicator
                else:
                    # add word to new string
                    new_text = new_text + word

    return new_text
