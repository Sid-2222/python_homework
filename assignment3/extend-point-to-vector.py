import math

class Point:
    def __init__(self , x , y):
        self.x = x
        self.y = y
    
    def __eq__(self, value):
        return self.x == value.x and self.y == value.y
    
    def __str__(self):
        return (f"{self.x} , {self.y}")
    
    def euclidian_distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
c1=Point(2,5)
c2=Point(2,5)
c3=Point(5,7)

print(Point.__eq__(c2,c1))
print(Point.__str__(c3))
print( c1.euclidian_distance(c3))

class Vector(Point):
    
    def __str__(self):
        return(f"Sub Class Vector ({self.x} , {self.y}) ")
    
    def __add__(self, other):
        return Vector(self.x + other.x , self.y + other.y)
    
v1=Vector(4,5)
v2=Vector(6,4)
print(Vector.__str__(v1))
print(Vector.__str__(v2))
print(Vector.__add__(v1,v2))