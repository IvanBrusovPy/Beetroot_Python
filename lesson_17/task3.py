class Fraction:
    def __init__(self, a, b):
        if isinstance(a, int) and not (1 > a > 0):
            self.a = a
        else:
            raise ValueError("Wrong first number")
        if isinstance(b, int) and not (1 > b >= 0):
            self.b = b
        elif b == 0:
            raise ZeroDivisionError("Division by zero. Wrong number")
        else:
            raise ValueError("Wrong second number")

    def __add__(self, other):
        temp = Fraction(self.a, self.b)
        if not isinstance(other, type(self)):
            raise TypeError("Wrong type. Only fraction")
        else:
            temp.a = (self.a * other.b) + (other.a * self.b)
            temp.b *= other.b
            return temp

    def __sub__(self, other):
        temp = Fraction(self.a, self.b)
        if not isinstance(other, type(self)):
            raise TypeError("Wrong type. Only fraction")
        else:
            temp.a = (self.a * other.b) - (other.a * self.b)
            temp.b *= other.b
            return temp

    def __truediv__(self, other):
        temp = Fraction(self.a, self.b)
        if not isinstance(other, type(self)):
            raise TypeError("Wrong type. Only fraction")
        else:
            temp.a *= other.b
            temp.b *= other.a
            return temp

    def __mul__(self, other):
        temp = Fraction(self.a, self.b)
        if not isinstance(other, type(self)):
            raise TypeError("Wrong type. Only fraction")
        else:
            temp.a *= other.a
            temp.b *= other.b
            return temp

    def __eq__(self, other):
        return round(self.a/self.b, 5) == round(other.a/other.b, 5)

    def __lt__(self, other):
        return round(self.a/self.b, 5) < round(other.a/other.b, 5)

    def __gr__(self, other):
        return round(self.a/self.b, 5) > round(other.a/other.b, 5)

    def __str__(self):
        return f"{self.a} / {self.b}"


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x + y == Fraction(3, 4))
