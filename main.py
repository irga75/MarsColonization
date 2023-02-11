from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Миссия Колонизация Марса'


@app.route('/sample_page')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Первая HTML-страница</h1>
                  </body>
                </html>"""


@app.route('/promotion')
def return_advertisement():
    return f"""<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="utf-8">
        <title>Реклама. Колонизация марса</title>
    </head>
    <body>
        <aside><pre>
Человечество вырастает из детства.
Человечеству мала одна планета.
Мы сделаем обитаемыми безжизненные пока планеты.
И начнем с Марса!
Присоединяйся!
        </pre></aside>
    </body>"""


@app.route('/image_mars')
def return_image_mars():
    return f"""<!DOCTYPE html>
    <html lang="ru">
        <head>
            <meta charset="utf-8">
            <title>Привет, Марс!</title>
        </head>
        <body>
        <h1>Жди нас, Марс!</h1>
        <img src="{url_for('static', filename='img/mars.png')}" width="220" alt="Изображение Марса">
        <p>Вот она какая, красная планета.</p>
        </body>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
