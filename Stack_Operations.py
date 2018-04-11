class Stack():
  
  def __init__(self):
    self.items = []
    
  def push(self, item):
    return self.items.append(item)
  
  def pop(self):
    return self.items.pop()
  
  def getElements(self):
    return self.items

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
print stack.getElements()

  
