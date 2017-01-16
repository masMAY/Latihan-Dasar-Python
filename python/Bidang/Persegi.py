#implementasi package and modul
class Persegi:
    def __init__(self,s):
        self.sisi = s

    def setSisi(self,s):
        self.sisi = s

    def getSisi(self):
        return self.sisi

    def hitungLuas(self):
        return self.sisi**2

    def hitungKeliling(self):
        return self.sisi*4


