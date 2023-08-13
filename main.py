import re

# 1. Даний текстовий файл. Необхідно створити новий файл, який потрібно переписати з першого файлу всі слова,
# що складаються не менше ніж з семи літер.

try:
    with open('Text1.txt', 'r', encoding='utf-8') as first_file:
        words_from_first_file = re.split(r'[:;,.\-\s]+', first_file.read())
    with open('Text2.txt', 'w', encoding='utf-8') as second_file:
        for word in words_from_first_file:
            if len(word) >= 7:
                word += ', '
                second_file.write(word)
    with open('Text2.txt', 'r', encoding='utf-8') as second_file:
        print(second_file.read())
except Exception as e:
    print(e)

# 2. Даний текстовий файл. Підрахувати кількість слів у ньому.

