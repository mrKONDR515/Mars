from flask import Flask, render_template, redirect

# from forms.loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Заготовка')


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<type>')
def list_prof(type):
    prof = ["инженер-исследователь", "пилот", "строитель", "экзобиолог", "врач"]
    return render_template('list_prof.html', type=type, prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
