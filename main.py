from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
sl = {'title': 'Анкета',
      "surname": 'Watny',
      "name": 'Mark',
      "education": 'выше среднего',
      "profession": 'штурман марсохода',
      "sex": 'male',
      "motivation": "Всегда мечтал застрять на Марсе!",
      "ready": 'true'}


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    return render_template('auto_answer.html', title=sl['title'], surname=sl['surname'], name=sl['name'],
                           education=sl['education'], profession=sl["profession"], sex=sl['sex'],
                           motivation=sl["motivation"], ready=sl["ready"])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
