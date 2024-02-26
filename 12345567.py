class Ogrenci:
    def __init__(self,isim,okul_no,sinif,soyisim):
        self.isim=isim
        self.okul_no=okul_no
        self.soyisim=soyisim
        self.sinif=sinif

kisi1=ogrenci('mustafa',407,'ŞAHİN','3/G')
kisi2=ogrenci('yağız',562,'ÖMER','3/B')

print(kisi1)
print(kisi1.isim)
print(kisi2.okul_no)
