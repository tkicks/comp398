#!/usr/bin/env python
"""reads data from .txt and turns into a node which is then put into a LL"""
import LinkedList
import scraper


def main():
    """does the work, does not have the classes"""
    scraper.scraper()   # run the scraper

    with open('output.csv', 'r') as csv_file:   #open file until done reading
        lists = LinkedList.LinkedList()

        for row in csv_file:
        # make the nodes from the .csv file and put them into a linked list
            state_text = repr(row.strip())
            lists.new_node(state_text)

    lists.print_list()

    # bools for loops, self-explanatory names
    has_state = False
    still_search = True

    while still_search:
        search_for = raw_input("\nEnter a letter to narrow search "
            "(1: exit, 0: whole list): ")
        print " "

        if search_for == "0":
        # print whole list
            lists.print_list()

        elif search_for == "1":
        # quit
            print "Ending search.\n"
            still_search = False

        else:
        # print only the states beginning with user inputted letter
            current_node = lists.head

            while current_node.next != None:
                # navigate list until the end
                if current_node.cargo[0] == search_for.upper():
                    # if state starts with input, has_state = True
                    print current_node.cargo
                    has_state = True
                current_node = current_node.next

            if has_state == False:
                # if no states are found
                print "No state or territory found."

        has_state = False


if __name__ == "__main__":
    main()
