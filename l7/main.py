import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def __str__(self):
        return f"Triangle with vertices: {self.point1}, {self.point2}, {self.point3}"

    def calculate_distance(self, point1, point2):
        return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)

    def calculate_area(self):
        side1 = self.calculate_distance(self.point1, self.point2)
        side2 = self.calculate_distance(self.point2, self.point3)
        side3 = self.calculate_distance(self.point3, self.point1)

        semiperimeter = (side1 + side2 + side3) / 2
        area = math.sqrt(semiperimeter * (semiperimeter - side1) * (semiperimeter - side2) * (semiperimeter - side3))

        return area

    def get_sides(self):
        side1 = self.calculate_distance(self.point1, self.point2)
        side2 = self.calculate_distance(self.point2, self.point3)
        side3 = self.calculate_distance(self.point3, self.point1)

        return (side1, side2, side3)


point1 = Point(0, 0)
point2 = Point(4, 0)
point3 = Point(0, 3)

triangle = Triangle(point1, point2, point3)

# Виведення інформації про трикутник
print(triangle)

# Обчислення площі трикутника
print("Area:", triangle.calculate_area())

# Отримання довжин сторін трикутника
print("Sides:", triangle.get_sides())
