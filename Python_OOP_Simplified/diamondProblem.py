'''
               class A
                ^    ^
               /      \
           class B    class C
              ^        ^           
              \       /
               class D
'''

class A:
    def method(self):
        print("This is class A")


class B(A):
    def method(self):
        print("This is class B")



class C(A):
    def method(self):
        print("This is class C")

# To use the overridden methon in class B, first inherit from B 
# To order is important. This is called 'method resolution order'.
class D(B,C):
    pass
    
    

d = D()
d.method()
