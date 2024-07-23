# Самостоятельная работа по уроку "Произвольное число параметров".

other_words = [
    'городской', 'Город', 'огород', 'междугородный', 'гараж',
    'поселок', 'внегородской', 'ОбЩЕгородСКОЙ', 'внутригородской']
def singl_root_words(root_word, *other_words):
    '''возращает список same_words из строковых элементов списка other_words
       в которые входит строка root_word и элементов списка other_words, которые
       входят в строку root_word'''
    same_words = []
    for word in other_words:
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():
            same_words.append(word)

    return same_words

same_words = singl_root_words('ГОРОДСКОЙ',*other_words)
print(same_words)