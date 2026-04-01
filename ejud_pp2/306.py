class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def answer(self):
            return self.length*self.width
l=int(input())
w=int(input())
rectangle=Rectangle(l,w)
print(rectangle.answer())