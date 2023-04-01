from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def name():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promo():
    return 'Человечество вырастает из детства.<br> Человечеству мала одна планета.<br> Мы сделаем' \
           ' обитаемыми безжизненные пока планеты.<br> И начнем с Марса!<br> Присоединяйся!'

@app.route('/image_mars')
def show_mars():
    return f'''
    <title>Привет, Марс!</title>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/MARS.png')}"style="width:270px; height: 250px">
    <p>Вот она какая, красная планета!</p>  '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
