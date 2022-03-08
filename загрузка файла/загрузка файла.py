from flask import Flask, url_for, render_template
from waitress import serve

app = Flask(__name__)


@app.route('/')
def greeting_page():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index_page():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def pr_page():
    li = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
          'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '<br>'.join(li)


@app.route('/image_mars')
def img_page():
    return f'''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Привет, Марс!</title>
        </head>
        <body>
            <h1>Жди нас, Марс!</h1>
            <figure>
                <img src="{url_for('static', filename='img/mars.gif')}" alt="oops!">
                <figcaption>Вот она какая - красная планета!</figcaption>
            </figure>  
        </body>
        </html>'''


@app.route('/carousel')
def peizazh_page():
    return f'''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
            <link rel="stylesheet" href="static/css/style.css">
            <title>Привет, Марс!</title>
        </head>
        <body>
            <h1>Жди нас, Марс!</h1>
            <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
              <div class="carousel-inner">
                <div class="carousel-item active first">
                  <img src="static/img/1.jpg" class="d-block w-100 data-bs-interval="2" alt="...">
                </div>
                <div class="carousel-item second">
                  <img src="static/img/2.jpg" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item third">
                  <img src="static/img/3.jpg" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item fourth">
                  <img src="static/img/4.jpg" class="d-block w-100" alt="...">
                </div>
              </div>
            </div>
        </body>
        </html>'''


@app.route('/load_photo', methods=['GET', 'POST'])
def load_photo():
    return render_template('load_photo.html')


if __name__ == '__main__':
    #app.run('127.0.0.1', 8080)
    serve(app, host='0.0.0.0', port=5000)