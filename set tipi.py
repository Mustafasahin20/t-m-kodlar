#SET VERİ TİPİ
#set veri tipinde elemanlar listelenelemez
#listelenmedikleri için index numarası yoktur
#dolaysıyla listeyi çağırdığımız zaman her bir eleman yeri
#farklı gelir
#tekrarlanamazlar, her eleman bir tane olmalıdır
# {} süslü parantez kullanılır

set_liste={1,2,3,4,5}

set_liste.add(6)
print(set_liste)

print(6 in set_liste)

set_liste.update([7,8,9])

print(set_liste)

set_liste.remove(3)
print(set_liste)
