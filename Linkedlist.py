class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def add_at_beg(self,data):
        if self.head ==None:
            self.head=Node(data)
        else:
            nn=Node(data)
            nn.next=self.head
            self.head=nn
    def print(self):
        i=self.head
        elements=[]
        while i:
            elements.append(str(i.data))
            i=i.next
        if elements:
            return ' --> '.join(elements)
        else:
            return None
    def add_at_end(self,data):
        i=self.head
        if self.head==None:
            self.head=Node(data)
            return
        while i.next:
            i=i.next
        i.next=Node(data)
    def count_elements(self):
        i=self.head
        c=0
        while i:
            c+=1
            i=i.next
        return c
    def add_at_index(self,data,index):
        count=0
        if index>self.count_elements() or index<0:
            raise Exception('Out of Index')
        if index==0:
            nn=Node(data)
            nn.next=self.head
            self.head=nn
        else:
            i=self.head
            while i:
                if count==index-1:
                    nn=Node(data)
                    nn.next=i.next
                    i.next=nn
                    break
                i=i.next
                count+=1
    def delete_at_beg(self):
        if self.count_elements()==1:
            self.head=None
        if self.head:
            self.head=self.head.next
        else:
            print('No elements to delete')
    def delete_at_end(self):
        if self.count_elements()==1:
            self.head=None
        if self.head:
            i=self.head
            while i.next.next:
                i=i.next
            i.next=None
        else:
            print('No elements to delete')
    def delete_at_index(self, index):
        if index < 0 or index >= self.count_elements():
            raise Exception('Not a valid Index')
        if self.count_elements() == 1:
            self.head = None
        elif self.head:
            if index == 0:
                self.head = self.head.next
            else:
                i = self.head
                c = 0
                while i and c < index - 1:
                    i = i.next
                    c += 1
                if i and i.next:
                    i.next = i.next.next
        else:
            print('No elements to delete')

# a=LinkedList()
# a.add_at_beg(14)
# a.add_at_beg(25)
# print(a.count_elements())
# print(a.print())
# a.add_at_end(7)
# a.add_at_index(23,2)
# a.add_at_end(10)
# a.delete_at_beg()
# a.delete_at_end()
# a.delete_at_index(1)
# print(a.count_elements())
# print(a.print())

if __name__=='__main__':
    a=LinkedList()
    while True:
        choice = int(input("Enter your choice: "))
    
        if choice == 1:
            a.add_at_beg(input('Enter value: '))
        elif choice == 2:
            a.add_at_end(input('Enter value: '))
        elif choice == 3:
            data, index = input('Enter value and index: ').split()
            a.add_at_index(int(data), int(index))
        elif choice == 4:
            a.delete_at_beg()
        elif choice == 5:
            a.delete_at_end()
        elif choice == 6:
            index = int(input('Enter index to delete: '))
            a.delete_at_index(index)
        elif choice == 7:
            a.count_elements()
        elif choice == 8:
            print(a.print())
        elif choice ==9:
            break
        else:
            print("Invalid choice. Please enter a valid option.")
            
            
