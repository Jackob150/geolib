import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x} , {self.y})"

    def get_dist_from_point(self, point):
        if isinstance(point, self.__class__):
            return math.sqrt((self.x - point.x) * (self.x - point.x) + (self.y - point.y) * (self.y - point.y))
        return None

    def get_dist_from_line(self, line):
        if isinstance(point, Line):
            return abs(line.A * self.x + line.B * self.y + line.C) / math.sqrt(line.A * line.A + line.B * line.B)
        return None

    def move_by_vector(self, vec):
        self.x += vec.x
        self.y += vec.y

class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __bool__(self):
        return bool(self.x + self.y)

    def __str__(self):
        return f"[{self.x} , {self.y}]"

    @classmethod
    def two_points_vector(cls, point_a: Point, point_b: Point):
        return cls(point_b.x - point_a.x, point_b.y - point_a.y)

    @classmethod
    def line_segment_vector(cls, ls):
        if isinstance(ls, LineSegment):
            return cls(ls.point_b.x - ls.point_a.x, ls.point_b.y - ls.point_a.y)
        return None

    def get_length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
    
    def normalize(self):
        if length := self.get_length():
            self.x /= length
            self.y /= length

    def get_normalized(self):
        return self.__class__(self.x / self.get_length(), self.y / self.get_length())

    def move_point(self, point: Point):
        return Point(point.x + self.x, point.y + self.y)

    def get_vector_sum(self, vec):
        if isinstance(vec, self.__class__):
            return self.__class__(self.x + vec.x, self.y + vec.y)
        return None
    
    def add_vector(self, vec):
        if isinstance(vec, self.__class__):
            self.x += vec.x
            self.y += vec.y

    def get_vector_diff(self, vec):
        if isinstance(vec, self.__class__):
            return self.__class__(self.x - vec.x, self.y - vec.y)
        return None

    def subtract_vector(self, vec):
        if isinstance(vec, self.__class__):
            self.x -= vec.x
            self.y -= vec.y

    def get_scaled_vector(self, k: float):
        return self.__class__(self.x * k, self.y * k)
    
    def scale_vector(self, k: float):
        self.x *= k
        self.y *= k

    def get_scalar_product(self, obj):
        if isinstance(obj, self.__class__) or isinstance(obj, Point):
            return self.x * obj.x + self.y * obj.y
        return None

    def get_angle(self, vec):
        if isinstance(vec, self.__class__):
            return math.acos(self.get_scalar_product(vec) / (self.get_length() * vec.get_length()))
        return None

class Line:
    def __init__(self, A: float, B: float, C: float):
        if A * A + B * B:
            self.A = A
            self.B = B
            self.C = C
            self.correct = True
        else:
            self.correct = False

    def __bool__(self):
        return self.correct

    def __str__(self):
        return f"{self.A}x + {self.B}y + {self.C} = 0"

    @classmethod
    def directional_line(cls, a: float, b: float):
        return cls(a, -1, b)

    @classmethod
    def two_points_line(cls, point_a: Point, point_b: Point):
        return cls((point_b.y - point_a.y) / (point_b.x - point_a.x), -1, 
                   (point_a.y * point_b.x - point_b.y * point_a.x) / (point_b.x - point_a.x))

    @classmethod
    def vector_line(cls, point: Point, vec: Vector):
        return cls(vec.x, vec.y, -vec.get_scalar_product(point))

    def get_direction(self):
        return Vector(self.A, self.B)

    def get_gradient(self):
        if self.B:
            return -self.A / self.B
        return None

    def get_OX_intersection(self):
        if self.A:
            return -self.C / self.A
        return None

    def get_OY_intersection(self):
        if self.B:
            return -self.C / self.B
        return None

    def get_gradient_formula(self):
        return self.get_gradient(), self.get_OY_intersection()

    def get_line_intersection(self, line):
        if denom := self.A * line.B - self.B * line.A:
            return Point((self.B * line.C - self.C * line.B) / denom, (self.A * line.C - self.C * line.A) / denom)
        return None

    def get_perp_line(self, point: Point):
        return Line(self.B, -self.A, self.A * point.y - self.B * point.x)

    def get_parallel_line(self, point: Point):
        return Line(self.A, self.B, -self.A * point.x - self.B * point.y)

    def get_dist_from_point(self, point: Point):
        return point.get_dist_from_line(self)

    def get_dist_from_line(self, line):
        if not self.A * line.B - self.B - line.A:
            return abs(line.C * self.A / line.A - self.C) / (self.A * self.A + self.B * self.B)
        return 0

class LineSegment:
    def __init__(self, point_a: Point, point_b: Point):
        self.point_a = point_a
        self.point_b = point_b

    def __str__(self):
        return f"{str(self.point_a)} --- {str(self.point_b)}"

    @classmethod
    def vector_line_segment(cls, point: Point, vec: Vector):
        return cls(point, vec.move_point(point))

    def get_length(self):
        return self.point_a.get_dist_from_point(self.point_b)

    def get_center(self):
        return Point((self.point_a.x + self.point_b.x) / 2, (self.point_a.y + self.point_b.y) / 2)

    def get_segment_line(self):
        return Line.two_points_line(self.point_a, self.point_b)

    def get_bisection(self):
        return self.get_segment_line().get_perp_line(self.get_center())

class PolygonChain:
    def __init__(self, points: list, closed: bool):
        if len(points) > 2:
            self.points = points
            self.closed = closed
            self.segments = [LineSegment(points[i], points[i + 1]) for i in range(len(points) - 1)]
            if closed:
                self.segments.append(LineSegment(points[-1], points[0]))
            self.correct = True
        else:
            self.correct = False

    def __bool__(self):
        return self.correct

    def __str__(self):
        msg = ""
        for point in self.points:
            msg += f" - {str(point)}"
        if self.closed:
            msg += f" - {str(self.points[0])}"
        return msg[3:]

    def get_length(self):
        return sum([segment.get_length() for segment in self.segments])

    def get_center(self):
        return Point(sum([point.x for point in self.points])/len(self.points),
                     sum([point.y for point in self.points])/len(self.points))

class Triangle(PolygonChain):
    def __init__(self, point_a: Point, point_b: Point, point_c: Point):
        self.v = Vector.two_points_vector(point_a, point_b)
        self.w = Vector.two_points_vector(point_a, point_c)
        self.u = Vector.two_points_vector(point_b, point_c)
        self.alpha = self.v.get_angle(self.w)
        self.beta = self.v.get_scaled_vector(-1).get_angle(self.u)
        self.gamma = self.w.get_angle(self.u)
        if math.sin(self.alpha):
            super().__init__([point_a, point_b, point_c], True)
        else:
            self.correct = False

    def get_area(self):
        return self.v.get_length() * self.w.get_length() * math.sin(self.alpha) / 2

    def get_orthocenter(self):
        pass

    def get_inner_circle(self):
        pass

    def get_outer_circle(self):
        pass

    def get_euler_circle(self):
        pass

    def get_euler_line(self):
        pass

    def is_inner_point(self, point: Point):
        return True

    def get_barycentric_coords(self, point: Point):
        if self.is_inner_point(point):
            a = self.__class__(self.points[2], self.points[0], point).get_area() / self.get_area()
            b = self.__class__(self.points[0], self.points[1], point).get_area() / self.get_area()
            c = self.__class__(self.points[1], self.points[2], point).get_area() / self.get_area()
            return a, b, c
        return None

class Circle:
    def __init__(self, radius: float, center: Point):
        if radius > 0:
            self.radius = radius
            self.center = center
            self.correct = True
        else:
            self.correct = False

    def __bool__(self):
        return self.correct

    def __str__(self):
        return f"O(R = {self.radius}, C = {str(self.center)})"

    def get_diameter(self):
        return 2 * self.radius

    def get_cirumference(self):
        return math.pi * self.get_diameter()

    def get_area(self):
        return math.pi * self.radius * self.radius

    def get_tangent_line(self, point: Point):
        return LineSegment(self.center, point).get_segment_line().get_perp_line(point)
