class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self, other):
        return Book(self.pages+other.pages)

    def __str__(self):
        return str(self.pages)

obj=Book(1000)
obj1=Book(2000)
obj2=Book(1500)
obj3=Book(500)

print(obj+obj1+obj2+obj3)