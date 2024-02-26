import random


liste=[]
i=0
toplam=0

while i<5:
    sayi=random.randint(1,100)
    liste.append(sayi)
    i=i+1

for element in liste:
    toplam=toplam+element
print(liste)
print('oluşturulan sayıların toplamı=',toplam)
