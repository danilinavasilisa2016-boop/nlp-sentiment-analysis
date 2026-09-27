import string
positive_words = {
    'отличная', 'отличный', 'отлично', 'прекрасно', 'прекрасный', 'хорошо',
    'хороший', 'удобно', 'удобный', 'быстро', 'быстрый', 'исправно',
    'рекомендую', 'рабочий', 'работает', 'проверено', 'проблем_нет',
    'нравится', 'качественный', 'качество', 'доволен', 'супер', 'идеально',
    'надежный', 'надежно', 'довольна', 'понравился', 'понравилось'
}

negative_words = {
    'сожжет', 'сжег', 'нерабочий', 'не_работает', 'ошибка', 'ошибки', 'брак',
    'проблема', 'проблемы', 'перезагрузку', 'перезагружается', 'не_позволяет',
    'отваливается', 'отвалился', 'минус', 'плохо', 'плохой', 'ужасно',
    'ужасный', 'разочарован', 'разочарование', 'сломался', 'сломался',
    'не_нравится', 'вернул', 'возврат', 'обман', 'развод', 'дорого'
}

def clean_and_split(text):
    """Очистка текста от пунктуации и разделение на слова"""
    text = text.lower()
    # Обработка устойчивых словосочетаний
    text = text.replace("проблем нет", "проблем_нет")
    text = text.replace("не позволяет", "не_позволяет")
    text = text.replace("не работает", "не_работает")
    text = text.replace("не нравится", "не_нравится")
    # Дефисы заменяем на пробел, чтобы "не-рабочий" -> "не рабочий"
    text = text.replace("-", " ")
    # Удаляем пунктуацию
    for p in string.punctuation + "«»—":
        text = text.replace(p, " ")
    return text.split()

def analyze_review(review_text):
    words = clean_and_split(review_text)

    pos_list = []
    neg_list = []
    neu_list = []

    for word in words:
        if len(word) <= 2 and word not in ['ок']:
            continue

        if word in positive_words:
            pos_list.append(word)
        elif word in negative_words:
            neg_list.append(word)
        else:
            neu_list.append(word)

    pos_list = sorted(list(set(pos_list)))
    neg_list = sorted(list(set(neg_list)))
    neu_list = sorted(list(set(neu_list)))

    # Определение общей оценки
    if len(pos_list) > len(neg_list):
        rating = "Положительный"
    elif len(neg_list) > len(pos_list):
        rating = "Отрицательный"
    else:
        rating = "Нейтральный"

    return pos_list, neg_list, neu_list, rating

def main():
    while True:
        review = input("\nВведите отзыв для анализа : ").strip()
        if review.lower() == 'выход':
            print("Программа завершена.")
            break
        if not review:
            print("Отзыв не может быть пустым.")
            continue

        pos, neg, neu, rating = analyze_review(review)

        print(f"Положительные характеристики: {', '.join(pos) if pos else 'нет'}")
        print(f"Отрицательные характеристики: {', '.join(neg) if neg else 'нет'}")
        print(f"Нейтральные характеристики: {', '.join(neu) if neu else 'нет'}")
        print(f"Общая оценка: {rating}")

if __name__ == "__main__":
    main()