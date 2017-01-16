import math

class Segitiga:
    def __init__(self,a,t):
        self.alas = a
        self.tinggi = t

    def setAlas(self,a):
        self.alas = a

    def setTinggi(self,t):
        self.tinggi = t

    def getAlas(self):
        return self.alas

    def getTinggi(self):
        return  self.tinggi

    def getSisiMiring(self):
        return math.sqrt(self.alas**2 + self.tinggi**2)

    def hitungKelilig(self,s):
        return self.alas + self.tinggi + s

    def hitungLuas(self):
        return self.alas * self.tinggi *1/2

    