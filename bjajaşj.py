class Ogrenci():
    def __init__(self,isim,soyisim,sinif,okul_no):
        self.isim=isim
        self.okul_no=okul_no
        self.soyisim=soyisim
        self.sinif=sinif

    def Talk(self):
        print(f'''Benim adım {self.isim}. Soyisimim ise {self.soyisim}.
              Ben {self.sinif}}
