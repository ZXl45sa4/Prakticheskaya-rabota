class WordsFinder:
    def __init__(self, *file_names):     # Метод при инциализации создает файл и записвает
        self.file_names = file_names
        for i in file_names:
            f = open(i, 'w',  encoding='utf 8')
            f.write("It's a text for task Найти везде, \n"
                    "Используйте его для самопроверки. \n"
                    "Успехов в решении задачи! \n"
                    "text text text")
            f.close()
        return

    def __add__(self):
        return WordsFinder(self.file_names)

    def get_products(self):       # Считывание из указанного файла
        for j in self.file_names:
            with open(j, "r", encoding='utf-8') as f:
                content = f.read()
                f.close()
            return content

    def get_all_words(self):
        all_words = {}
        for k in self.file_names:
            with open(k, "r", encoding='utf-8') as f:
                content_2 = f.read().lower()
                bez_probela = content_2.replace("\n","")
                punktuatsiya = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for l in punktuatsiya:
                    bez_probela = bez_probela.replace(l, '')
                wor = bez_probela.split(' ')
                all_words[k] = wor
        return all_words

    def find(self, word):
        slovo_po_schotu = {}
        for file_names, w in self.get_all_words().items():
            if word.lower() in w:
                slovo_po_schotu[file_names] = w.index(word.lower()) + 1
        return slovo_po_schotu

    def count(self, word):
        slova_v_tekste = {}
        for file_names, w in self.get_all_words().items():
            slova_v_tekste[file_names] = w.count(word.lower())
        return slova_v_tekste

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
