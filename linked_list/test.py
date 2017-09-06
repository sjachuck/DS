from list_utils import LinkedList
import pdb

def main():
    print "Testing"
    ll = LinkedList('MyList')
    ll.printList()
    ll.createRandomList()
    ll.printList()

    #printNthNode(ll)
    #printMiddleElement(ll)
    printNthNodeFromEnd(ll)

def printNthNodeFromEnd(ll):
    N = input("Enter the reverse-index of element that you want to see: ")
    if N < 1:
        print "Enter a valid index (starting with 1)"
        return

    counter = N
    ptr2 = ll.HEAD

    while ptr2 is not None and counter != 0:
        ptr2 = ptr2.link
        counter -= 1
    if counter != 0:
        print "List is not as long as you expected..."
        return
    ptr1 = ll.HEAD
    while ptr2 is not None:
        ptr2 = ptr2.link
        ptr1 = ptr1.link
    print ptr1.data

def printMiddleElement(ll):
    print "Middle Element is"
    ptr1 = ll.HEAD
    ptr2 = ptr1.link

    while ptr2 is not None:
        ptr1 = ptr1.link
        ptr2 = ptr2.link
        if ptr2 is None:
            break
        else:
            ptr2 = ptr2.link
    print ptr1.data

def printNthNode(ll):
    N = input("Enter the index of element that you want to see: ")
    if N < 1:
        print "Enter a valid index (starting with 1)"
        return
    ptr = ll.HEAD
    count = 1
    while ptr is not None and count < N:
        ptr = ptr.link
        count += 1
    if ptr is None:
        print "Linked List shorter than what you expect"
    else:
        print ptr.data


if __name__ == '__main__':
    main()