#1. Complex Number Class

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Example
c1 = Complex(3, 4)
c2 = Complex(1, 2)
print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)


#2. Matrix Class (3x3)

class Matrix:
    def __init__(self, data):
        self.data = data

    def add(self, other):
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(3)] for i in range(3)])

    def multiply(self, other):
        return Matrix([[sum(self.data[i][k] * other.data[k][j] for k in range(3)) for j in range(3)] for i in range(3)])

    def transpose(self):
        return Matrix([[self.data[j][i] for j in range(3)] for i in range(3)])

    def display(self):
        for row in self.data:
            print(row)

# Example
m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("Addition:")
m1.add(m2).display()
print("Multiplication:")
m1.multiply(m2).display()
print("Transpose of m1:")
m1.transpose().display()


#3. Solid Class (Surface Area & Volume)

class Solid:
    def __init__(self, shape, dimension):
        self.shape = shape
        self.dimension = dimension

    def surface_area(self):
        if self.shape == "cube":
            return 6 * self.dimension ** 2
        elif self.shape == "sphere":
            return 4 * 3.1416 * self.dimension ** 2
        return None

    def volume(self):
        if self.shape == "cube":
            return self.dimension ** 3
        elif self.shape == "sphere":
            return (4/3) * 3.1416 * self.dimension ** 3
        return None

# Example
s = Solid("sphere", 5)
print("Surface Area:", s.surface_area())
print("Volume:", s.volume())


#4. Regular Shape (Area & Perimeter)

class Shape:
    def __init__(self, shape, dimension):
        self.shape = shape
        self.dimension = dimension

    def area(self):
        if self.shape == "square":
            return self.dimension ** 2
        elif self.shape == "circle":
            return 3.1416 * self.dimension ** 2
        return None

    def perimeter(self):
        if self.shape == "square":
            return 4 * self.dimension
        elif self.shape == "circle":
            return 2 * 3.1416 * self.dimension
        return None

# Example
shape = Shape("square", 4)
print("Area:", shape.area())
print("Perimeter:", shape.perimeter())


#5. Time Class

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def add(self, other):
        total_seconds = self.seconds + other.seconds
        total_minutes = self.minutes + other.minutes + total_seconds // 60
        total_hours = self.hours + other.hours + total_minutes // 60

        return Time(total_hours % 24, total_minutes % 60, total_seconds % 60)

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

# Example
t1 = Time(10, 45, 50)
t2 = Time(5, 30, 20)
t3 = t1.add(t2)
print("Time after addition:", t3)



#6. Date Class with Overloaded ==

class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]

    def __eq__(self, other):
        return self.date == other.date

# Example
d1 = Date(24, 4, 2025)
d2 = Date(24, 4, 2025)
print("Dates are equal:", d1 == d2)


#7. Weather Class with Overloaded in

class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters

# Example
weather = Weather(["rain", "sunny", "windy"])
print("rain" in weather)  # True
print("snow" in weather)  # False


#8. String Class with Custom Methods

class MyString:
    def __init__(self, text):
        self.text = text

    def __iadd__(self, other):
        self.text += other
        return self

    def toLower(self):
        return self.text.lower()

    def toUpper(self):
        return self.text.upper()

# Example
s = MyString("Hello")
s += " World"
print("Concatenated:", s.text)
print("Lowercase:", s.toLower())
print("Uppercase:", s.toUpper() )
