
oyunlar = ['roblox,entry point,glass,break in story2,minecraft']
print(oyunlar[3])

oyunlar.append('brookhaven')
print(oyunlar)

#clear komutu listeyi temizler.
#copy komutu listeyi kopyalar.

sayi = oyunlar.count('roblox')
print(sayi)

#extend komutu iki listeyi birbirine bağlar.

print(oyunlar.index('glass'))

oyunlar.insert(5,'brookhaven')
print(oyunlar)

oyunlar.pop(5)
print(oyunlar)

oyunlar.remove('minecraft')
print(oyunlar)
