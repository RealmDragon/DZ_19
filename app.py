from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    statuses = [
        {'name': 'Новый', 'color': 'blue'},
        {'name': 'Обработка', 'color': 'yellow'},
        {'name': 'Обработан', 'color': 'green'},
        {'name': 'Отмена', 'color': 'red'},
    ]
    return render_template('index.html', statuses=statuses)

if __name__ == '__main__':
    app.run(debug=True)