from flask import Flask, render_template

from data.forms import LoginForm

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


@app.route('/answer')
@app.route("/auto_answer")
def answer():
    data = {
        'title': 'Анкета',
        'surname': 'Watny',
        'name': 'Mark',
        'education': 'выше среднего',
        'profession': 'штурман марсохода',
        'sex': 'male',
        'motivation': 'Всегда мечтал застрять на Марсе',
        'ready': 'True'
    }
    return render_template('auto_answer.html', **data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return render_template('success.html', title='Успешно')
    return render_template('login.html', title='Аварийный доступ', form=form)


@app.route('/distribution')
def distribution():
    astronauts = ["Ридли Скотт", "Энди Уир", "Марк Уотни", "Венката Капур", "Тедди Сандерс", "Шон Бин"]
    return render_template('distribution.html', title='Размещение по каютам', astronauts=astronauts)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
