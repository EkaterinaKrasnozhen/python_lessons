#3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'абв абвгдейка ура что сабв сам'.split()
x = 'абв'
 
lis = [i for i in text if x not in i]

print(*lis)

    