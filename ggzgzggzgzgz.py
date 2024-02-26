def gelismis_hesap_makinasıi():
    while True:
        print('\nhesap makinesine hoşgeldiniz!:loading...')
        print('1. Toplama')
        print('2. Çıkarma')
        print('3. Çarpma')
        print('4. Bölme')
        print('5. Hesap Makinasından Çık.(/ :( /)')


        secim = input('bir işlem seçiniz pls (1/2/3/4/5): ')

        if secim in ('1','2','3','4'):
            sayilar = input('lütfen sayiların arasına boşluk koyunuz pls')
            sayi_listesi=[float(sayi) for sayi in sayilar.split()]


            if secim == '1':
                sonuc = sum(sayi_listesi)
            elif secim == '2':
                sonuc = sayi_listesi[1:]:
                for sayi in sayi_listesi[1:]:
                    sonuc -= sayi
            elif secim == '3':
                sonuc=1
                for sayi in sayi_listesi:
                    sonuc *= sayi
            elif secim == '4':
                sonuc = sayi_listesi[0]
                try:
                    for sayi in sayi_listesi[1:]:
                        sonuc /= sayi

                except ZeroDivisionError:
                        print('Hata!type error!systax error! sıfır bolünmeeeez!')
                        continue
            print('sonuç', sonuc)

        elif secim =='5':
            print(


                
                    
    



              
