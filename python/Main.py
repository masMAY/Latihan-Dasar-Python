from Bidang import Segitiga,Persegi

segitigaA = Segitiga(6,8)
persegiA = Persegi(60)

print "Luas SegitigaA :", segitigaA.hitungLuas()
print "Sisi Miring SegitgaA :", segitigaA.getSisiMiring()
print "Keliling SegitigaA :", segitigaA.hitungKelilig(segitigaA.getSisiMiring())
print "\n"
print "Luas PersegiA :", persegiA.hitungLuas()
print "Keliling Persegi A :", persegiA.hitungKeliling()