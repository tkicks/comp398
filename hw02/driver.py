#!/usr/bin/env python
"""reads data from .txt and turns into a node which is then put into a LL"""
import LinkedList
import scraper


def main():
    """does the work, does not have the classes"""
    # make the nodes from the .csv file and put them into a linked list
    scraper.scraper()
    with open('output.csv', 'r') as csv_file:
        lists = LinkedList.LinkedList()
        for row in csv_file:
            disease_text = repr(row.strip())
            lists.new_node(disease_text)

    # print the list to the console
    #(currently prints in reverse order of addition to the list)
    current_node = lists.head
    while current_node.next != None:
        print current_node.cargo
        current_node = current_node.next

    # print only the diseases beginning with user inputted letter
    has_state = False
    search_for = raw_input("\nEnter a letter to narrow search (A-G): ")
    print " "
    current_node = lists.head
    while current_node.next != None:
        if current_node.cargo[1] == search_for.upper():
            print current_node.cargo
            has_state = True
        current_node = current_node.next
    if has_state == False:
        print "List not extensive enough, no state or territory found."
    print " "

if __name__ == "__main__":
    main()
