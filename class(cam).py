class Person:
    def __init__(self,isim,yas,cinsiyet,memleket):

        self.isim=isim
        self.yas=yas
        self.cinsiyet=cinsiyet
        self.memleket=memleket

kisi1=Person('mert',24,'erkek','samsun')
kisi2=Person('berkan',10,'erkek','samsun')
kisi3=Person('zehra',11,'kız','ardahan')

print(kisi2.yas)
print(kisi1.isim)
