#!/usr/bin/env python
"""reads data from .txt and turns into a node which is then put into a LL"""
import LinkedList
import scraper


def main():
    """
    Demonstrates capabilities of linkedlist class
    """

    scraper.scraper()

    # make the nodes from the .csv file and put them into a linked list
    with open('output.csv', 'r') as csv_file:   
        lists = LinkedList.LinkedList()

        for row in csv_file:
            state_text = repr(row.strip())
            lists.new_node(state_text)

    lists.print_list()

    # searches for list values with matching first letter
    has_state = False
    still_search = True

    while still_search:
        search_for = raw_input("\nEnter a letter to narrow search "
            "(1: exit, 0: whole list): ")
        print " "

        if search_for == "0":
            lists.print_list()

        elif search_for == "1":
            print "Ending search.\n"
            still_search = False

        else:
        # print only the states beginning with user inputted letter
            current_node = lists.head

            while current_node.next != None:
                if current_node.cargo[0] == search_for.upper():
                    print current_node.cargo
                    has_state = True
                current_node = current_node.next

            if has_state == False:
                print "No state or territory found."

        has_state = False


if __name__ == "__main__":
    main()
