#mengenal Fungsi raw_input (input data dari user)

name = raw_input('masukkan nama bangun :')
alas = raw_input("alas :")
tinggi = raw_input("tinggi :")

print "Nama Bangun adalah :", name
luas =  float(alas) * float(tinggi) * 1/2 
print luas
print "Luas", name, " dengan ukuran %f %f adalah %f" %(float(alas), float(tinggi), luas)


