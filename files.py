#dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
#kullanımı : open(dosya_adi,dosya_erişme_mode)
#dosya_erişme_mode => dosyayı hangi amaçla açtığımızı belirtir.

 # "w" : (write) yazma modu dosyayı konumda oluşturur.

#file = open("newfile.txt","w")
#file.close()



#file = open("c:/Users/Dell/Desktop/newfile.txt","w")
#print(file)


#file =open("newfile.txt","w" , encoding='utf-8')
#file.write("MehmetAkifAKSOY")
#file.write("Arife")
#file.write("Senem")
#file.write("Ahmet")
#file.write("Bihar")
#file.write("Ege")
#file.close()

 # "a" : (Append) ekleme Dosya konumda yoksa oluşturur.

#file =open("newfile.txt","a" , encoding='utf-8')
#file.write("\n MehmetAkifAKSOY")
#file.write("\n Mehmet")
#file.write("\n Ahmet")
#file.write("\n sevgi")
#file.write("\n senem")
#file.write("\n Arif")
#file.write("\n AKSOY")
#file.write("\n AkifAKSOY")
#file.close

# "x " : (create) oluşturma dosya zaten varsa hata verir.

#file =open("newfile2.txt","x" , encoding='utf-8')

 # "r" : (read) okuma varsayılan  dosya konumda yoksa hata verir.

 



