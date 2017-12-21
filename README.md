# project_1
CONS = u"бвгджзклмнпрстфхцчшщ"
VOW = u"аеёиоуыэюя"
text = str(input("введите слово или прпедложение на русском\n>>>"))

cons = sum(1 for t in text.lower() if t in CONS)
vow = sum(1 for t in text.lower() if t in VOW)

print (cons,"- согласных",vow,"- гласных")

print('~'*30)
