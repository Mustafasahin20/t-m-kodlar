#çoklu koşullar
sinav1=int(input('1.sınav notunuzu giriniz:'))
sinav2=int(input('2.sınav notunuzu giriniz:'))
ortalama=(sinav1+sinav2)/2
print(ortalama)

if ortalama>=85:
    print('PEKİYİ')
elif ortalama>=65:
    print('İYİ')
elif ortalama>=45:
    print('ORTA')
elif ortalama>=37
    print('GEÇER')
else:
    print('KALDIN')

