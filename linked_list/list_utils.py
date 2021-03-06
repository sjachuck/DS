import random

MAX_ELEMENTS = 10
MIN_ELEMENTS = 2
NAME_Counter = 1

class Node:
    def __init__(self):
        self.data = 0
        self.link = None

    def __init__(self, data):
        self.data = data
        self.link = None

    def setData(self, data):
        self.data = data

    def setLink(self, node):
        self.link = node

class LinkedList:
    def __init__(self, name='NO NAME'):
        self.name = name
        self.HEAD = None
        self.TAIL = None
        self.LEN = 0

    def printList(self):
        print "Contents of %s" % self.name
        elements = self.convertListToArray()
        elements.append('NULL')
        print ' --> '.join(elements)

    def convertListToArray(self):
        node = self.HEAD
        elements = []
        while node is not None:
            elements.append(str(node.data))
            node = node.link
        return elements

    def createRandomList(self, sorted=False):
        response = 'y'
        if self.HEAD is not None:
            print "List is not empty. Creating a random list will delete all the contents."
            response = input("Do you want to proceed? (y/n) ")
        if response == 'n' or response == 'N':
            print "No new list created. Existing List is intact"
            return
        N = random.randint(MIN_ELEMENTS, MAX_ELEMENTS)
        for i in range(N):
            self.push(random.randint(1, 100))
        if sorted is True:
            self.sort()

    def length(self):
        count = 0
        if self.HEAD is None:
            return 0
        ptr = self.HEAD
        while ptr is not None:
            count += 1
            ptr = ptr.link
        return count

    def sort(self):
        # Using bubble sort
        n = self.length()
        if n < 2:
            return
        head = self.HEAD

        for i in range(n):
            ptr1 = head
            ptr2 = head.link
            for j in range(n-i-1):
                if ptr1.data > ptr2.data:
                    tmp = ptr1.data
                    ptr1.data = ptr2.data
                    ptr2.data = tmp
                ptr1 = ptr1.link
                ptr2 =  ptr2.link

    def push(self, data):
        new_node = Node(data)
        if self.HEAD == None:
            self.HEAD = new_node
            self.TAIL = new_node
        else:
            new_node.link = self.HEAD
            self.HEAD = new_node
        self.LEN += 1

    def pop(self):
        if self.HEAD is None:
            self.TAIL = None
            return None
        node = self.HEAD
        self.HEAD = self.HEAD.link
        self.LEN -= 1
        return node.data

    def insert(self, data):
        new_node = Node(data)
        if self.HEAD == None:
            self.HEAD = new_node
            self.TAIL = new_node
        else:
            self.TAIL.link = new_node
            self.TAIL = new_node
        self.LEN += 1

    def delete(self):
        self.pop()

    def deleteNthNode(self, N):
        if self.HEAD is None:
            return
        prev = None
        curr = self.HEAD
        count = 1
        while curr is not None and count != N :
            prev = curr
            curr = curr.link
        if count == N:
            prev.link = curr.link
            curr = None
        else:
            print "# Cannot delete. Length specified is longer than the linked list."
        self.LEN -= 1

    def deleteListRecursion(self, head):
        if head is None:
            return
        self.deleteListRecursion(head.link)
        next_node = head.link
        head.link = None
        if next_node is not None:
            del next_node


    def deleteList(self):
        print "\nDeleting List now...\n"
        self.deleteListRecursion(self.HEAD)
        old_head = self.HEAD
        self.HEAD = None
        del old_head
        self.TAIL = None


