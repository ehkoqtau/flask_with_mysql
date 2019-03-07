from math import pi

class Lingkaran(object):
    def __init__(self):
        self.radius = 0
        
    def setRadius(self, r):
        self.radius = r
    
    def getRadius(self):
        return self.radius

    def hitungLuas(self):
        return pi * (self.radius ** 2)

    def hitungKeliling(self):
        return 2 * pi * self.radius