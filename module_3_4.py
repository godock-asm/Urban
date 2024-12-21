

same_words = []
words = []

def single_root_words(root_word, *other_words):
    same_words = []
    words = []
    word = str(root_word).lower()
    other_words = str(*other_words)
    l = 0
    start = 0  # Начало строки
    while l < len(other_words):
        ltr = other_words[l]
        if  ltr == ' ':
            l = l + 1
            nxt_word = other_words[start:l-1]
            start = l
            if len(nxt_word) == 0:  # пропускаем пробелы
                continue
            words.append(nxt_word)
            if nxt_word.lower() in word:
                print(f'{root_word} содержит слово {nxt_word}')
                same_words.append(nxt_word)
            elif word in nxt_word.lower():
                same_words.append(nxt_word)
        elif l == len(other_words)-1:   # проверим последнее слово
            words.append(other_words[start:l+1])
            if other_words[start:l+1].lower() in word:
                print(f'{root_word} содержит слово {nxt_word}')
                same_words.append(other_words[start:l+1])
            elif other_words[start:l+1].lower().count(word):
                same_words.append(other_words[start:l + 1])
            break
        else:
            l = l + 1
            continue
    print('Проверяемые слова:', words)

    l_other_words = ' ' + other_words.lower() + ' '
    n = l_other_words.count(word)  # количество совпадений, счетчик
#    s = l_other_words.count(' ')  # количество пробелов
    print("Проверочное слово: ",root_word)
    if n == 0:
        print('Однокоренных слов не встретилось')
    else:
        s = l_other_words.count(' ')  # количество пробелов
    return same_words

# Проверка
root_word = 'Лаг'
other_words = 'лагман лАгорифм ЛаГуна флагман лазурный'
print(type(other_words))
single_root_words(root_word, other_words)
print('Однокоренные слова:\n', *same_words)
print(' '+'~'*len(other_words))
