from flask import Flask, render_template, redirect
# from forms.loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Заготовка')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
