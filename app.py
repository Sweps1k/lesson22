from flask import Flask

app = Flask(__name__)
# 1
@app.route('/')
def home():
    return "Вітаю це головна сторінка мого сервера"

@app.route('/about')
def about():
    return "Я початковий розробник вивчаю пайтон і веб розробку"

@app.route('/skills')
def skills():
    return "знаю python flask html css трохи баз даних"

@app.route('/contact')
def contact():
    return "телеграм для звязку dev_user або пошта mymail@gmail.com"

# 2
@app.route('/temperature/<int:t>')
def temperature(t):
    if t < 0:
        return "Мороз"
    elif 0 <= t <= 20:
        return "Прохолодно"
    elif 20 < t < 30:
        return "Тепло"
    else:
        return "Спека"


# 3
@app.route('/math/<operation>/<int:a>/<int:b>')
def calculate(operation, a, b):
    if operation == 'add':
        return str(a + b)
    elif operation == 'sub':
        return str(a - b)
    elif operation == 'mul':
        return str(a * b)
    elif operation == 'div':
        if b == 0:
            return "на нуль ділити не можна"
        return str(a / b)
    else:
        return "невідома операція"


if __name__ == '__main__':
    app.run(debug=True)
