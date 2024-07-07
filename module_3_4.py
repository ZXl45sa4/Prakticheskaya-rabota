
def single_root_words (root_word, *other_words): #Объявите функцию single_root_words и
                                                # напишите в ней параметры root_word и *other_words.
    same_words = []                             #Создайте внутри функции пустой список same_words,
                                                # который пополнится нужными словами.
    for i in other_words:                   #При помощи цикла for переберите предполагаемо подходящие слова.
        if root_word.upper() in  i.upper() or i.lower() in root_word.lower():
            same_words.append(i)                # добавляются слова в результирующий список same_words.
    return same_words                            # После цикла верните образованный функцией список same_words.
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)