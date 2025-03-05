from flask import Flask, render_template, request, redirect, url_for
from utils.text_analysis import analyze_text, generate_wordcloud
from utils.logger import setup_logger
import os

# Инициализация Flask-приложения
app = Flask(__name__)

# Настройка логгера
logger = setup_logger()

@app.route("/", methods=["GET", "POST"])
def index():
    """Главная страница приложения."""
    if request.method == "POST":
        text = request.form.get("text")
        if text:
            logger.info("Получен текст для анализа.")
            # Анализ текста
            stats = analyze_text(text)
            # Генерация облака тегов
            wordcloud_path = generate_wordcloud(text)
            return render_template("result.html", stats=stats, wordcloud_path=wordcloud_path)
        else:
            logger.warning("Текст не был введен.")
            return redirect(url_for("index"))
    return render_template("index.html")

if __name__ == "__main__":
    # Создание папки для логов, если её нет
    if not os.path.exists("logs"):
        os.makedirs("logs")
    # Запуск приложения
    app.run(debug=True)