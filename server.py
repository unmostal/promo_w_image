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


@app.route('/promotion_image')
def promo_with_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1 class="text-danger">Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/MARS.png')}"style="width:270px; height: 250px">
                            <div class="d-flex justify-items-end alert alert-dark" role="alert">
                                <h2>Человечество вырастает из детства.</h2>
                            </div>
                            <div class="d-flex justify-items-end alert alert-success" role="alert">
                                <h2>Человечеству мала одна планета.</h2>
                            </div>
                            <div class="d-flex justify-items-end alert alert-secondary" role="alert">
                                <h2>И сделаем мы обитаемыми безжизненные пока планеты.</h2>
                            </div>
                            <div class="d-flex justify-items-end alert alert-warning" role="alert">
                                <h2>И начнем с Марса!</h2>
                            </div>
                            <div class="d-flex justify-items-end alert alert-danger" role="alert">
                                <h2>Присоединяйся!</h2>
                            </div>
                            
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
