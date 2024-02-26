import random

def kelime_sec():
    kelime_listesi=['''Pokemon yolculukları,india louge,yüzükler efendisi,leo,
sihirli ejder,pokemon ustası yolculukları,pokemon benzersiz yolculukları,pokemon
ustası olmak,yüzüklerin efendisi2,yıldızlar arası''']
    return random.choice(kelime_listesi)

def adam_asmaca_tahtasi(can):
    tahta = [
        '''
            +---+
            |   |
                |
                |
                |
                |
            ======== ''',

        '''
            +---+
            |   |
            O   |
                |
                |
                |
            ======== ''',

         '''
            +---+
            |   |
            O   |
            |   |
                |
                |
            ======== ''',

        '''
            +---+
            |   |
            O   |
           /|   |
                |
                |
            ======== ''',

         '''
            +---+
            |   |
            O   |
           /|\  |
                |
            ======== ''',

        '''
            +---+
            |   |
            O   |
           /|\  |
           /\   |
            ======== '''
    ]
    return tahta[6 - can]

def adam_asmaca_oyunu():
    secilen_kelime=kelime_sec()
    kelime_uzunluk=len(secilen_kelime)
    kelime=['_']*kelime_uzunluk
    can=6
    oyun_sonu=False

    print('film adam asmacısına hoşgeldin.')    

    while not oyun_sonu:
        tahmin=input('bir harf giriniz: ').lower()
        if not tahmin.isalpha() or len(tamin) !=1:
            print('lütfen geçerli bir harf giriniz.')
            continue

        if tahmin in kelime:
            print('bu harfi zaten tahmin ettiniz.tekrar deneyiniz: ')
            continue

        if tahmin not in secilen_kelime:
            can-=1
            print('yanlış tahmin! kalan can: {}'.format(can))


        for i in range(kelime_uzunluk):
            harf = secilen_kelime[i]
            if harf==tahmin:
                kelime[i]=harf


        print(adam_asmaca_tahtasi(can))
        print('tahmin durumu: {}'.format(' '.join(kelime)))


        if '_' not in kelime:
            oyun_sonu=True
            print('tebrikler!kelimeyi doğru buldunuz.')

        elif can==0:
            oyun_sonu=True

adam_asmaca_oyunu()
        
