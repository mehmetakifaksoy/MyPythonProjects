#  liste = ["1","2","5a","10b","abc","10","50"]


# 1 : liste elemanları içindeki sayısal değerleri bulunuz.



#for x in liste:
  #  try:
     #     result = int(x)
     #     print(result)
   #   except ValueError:
     #     continue



# 2 : kullanıcı "q" değerlerini girmedikçe aldığınız her inputun sayı olup  olduğundan emin olunuz aksi halde hata mesajı yazın.


#while True:
 #   sayi = input('sayı: ')
  #  if sayi == 'q':
   #     break

  #  try:
   #     result = float(sayi)
    #    print('girdiginiz sayi : ' , result)
    #    break
  #  except ValueError:
   #         print('gecersiz sayi')
    #        continue


    # girilen parola içinde türkçe karakter hatası veriniz.

#def chekPassword(parola):
 #   turkce_karakterler = "şçğüöıİ"    
  #  parola = input('parola: ')

  #  for i in parola:
  #      if i in turkce_karakterler:
 #           raise TypeError('Parola türkçe karakter içermez')
  #      else:
  #          pass
  #      print('gecerli parola')

#parola = input('parola: ')

#try : 
  #  checkPassword(parola)
#except TypeError as err:
 #   print(err)

# 4: faktoriyel fonsiyonun oluşturup fonsiyona gelen değer için hata mesajları verin




def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError('Negatif Değer')


    result = 1

    for i in range(1, x+1):
        result *=i
        
    return result



for x in [5, 10, 20, -3, '10a']:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)    







































