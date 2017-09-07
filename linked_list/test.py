from list_utils import LinkedList
import pdb

def main():
    print "Testing"
    lla = LinkedList('List-A')
    lla.createRandomList(sorted=True)
    lla.printList()
    print ""
    llb = LinkedList('List-B')
    llb.createRandomList(sorted=True)
    llb.printList()
    print ""
    llc = mergeTwoLists(lla, llb)
    llc.printList()

    #printNthNode(ll)
    #printMiddleElement(ll)
    #printNthNodeFromEnd(ll)
    #print ll.length()
    #ll.sort()
    #ll.HEAD = reverseList(ll.HEAD)

def mergeTwoLists(a, b):
    c = LinkedList('List-C')
    ptr1 = a.HEAD
    ptr2 = b.HEAD
    while ptr1 is not None and ptr2 is not None:
        if ptr1.data <= ptr2.data:
            c.insert(ptr1.data)
            ptr1 = ptr1.link
        else:
            c.insert(ptr2.data)
            ptr2 = ptr2.link
    while ptr1 is not None:
        c.insert(ptr1.data)
        ptr1 = ptr1.link
    while ptr2 is not None:
        c.insert(ptr2.data)
        ptr2 = ptr2.link
    return c

def reverseList(head):
    if head is None:
        return None
    new_head = reverseList(head.link)
    next_node = head.link
    if next_node is not None:
        next_node.link = head
    head.link = None
    if new_head is not None:
        return new_head
    else:
        return head

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