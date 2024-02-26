import random

hedefgzgzgzgz=random.randint(1,10)
deneme=0

while True:
    tahmin=int(input('bir sayı tahmin ediniz'))
    deneme+=1

    if tahmin<hedefgzgzgzgz:
        print('daha yüksek bir sayı tahmin ediniz.')
    elif tahmin>hedefgzgzgzgz:
        print('daha düşük bir sayı tahmin ediniz.')

    else:
        print(f'tebrikler,{hedefgzgzgzgz}`ı {deneme} denemede buldunuz!')
        break
