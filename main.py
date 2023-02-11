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


@app.route('/promotion_image')
def return_promotion_image():
    return f"""<!DOCTYPE html>
    <html lang="ru">
        <head>
            <meta charset="utf-8">
            <meta name="viewpoint" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet"
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
            crossorigin="anonymous">
            <link rel="stylesheet"
            href="{url_for('static', filename='css/style.css')}">
            <title>Колонизация</title>
        </head>
        <body>
            <h1>Жди нас, Марс!</h1>
            <img src="{url_for('static', filename='img/mars.png')}" width="220" alt="Изображение Марса">
            <div class="p-3 mb-2 bg-warning text-dark">Человечество вырастает из детства.</div>
            <div class="p-3 mb-2 bg-info text-dark">Человечеству мала одна планета.</div>
            <div class="p-3 mb-2 bg-danger text-white">Мы сделаем обитаемыми безжизненные пока планеты.</div>
            <div class="p-3 mb-2 bg-success text-white">И начнем с Марса!</div>
            <div class="p-3 mb-2 bg-primary text-white">Присоединяйся!</div>
        </body>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
