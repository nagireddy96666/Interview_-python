class Parent:        # define parent class
   def myMethod(self):
      print 'Calling parent method'

class Child(Parent): # define child class
   def myMethod(self):
      print 'Calling child method'

c = Child()
c1 = Parent()# instance of child
c.myMethod()
c1.myMethod()# child calls overridden method
