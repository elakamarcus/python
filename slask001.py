#!/usr/bin/python

class Shape:
    # basic shape = dot
    def __init__(self, x):
        self.x = x
        

class Square(Shape):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def shapeinfo(self):
        print("|-------------|")
        print(f'|x = {self.x} ------|')
        print(f'|y = {self.y} -------|')
        print("|-------------|")
        print(f'|A = {self.x * self.y} ------|')
        print(f'|C = {self.x*2 + self.y*2} ------|')
        print("|-------------|")

def main():
    square = Square(10, 5)
    square.shapeinfo()

if __name__ == "__main__":
    main()