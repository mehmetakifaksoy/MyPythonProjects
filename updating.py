# # with open("newfile.txt","r+", encoding="utf-8") as file:
# #     file.seek(12)
# #     print(file.write("deneme"))

# # with open("newfile.txt","r+", encoding="utf-8") as file:
# #     file.seek(20)
# #     print(file.read())

# # **********sayfa sonunda güncelleme*************


# # with open("newfile.txt","a",encoding="utf-8") as file:
# #     print(file.write("\nmehmet"))


# # **********sayfa basında güncelleme*************


# # with open("newfile.txt","r+",encoding="utf-8") as file:
# #     content = file.read()
# #     content = "mehmet aksoy\n" + content
# #     print(content)
# #     file.seek(0)
# #     file.write(content)



with open("newfile.txt","r+",encoding="utf-8") as file:
     list = file.readlines()
     list.insert(1,"Ali Korkmaz")
     list.insert(4,"senem aksoy")
     list.insert(5,"cansu bektaslı")
     file.seek(0)
     print(list)

# # **********sayfa ortasında güncelleme*************

