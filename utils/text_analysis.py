from collections import Counter
import nltk
from wordcloud import WordCloud

# Загрузка ресурсов NLTK
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")


def filter_words(text):
    """
    Фильтрует слова, оставляя только существительные, прилагательные и наречия.
    :param text: Входной текст.
    :return: Список отфильтрованных слов.
    """
    # Токенизация текста
    words = nltk.word_tokenize(text)

    # POS-тегирование (определение частей речи)
    pos_tags = nltk.pos_tag(words)

    # Фильтрация слов
    filtered_words = [
        word for word, pos in pos_tags
        if pos.startswith("NN")  # Существительные
           or pos.startswith("JJ")  # Прилагательные
           or pos.startswith("RB")  # Наречия
    ]

    return filtered_words


def analyze_text(text):
    """
    Анализирует текст и возвращает статистику.
    :param text: Входной текст.
    :return: Словарь с результатами анализа.
    """
    # Фильтрация слов
    filtered_words = filter_words(text)

    # Подсчет количества символов (без учета пробелов и знаков препинания)
    char_count = len("".join(filtered_words))

    # Подсчет количества слов
    word_count = len(filtered_words)

    # Подсчет частоты слов
    word_freq = Counter(filtered_words)

    return {
        "char_count": char_count,
        "word_count": word_count,
        "word_freq": word_freq.most_common(10),  # Топ-10 слов
    }


def generate_wordcloud(text):
    """
    Генерирует облако тегов из текста и сохраняет его в файл.
    :param text: Входной текст.
    :return: Путь к файлу с облаком тегов.
    """
    # Фильтрация слов
    filtered_words = filter_words(text)
    filtered_text = " ".join(filtered_words)

    # Генерация облака тегов
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(filtered_text)
    wordcloud_path = "static/wordcloud.png"
    wordcloud.to_file(wordcloud_path)
    return wordcloud_path