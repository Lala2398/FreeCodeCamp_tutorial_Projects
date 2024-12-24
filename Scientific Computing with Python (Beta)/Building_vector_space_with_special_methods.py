class R2Vector:
    def __init__(self, *, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return sum(val**2 for val in vars(self).values())**0.5

    def __str__(self):
        return str(tuple(getattr(self, i) for i in vars(self)))

    def __repr__(self):
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'

    def __add__(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __sub__(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __mul__(self, other):
        if type(other) in (int, float):
            kwargs = {i: getattr(self, i) * other for i in vars(self)}
            return self.__class__(**kwargs)        
        elif type(self) == type(other):
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]
            return sum(args)            
        return NotImplemented

    def __eq__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return all(getattr(self, i) == getattr(other, i) for i in vars(self))
        
    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.norm() < other.norm()

    def __gt__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()

    def __le__(self, other):
        return not self > other

    def __ge__(self, other):
        return not self < other

class R3Vector(R2Vector):
    def __init__(self, *, x, y, z):
        super().__init__(x=x, y=y)
        self.z = z
        
    def cross(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {
            'x': self.y * other.z - self.z * other.y,
            'y': self.z * other.x - self.x * other.z,
            'z': self.x * other.y - self.y * other.x
        }
        
        return self.__class__(**kwargs)
v1 = R3Vector(x=2, y=3, z=1)
v2 = R3Vector(x=0.5, y=1.25, z=2)
print(f'v1 = {v1}')
print(f'v2 = {v2}')
v3 = v1 + v2
print(f'v1 + v2 = {v3}')
v4 = v1 - v2
print(f'v1 - v2 = {v4}')
v5 = v1 * v2
print(f'v1 * v2 = {v5}')
v6 = v1.cross(v2)
print(f'v1 x v2 = {v6}')

'''
A vector space is a fundamental concept in mathematics and linear algebra. 
It consists of vectors that can be added together and multiplied by scalars. 
Python can be used to create and manipulate vector spaces, particularly with libraries like NumPy or through custom classes.

__init__ :  Initializes the object with specified attributes. Sets the x, y (and z for R3Vector) values during object creation.
__str__  : Returns a user-friendly string representation of the object. Displays the vector as a tuple, e.g., (x, y) or (x, y, z).
__repr__ : Returns a developer-friendly string representation of the object. Displays the class name and attributes in a constructor-like format.
__add__  : Defines the behavior of the + operator.Adds corresponding components of two vectors.
__sub__  : Defines the behavior of the - operator.Subtracts corresponding components of two vectors.
__mul__  : Defines the behavior of the * operator. Performs scalar multiplication if other is a number, or dot product if other 
__eq__   :  Defines the behavior of the == operator.Compares vectors for equality based on their components.
__ne__   :  Defines the behavior of the != operator. Compares vectors for inequality.
__lt__   : Defines the behavior of the < operator. Compares the norms of two vectors.
__gt__   : Defines the behavior of the > operator. Compares the norms of two vectors.
__le__   : Defines the behavior of the <= operator.Compares the norms of two vectors for less-than-or-equal.
__ge__   : Defines the behavior of the >= operator. Compares the norms of two vectors for greater-than-or-equal.
cross (Not a Special Method, but Important in R3Vector) : Computes the cross product of two 3D vectors. Calculates a new vector orthogonal to the two input vectors. '''

