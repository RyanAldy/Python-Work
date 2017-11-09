class One:
    # Constructor
    def __init__(self):
        self.a = 0
        self.b = 0
    def assign(self, x, y):
        self.a = x
        self.b = y
    # Overloading add method
    def __add__(self, R):
        x = One()
        x.a = self.a + R.b
        x.b = self.b + R.b
        return x
    def __sub__(self, R):
        x = One()
        x.a = self.a - R.a
        x.b = self.b - R.b
        return x
    def __mul__(self, R):
        x = One()
        x.a = self.a * R.a
        x.b = self.b * R.b
        return x
    def __div__(self, R):
        x = One()
        x.a = self.a / R.a
        x.b = self.b / R.b


a = One()
a.assign(2,4)
b = One()
b.assign(10,20)
# Adding two objects of the one class here as overloaded the addition operator
c = b + a
print(c.a)
print(c.b)

d = One()
d.assign(20,10)
e = One()
e.assign(15,2)
f = d - e
print(f.a)
print(f.b)
