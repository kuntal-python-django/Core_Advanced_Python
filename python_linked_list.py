class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.start_node = None
      
    def traverse_list(self):
      if self.start_node is None:
          print("List has no element")
          return
      else:
          n = self.start_node
          while n is not None:
              print(n.item , " ")
              n = n.ref

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node= new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n= n.ref
        n.ref = new_node;

    def insert_after_item(self, x, data):
        n = self.start_node
        print(n.ref)
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List has no element")
            return
        if x == self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return
        n = self.start_node
        print(n.ref)
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_at_index (self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index-1 and n is not None:
            n = n.ref
            i = i+1
        if n is None:
            print("Index out of bound")
        else: 
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def search_item(self, x):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.ref
        print("item not found")
        return False

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        self.start_node = self.start_node.ref

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return

        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    def delete_element_by_value(self, x):
      if self.start_node is None:
          print("The list has no element to delete")
          return 
      if self.start_node.item == x:
          self.start_node = self.start_node.ref
          return
      n = self.start_node
      while n.ref is not None:
          if n.ref.item == x:
              break
          n = n.ref
      if n.ref is None:
          print("item not found in the list")
      else:
          n.ref = n.ref.ref

    def get_count(self):
      if self.start_node is None:
          return 0;
      n = self.start_node
      count = 0;
      while n is not None:
          count = count + 1
          n = n.ref
      return count







################################# Insert At Mid ################################
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None

def insertAtMid(head, x): 
	if(head == None):
		head = Node(x) 
	else: 
		newNode = Node(x) 
		ptr = head 
		length = 0
		while(ptr != None): 
			ptr = ptr.next
			length += 1
		if(length % 2 == 0): 
			count = length / 2
		else: 
			(length + 1) / 2
		ptr = head
		while(count > 1): 
			count -= 1
			ptr = ptr.next
		newNode.next = ptr.next
		ptr.next = newNode 

# function to displat the linked list 
def display(head): 
	temp = head 
	while(temp != None): 
		print(str(temp.data), end = " ")
		temp = temp.next

# Creating the linked list 1.2.4.5 
head = Node(1) 
head.next = Node(2) 
head.next.next = Node(4) 
head.next.next.next = Node(5) 
print("Linked list before insertion: ", end = "") 
display(head) 
# inserting 3 in the middle of the linked list. 
x = 3
insertAtMid(head, x)
print("\nLinked list after insertion: " , end = "") 
display(head)




################################ Find Mid Node #################################
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList: 
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Function to get the middle of  
    def printMiddle(self): 
        slow_ptr = self.head 
        fast_ptr = self.head 
        if self.head is not None: 
            while (fast_ptr is not None and fast_ptr.next is not None): 
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            print("The middle element is: ", slow_ptr.data) 
  
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()



############################### Sorting Linked List ############################
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
    def __init__(self): 
        self.head = None

    def append(self, new_value): 
        new_node = Node(new_value) 
        if self.head is None: 
            self.head = new_node 
            return
        curr_node = self.head 
        while curr_node.next is not None: 
            curr_node = curr_node.next
        curr_node.next = new_node 
          
    def sortedMerge(self, a, b): 
        result = None
        # Base cases 
        if a == None: 
            return b 
        if b == None: 
            return a 
        # pick either a or b and recur.. 
        if a.data <= b.data: 
            result = a 
            result.next = self.sortedMerge(a.next, b) 
        else: 
            result = b 
            result.next = self.sortedMerge(a, b.next) 
        return result 
      
    def mergeSort(self, h): 
        # Base case if head is None 
        if h == None or h.next == None: 
            return h 
        # get the middle of the list  
        middle = self.getMiddle(h) 
        nexttomiddle = middle.next
        # set the next of middle node to None 
        middle.next = None
        # Apply mergeSort on left list  
        left = self.mergeSort(h) 
        # Apply mergeSort on right list 
        right = self.mergeSort(nexttomiddle)
        # Merge the left and right lists  
        sortedlist = self.sortedMerge(left, right) 
        return sortedlist 

    def getMiddle(self, head): 
        if (head == None): 
            return head 
        slow = head 
        fast = head 
        while (fast.next != None and 
               fast.next.next != None): 
            slow = slow.next
            fast = fast.next.next
        return slow

def printList(head): 
    if head is None: 
        print(' ') 
        return
    curr_node = head 
    while curr_node: 
        print(curr_node.data, end=" ")
        curr_node = curr_node.next
    print(' ') 


# Driver Code 
if __name__ == '__main__': 
    li = LinkedList() 
    # Let us create a unsorted linked list 
    # to test the functions created.  
    # The list shall be a: 2->3->20->5->10->15  
    li.append(15) 
    li.append(10) 
    li.append(5) 
    li.append(20) 
    li.append(3) 
    li.append(2) 
    # Apply merge Sort  
    li.head = li.mergeSort(li.head)
    print ("Sorted Linked List is:")
    printList(li.head)






####################################### Add Two Linked List #############################
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
 
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    def addTwoLists(self, first, second):
        prev = None
        temp = None
        carry = 0
 
        while(first is not None or second is not None):
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data
            Sum = carry + fdata + sdata
            carry = 1 if Sum >= 10 else 0
            Sum = Sum if Sum < 10 else Sum % 10
            temp = Node(Sum)
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp
            prev = temp
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next
        if carry > 0:
            temp.next = Node(carry)

    def printList(self):
        temp = self.head
        while(temp):
          print(temp.data)
          temp = temp.next
 
# Driver code
first = LinkedList()
second = LinkedList()
 
# Create first list
first.push(6)
first.push(4)
first.push(9)
first.push(5)
first.push(7)
print("First List is ")
first.printList()
 
# Create second list
second.push(4)
second.push(8)
print("\nSecond List is ")
second.printList()
 
# Add the two lists and see result
res = LinkedList()
res.addTwoLists(first.head, second.head)
print("\nResultant list is ")
res.printList()




#################################### Reversed Linked List ##############################
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
 
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
 
# Driver code
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
print("Given Linked List")
llist.printList()
llist.reverse()
print("\nReversed Linked List")
llist.printList()




############################# Flattening #############################
def flattenning(iList, newList=[]):
    for item in iList:
        if isinstance(item, list):
            flattenning(item, newList)
        else:
            newList.append(item)
    return newList

theList = [1,[3,[5,[8,[10]]],12,['A',['B',['C']]]],14,['a','c']]
print("Given List : ", theList)
lst = flattenning(theList)
print("Converted : ", lst)



######################## Stack by Linked List ##################################
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
class Stack: 
    # Initializing a stack. 
    # Use a dummy node, which is 
    # easier for handling edge cases. 
    def __init__(self):
        self.head = Node("head")
        self.size = 0
 
   # String representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]   
 
    # Get the current size of the stack
    def getSize(self):
        return self.size
    
    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0
        
   # Get the top item of the stack
    def peek(self):
        
        # Sanitary check to see if we 
        # are peeking an empty stack. 
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value
 
    # Push a value into the stack. 
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
      
    # Remove a value from the stack and return. 
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value
 
# Driver Code
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")
    
    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")




############################### Queue by Linked List ###########################
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
# A class to represent a queue 
  
# The queue, front stores the front node 
# of LL and rear stores the last node of LL 
class Queue: 
      
    def __init__(self): 
        self.front = self.rear = None
  
    def isEmpty(self): 
        return self.front == None
      
    # Method to add an item to the queue 
    def EnQueue(self, item): 
        temp = Node(item) 
          
        if self.rear == None: 
            self.front = self.rear = temp 
            return
        self.rear.next = temp 
        self.rear = temp 
  
    # Method to remove an item from queue 
    def DeQueue(self): 
          
        if self.isEmpty(): 
            return
        temp = self.front 
        self.front = temp.next
  
        if(self.front == None): 
            self.rear = None
  
# Driver Code 
if __name__== '__main__': 
    q = Queue() 
    q.EnQueue(10) 
    q.EnQueue(20) 
    q.DeQueue() 
    q.DeQueue() 
    q.EnQueue(30) 
    q.EnQueue(40) 
    q.EnQueue(50)  
    q.DeQueue()    
    print("Queue Front " + str(q.front.data)) 
    print("Queue Rear " + str(q.rear.data)) 



############################# Circular Queue ###################################
class CircularQueue(): 
  
    # constructor 
    def __init__(self, size): # initializing the class 
        self.size = size 
          
        # initializing queue with none 
        self.queue = [None for i in range(size)]  
        self.front = self.rear = -1
  
    def enqueue(self, data): 
          
        # condition if queue is full 
        if ((self.rear + 1) % self.size == self.front):  
            print(" Queue is Full\n") 
              
        # condition for empty queue 
        elif (self.front == -1):  
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data 
        else: 
              
            # next position of rear 
            self.rear = (self.rear + 1) % self.size  
            self.queue[self.rear] = data 
              
    def dequeue(self): 
        if (self.front == -1): # codition for empty queue 
            print ("Queue is Empty\n") 
              
        # condition for only one element 
        elif (self.front == self.rear):  
            temp=self.queue[self.front] 
            self.front = -1
            self.rear = -1
            return temp 
        else: 
            temp = self.queue[self.front] 
            self.front = (self.front + 1) % self.size 
            return temp 
  
    def display(self): 
      
        # condition for empty queue 
        if(self.front == -1):  
            print ("Queue is Empty") 
  
        elif (self.rear >= self.front): 
            print("Elements in the circular queue are:",  
                                              end = " ") 
            for i in range(self.front, self.rear + 1): 
                print(self.queue[i], end = " ") 
            print () 
  
        else: 
            print ("Elements in Circular Queue are:",  
                                           end = " ") 
            for i in range(self.front, self.size): 
                print(self.queue[i], end = " ") 
            for i in range(0, self.rear + 1): 
                print(self.queue[i], end = " ") 
            print () 
  
        if ((self.rear + 1) % self.size == self.front): 
            print("Queue is Full") 
  
# Driver Code 
ob = CircularQueue(5) 
ob.enqueue(14) 
ob.enqueue(22) 
ob.enqueue(13) 
ob.enqueue(-6) 
ob.display() 
print ("Deleted value = ", ob.dequeue()) 
print ("Deleted value = ", ob.dequeue()) 
ob.display() 
ob.enqueue(9) 
ob.enqueue(20) 
ob.enqueue(5) 
ob.display()