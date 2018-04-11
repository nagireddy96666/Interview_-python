class Stack(list):
    ''' define the stack class '''
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, items):
        self.items.append(items)
    def pop(self):
        if not self .isEmpty():
            return self.items.pop()
        else:
            raise Exception('Stack is empty!')
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def main(self):
        stack=Stack() 
        stack.push(1)
        stack.push(2)
        stack.push(3)
        print(stack.size())
        print(stack.peek())
        print(stack.pop())
        print(stack.peek())
if __name__ == '__main__':
    x=Stack()
    x.main()
'''
stack is an ordered list in which items may be added or removed only at the end,
called the top of the stack.
the last item to be added to a stock is the first item to be removed.accordingly
stack are also called last in first out(LIFO) or first in last out(FILO)
'''

