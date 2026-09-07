class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        return f"{self.make} {self.model}"

    def __str__(self):
        return f"{self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def describe(self):
        return f"{self.make} {self.model} with {self.doors} doors"


class Motorcycle(Vehicle):
    def __init__(self, make, model, has_sidecar):
        super().__init__(make, model)
        self.has_sidecar = has_sidecar

    def describe(self):
        if self.has_sidecar:
            return f"{self.make} {self.model} with a sidecar"
        else:
            return f"{self.make} {self.model} without a sidecar"


class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size


class Shape2:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclasses must implement area()")


class Triangle(Shape2):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# --- Demonstration ---
if __name__ == "__main__":
    vehicles = [Car("Benz", "Sports", "4"), Motorcycle("BMW", "Royal", True)]
    for v in vehicles:
        print(v.describe())

    c = Car("Toyota", "Corolla", 4)
    print(c)   # uses inherited __str__

    s = Square(4)
    circ = Circle(3)
    print(s.area())
    print(circ.area())

    m = Manager("Sam", 80000, 5)
    m.give_raise(5000)
    print(m.salary)

    t = Triangle("Triangle1", 6, 4)
    print(t.area())