def tek_cift(sayi):
    
    if sayi%2==0:
        print(sayi,'sayısı çifttir')
    else:
        print(sayi,'sayısı tektir')
        
sayi=int(input('lütfen bir sayı giriniz: '))
        

print('''merhaba girilen sayının tek mi çift mi olduğunu bulan programa
hoşgeldiniz!
GİRİLEN SAYI: ''')

tek_cift(sayi)
