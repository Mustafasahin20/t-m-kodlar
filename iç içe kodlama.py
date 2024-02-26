#içiçe koşullar
isim = input('isminizi giriniz')
soyisim = input('soyisimini giriniz')
e_mail = input('e mail giriniz')
kullanici_adi = input('kullanıcı adını giriniz')
sifre = input('şifrenizi giriniz')

print(f'merhaba {isim} {soyisim} hesabınız başarıyla oluşturuldu!')
print('devam etmek içim lütfen giriş yapınız')

kullanici_adi2 = input('kullanıcı adınızı giriniz')
sifre2 = input('şifrenizi giriniz')

if kullanici_adi==kullanici_adi2:
    if sifre==sifre2:
        print('Sisteme başarıyla giriş yapıldı!')
    else:
        print('Şifreler eşleşmedi, sisteme girilmedi!')
else:
    print('kullanıcı adı hatalı, sisteme girilmedi!')
