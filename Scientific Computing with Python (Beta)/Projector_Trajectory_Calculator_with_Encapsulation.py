import math

GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"

class Projectile:
    __slots__ = ('__speed', '__height', '__angle')

    def __init__(self, speed, height, angle):
        self.__speed = speed
        self.__height = height
        self.__angle = math.radians(angle)
        
    def __str__(self):
        return f'''
Projectile details:
speed: {self.speed} m/s
height: {self.height} m
angle: {self.angle}°
displacement: {round(self.__calculate_displacement(), 1)} m
'''

    def __calculate_displacement(self):
        horizontal_component = self.__speed * math.cos(self.__angle)
        vertical_component = self.__speed * math.sin(self.__angle)
        squared_component = vertical_component**2
        gh_component = 2 * GRAVITATIONAL_ACCELERATION * self.__height
        sqrt_component = math.sqrt(squared_component + gh_component)
        
        return horizontal_component * (vertical_component + sqrt_component) / GRAVITATIONAL_ACCELERATION
        
    def __calculate_y_coordinate(self, x):
        height_component = self.__height
        angle_component = math.tan(self.__angle) * x
        acceleration_component = GRAVITATIONAL_ACCELERATION * x ** 2 / (
                2 * self.__speed ** 2 * math.cos(self.__angle) ** 2)
        y_coordinate = height_component + angle_component - acceleration_component

        return y_coordinate
    
    def calculate_all_coordinates(self):
        return [
            (x, self.__calculate_y_coordinate(x))
            for x in range(math.ceil(self.__calculate_displacement()))
        ]

    @property
    def height(self):
        return self.__height

    @property
    def angle(self):
        return round(math.degrees(self.__angle))

    @property
    def speed(self):
        return self.__speed

    @height.setter
    def height(self, n):
        self.__height = n

    @angle.setter
    def angle(self, n):
        self.__angle = math.radians(n)

    @speed.setter
    def speed(self, s):
       self.__speed = s
    
    def __repr__(self):
        return f'{self.__class__}({self.speed}, {self.height}, {self.angle})'

class Graph:
    __slots__ = ('__coordinates')

    def __init__(self, coord):
        self.__coordinates = coord

    def __repr__(self):
        return f"Graph({self.__coordinates})"

    def create_coordinates_table(self):
        table = '\n  x      y\n'
        for x, y in self.__coordinates:
            table += f'{x:>3}{y:>7.2f}\n'

        return table

    def create_trajectory(self):

        rounded_coords = [(round(x), round(y)) for x, y in self.__coordinates]

        x_max = max(rounded_coords, key=lambda i: i[0])[0]
        y_max = max(rounded_coords, key=lambda j: j[1])[1]

        matrix_list = [[" " for _ in range(x_max + 1)] for _ in range(y_max + 1)]

        for x, y in rounded_coords:
            matrix_list[-1 - y][x] = PROJECTILE

        matrix = ["".join(line) for line in matrix_list]

        matrix_axes = [y_axis_tick + row for row in matrix]
        matrix_axes.append(" " + x_axis_tick * (len(matrix[0])))

        graph = "\n" + "\n".join(matrix_axes) + "\n"

        return graph

def projectile_helper(speed, height, angle):
    projectile = Projectile(speed, height, angle)

    print(projectile)

    coordinates = projectile.calculate_all_coordinates()

    graph = Graph(coordinates)
    print(graph.create_coordinates_table())
    print(graph.create_trajectory())

projectile_helper(10, 3, 45)



'''
This project is a Projectile Trajectory Calculator that simulates the motion of a projectile based on given speed, height, and angle values. 
It calculates the projectile's details, generates a coordinate table, and visualizes its trajectory. 
The project uses mathematical modeling of horizontal and vertical motion based on physics principles.
Encapsulation in Python is the principle of hiding a class's data and methods from the outside world and providing controlled access. 

In this project, encapsulation is applied as follows:

- Private Attributes:
        = Attributes like __speed, __height, and __angle are defined with __ (double underscore) to prevent direct access from outside the class.
        = Controlled access to these attributes is provided through getter and setter methods (e.g., @property and @height.setter).

- Private Methods:
       = Methods like __calculate_displacement() and __calculate_y_coordinate(x) are marked private to restrict their usage within the class. 
          This keeps the internal logic hidden from external interference.
          
-  Use of __slots__:
        =The __slots__ mechanism limits the attributes a class can have, optimizing memory usage and maintaining data integrity. It is used in both Projectile and Graph classes.

Encapsulation in this project:
-Prevented improper access and manipulation of data.
-Made the classes more reliable and reusable.
-Optimized memory usage with __slots__.'''
