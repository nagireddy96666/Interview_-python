#linked list
class node(object):
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next
l=node("a",node("b",node("c",node("d"))))
print l.next.next.value
