#how to create class --> it has to has key word (class), it has to has constructor class (_init_())
#it has to has self parameter in the first class in every method
class PersegiPanjang:
    def __init__(self, panjang,lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang*self.lebar

    def hitung_keliling(self):
        return (self.panjang+self.lebar)*2

    def gambar_persegi_panjang(self):
        for i in range(0,self.panjang):
            for j in range(0,self.lebar):
                print "*",
            print ""

    def gambar_persegi_panjang_tanpa_isi(self):
        for i in range(0,self.panjang):
            if i>0 and i<self.panjang-1:
                for j in range(0, self.lebar):
                    if j>0 and j<self.lebar-1:
                        print ' ',
                    else:
                        print "*",
            else:
                for j in range(0,self.lebar):
                    print "*",

            print ""



persegipanjangA = PersegiPanjang(5,10)
#Built-in function class and object
print PersegiPanjang.__doc__
print PersegiPanjang.__name__
print PersegiPanjang.__dict__
print PersegiPanjang.__module__
print PersegiPanjang.__bases__
print persegipanjangA.__doc__
print persegipanjangA.__dict__
print persegipanjangA.__module__




persegipanjangB = PersegiPanjang(10,20)

print "Panjang Persegi Panjang A adalah :", persegipanjangA.panjang
print "Panjang Persegi Panjang B adalah :", persegipanjangB.lebar
print "Luas Persegi Panjang A adalah :", persegipanjangA.hitung_luas()
print "Keliling Persegi Panjang A adalah :", persegipanjangA.hitung_keliling()
print "Menggambar Persegi Panjang A :"
persegipanjangA.gambar_persegi_panjang()
print "Menggambar Tepi Persegi Panjang A :"
persegipanjangA.gambar_persegi_panjang_tanpa_isi()

