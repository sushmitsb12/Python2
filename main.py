class Triangle:
    def __init__(self,angle1,angle2,angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    number_of_sides = 3
    def check_Triangle(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False
class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        angle = 60
        self.a1 = self.a2 = self.a3 = self.angle

t = Triangle(60,90,30)
print(t.check_Triangle())