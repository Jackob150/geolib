import math

from src.constans import epsilon
from src.exceptions import ZeroLengthVectorNormalized, PointOutsideLine

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x} , {self.y})"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return abs(self.x - other.x) < epsilon and abs(self.y - other.y) < epsilon
        return False

    def get_dist_from_point(self, point):
        if isinstance(point, self.__class__):
            return math.sqrt((self.x - point.x) * (self.x - point.x) + (self.y - point.y) * (self.y - point.y))
        return None

    def get_dist_from_line(self, line):
        if isinstance(line, Line):
            return abs(line.A * self.x + line.B * self.y + line.C) / math.sqrt(line.A * line.A + line.B * line.B)
        return None

    def get_vector(self):
        return Vector(self.x, self.y)

    def move_by_vector(self, vec):
        if isinstance(vec, Vector):
            self.x += vec.x
            self.y += vec.y

    def get_moved_by_vector(self, vec):
        return Point(self.x + vec.x, self.y + vec.y)

    def rotate_around_origin(self, angle: float):
        vec = Vector(self.x, self.y)
        vec.rotate_by_angle(angle)
        self.x = vec.x
        self.y = vec.y

    def get_rotated_around_origin(self, angle):
        vec = Vector(self.x, self.y)
        vec.rotate_by_angle(angle)
        return Point(vec.x, vec.y)

    def rotate_around_point(self, center, angle: float):
        if isinstance(center, self.__class__):
            self.x -= center.x
            self.y -= center.y
            self.rotate_around_origin(angle)
            self.x += center.x
            self.y += center.y

    def get_rotated_around_point(self, center, angle: float):
        if isinstance(center, self.__class__):
            p = Point(self.x - center.x, self.y - center.y)
            p.rotate_around_origin(angle)
            p.x += center.x
            p.y += center.y
            return p
        return None

class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __bool__(self):
        return bool(self.x + self.y)

    def __str__(self):
        return f"[{self.x} , {self.y}]"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return abs(self.x - other.x) < epsilon and (self.y - other.y) < epsilon
        return False

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
        try:
            length = self.get_length()
            self.x /= length
            self.y /= length
        except:
            raise ZeroLengthVectorNormalized()


    def get_normalized(self):
        if length := self.get_length():
            return self.__class__(self.x / length, self.y / length)
        return None

    def get_moved_point(self, point: Point):
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
        if isinstance(vec, self.__class__) and self.get_length() and vec.get_length():
            return math.acos(self.get_scalar_product(vec) / (self.get_length() * vec.get_length()))
        return None

    def get_outer_product(self, vec):
        if isinstance(vec, self.__class__):
            return self.x * vec.y - self.y * vec.x
        return None

    def rotate_by_angle(self, angle: float):
        tmp_x = math.cos(angle) * self.x - math.sin(angle) * self.y
        tmp_y = math.sin(angle) * self.x + math.cos(angle) * self.y
        self.x = tmp_x
        self.y = tmp_y

    def get_rotated_by_angle(self, angle: float):
        return Vector(math.cos(angle) * self.x - math.sin(angle) * self.y,
                      math.sin(angle) * self.x + math.cos(angle) * self.y)

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

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if abs(self.A * other.C - self.C * other.A) < epsilon and \
               abs(self.B * other.C - self.C * other.B) < epsilon and \
               abs(self.A * other.B - self.B * other.A) < epsilon:
                return True
        return False

    @classmethod
    def directional_line(cls, a: float, b: float):
        return cls(a, -1, b)

    @classmethod
    def two_points_line(cls, point_a: Point, point_b: Point):
        if not point_a == point_b:
            return cls(-(point_b.y - point_a.y), point_b.x - point_a.x, 
                    point_a.x * point_b.y - point_a.y * point_b.x)
        return None

    @classmethod
    def vector_line(cls, point: Point, vec: Vector):
        if vec.x or vec.y:
            return cls(-vec.y, vec.x, point.get_vector().get_outer_product(vec))
        return None

    def is_point_in_line(self, point: Point):
        if abs(self.A * point.x + self.B * point.y + self.C) < epsilon:
            return True
        return False

    def get_direction(self):
        return Vector(-self.B, self.A)

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
        if self.B:
            return self.get_gradient(), self.get_OY_intersection()
        return None

    def get_line_intersection(self, line):
        if denom := self.B * line.A - self.A * line.B:
            return Point((self.C * line.B - self.B * line.C) / denom, (self.A * line.C - self.C * line.A) / denom)
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

    def rotate_by_angle(self, angle: float, point: Point):
        if self.is_point_in_line(point):
            tmp_A = math.cos(angle) * self.A - math.sin(angle) * self.B
            tmp_B = math.sin(angle) * self.A + math.cos(angle) * self.B
            self.A = tmp_A
            self.B = tmp_B
            self.C = -self.A * point.x - self.B * point.y
        else:
            raise PointOutsideLine(self, point)

    def get_rotated_by_angle(self, angle: float, point: Point):
        if self.is_point_in_line(point):
            return Line(math.cos(angle) * self.A - math.sin(angle) * self.B,
                        math.sin(angle) * self.A + math.cos(angle) * self.B,
                        -(math.cos(angle) * self.A - math.sin(angle) * self.B) * point.x \
                        -(math.sin(angle) * self.A + math.cos(angle) * self.B) * point.y)
        return None

class LineSegment:
    def __init__(self, point_a: Point, point_b: Point):
        if not point_a == point_b:
            self.point_a = point_a
            self.point_b = point_b
            self.correct = True
        else:
            self.correct = False

    def __str__(self):
        return f"{str(self.point_a)} --- {str(self.point_b)}"

    def __bool__(self):
        return self.correct

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.point_a == other.point_a and self.point_b == other.point_b) or \
                   (self.point_a == other.point_b and self.point_b == other.point_a)
        return False

    @classmethod
    def vector_line_segment(cls, point: Point, vec: Vector):
        if vec.x or vec.y:
            return cls(point, vec.get_moved_point(point))
        return None

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

    def get_edge_lines(self):
        return [Line.two_points_line(self.points[1], self.points[2]),
                Line.two_points_line(self.points[0], self.points[2]),
                Line.two_points_line(self.points[0], self.points[1])]

    def get_heights(self):
        e_lines = self.get_edge_lines()
        h_points = [e_line.get_perp_line(i).get_line_intersection(e_line) for i, e_line in enumerate(e_lines)]
        return [LineSegment(self.points[i], h_point) for i, h_point in enumerate(h_points)]

    def get_angle_bisections(self):
        sign = self.v.get_outer_product(self.w)
        return [Line.vector_line(self.points[0], self.v.get_rotated_by_angle(sign * self.alpha / 2)),
                Line.vector_line(self.points[1], self.v.get_rotated_by_angle(sign * self.beta / 2)),
                Line.vector_line(self.points[2], self.v.get_rotated_by_angle(sign * self.gamma / 2))]

    def get_orthocenter(self):
        return self.get_heights()[0].get_segment_line().get_line_intersection(self.get_heights()[1].get_segment_line())

    def get_inner_circle(self):
        bis = self.get_angle_bisections()
        center = bis[0].get_line_intersection(bis[1])
        return Circle(center.get_dist_from_line(self.get_edge_lines()[0]), center)

    def get_outer_circle(self):
        e_lines = self.get_edge_lines()
        c_p = e_lines[0].get_perp_line(LineSegment(self.points[1], self.points[2]).get_center()).get_line_intersection(
              e_lines[1].get_perp_line(LineSegment(self.points[0], self.points[2]).get_center()))
        return Circle(c_p.get_dist_from_point(self.points[0]), c_p)

    def get_euler_circle(self):
        pass

    def get_euler_line(self):
        pass

    def is_inner_point(self, point: Point):
        a_to_point = Vector.two_points_vector(self.points[0], point)
        b_to_point = Vector.two_points_vector(self.points[1], point)
        return bool(self.v.get_outer_product(a_to_point) + self.v.get_outer_product(self.w)) and \
               bool(self.u.get_outer_product(b_to_point) + self.u.get_outer_product(self.v.get_scaled_vector(-1))) and \
               self.v.get_angle(a_to_point) <= self.alpha and self.u.get_angle(b_to_point) <= self.beta

    def get_barycentric_coords(self, point: Point):
        if self.is_inner_point(point):
            a = self.__class__(self.points[2], self.points[0], point).get_area() / self.get_area()
            b = self.__class__(self.points[0], self.points[1], point).get_area() / self.get_area()
            c = self.__class__(self.points[1], self.points[2], point).get_area() / self.get_area()
            return a, b, c
        return None

    def get_barycentric_point(self, a: float, b: float, c: float):
        return Point(a * self.points[0] + b * self.points[1] + c * self.points[2],
                     a * self.points[0] + b * self.points[1] + c * self.points[2])

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

    @classmethod
    def general_circle(cls, a: float, b: float, c: float):
        return cls(math.sqrt((a / 2) ** 2 + (b / 2) ** 2 - c), Point(-a / 2, -b / 2))

    def get_diameter(self):
        return 2 * self.radius

    def get_cirumference(self):
        return math.pi * self.get_diameter()

    def get_area(self):
        return math.pi * self.radius * self.radius

    def get_tangent_line(self, point: Point):
        return LineSegment(self.center, point).get_segment_line().get_perp_line(point)

    def get_chord(self, line: Line):
        if h := line.get_dist_from_point(self.center) <= self.radius:
            perp = line.get_perp_line(self.center)
            alpha = math.acos(h / self.radius)
            pa = perp.get_rotated_by_angle(alpha, self.center).get_line_intersection(line)
            pb = perp.get_rotated_by_angle(-alpha, self.center).get_line_intersection(line)
            return LineSegment(pa, pb)
        return None
