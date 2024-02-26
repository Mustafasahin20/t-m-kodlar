import random

def sayi_tahmin():
    while True:
        rastgele_sayi=random.randint(1,100)
        i=0
        while i<5:
            tahmin=int(input('bir sayı giriniz'))
            i=i+1
            if tahmin==rastgele_sayi:
                       print('kazandın')
                       break
            elif tahmin<rastgele_sayi:
                print('hayırr dahaaaa yükseeekk sayi giiiiiiirrrrrrr')
            elif tahmin>rastgele_sayi:
                print('''haayyıııııırrrrrrr daaahhhhaaaaa kkküüüüüççççüüüükkkkk
sayi giiiiirrrrrrrrr!''')
        else:
            print('''kaaaaaaaaayyyyyyybbbbbbbbeeeeeeeetttttttttttttiiiiiiiinnnnn
eeeeeezzzzzzzzziiiiiiiiiiiiiiiikkkkkkkkk!!!!!!!:):):)''')

sayi_tahmin()
