
from flask import Flask, render_template
import os

app = Flask(__name__)

# Главная страница
@app.route('/')
def home():
    return render_template('index.html')

# Страница новостей
@app.route('/news')
def news():
    # Список новостей (можно потом вынести в базу данных)
    news_list = [
        {
            'id': 1,
            'title': 'Первая новость',
            'content': 'Краткое описание первой новости...',
            'image': 'news1.jpg',  # Фото должно быть в static/images/
            'date': '15.01.2025',
            'tags': ['Спорт', 'Мероприятие']
        },
        {
            'id': 2,
            'title': 'Вторая новость',
            'content': 'Краткое описание второй новости...',
            'image': 'news2.jpg',
            'date': '10.01.2025',
            'tags': ['Олимпиада', 'Наука']
        },
        {
            'id': 3,
            'title': 'Третья новость',
            'content': 'Краткое описание третьей новости...',
            'image': 'news3.jpg',
            'date': '05.01.2025',
            'tags': ['Экскурсия', 'Развлечения']
        }
    ]
    return render_template('news.html', news=news_list)

# Страница "О нас"
@app.route('/about')
def about():
    return render_template('about.html')

# Страница отдельной новости
@app.route('/news/<int:news_id>')
def news_detail(news_id):
    # Здесь можно сделать детальную страницу новости
    return f"Детальная страница новости {news_id}"

# Контактная форма
@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    # Здесь будет обработка формы
    return "Спасибо за сообщение!"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)