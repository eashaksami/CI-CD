from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return {
        'msg': 'Hello',
        'app_version': '1'
    }

@app.route('/add/<a>/<b>')
def add_route(a, b):
    return {
        'result': add(a, b)
    }

def add(a,b):
    if type(a) == str and not a.isdigit():
        return "Invalid Input"

    if type(b) == str and not b.isdigit():
        return "Invalid Input"

    a = int(a)
    b = int(b)
    return a + b


@app.route('/subtract/<a>/<b>')
def remove_route(a, b):
    return {
        'result': subtract(a, b)
    }

# Input can be both strings and digits
def subtract(a,b):
    if type(a) == str and not a.isdigit():
        return "Invalid Input"

    if type(b) == str and not b.isdigit():
        return "Invalid Input"

    a = int(a)
    b = int(b)
    return a - b

@app.route('/multiply/<a>/<b>')
def multiply_route(a, b):
    return {
        'result': multiply(a, b)
    }

# Input can be both strings and digits
def multiply(a,b):
    if type(a) == str and not a.isdigit():
        return "Invalid Input"

    if type(b) == str and not b.isdigit():
        return "Invalid Input"

    a = int(a)
    b = int(b)
    return a * b

@app.route('/divide/<a>/<b>')
def divide_route(a, b):
    return {
        'result': divide(a, b)
    }

# Input can be both strings and digits
def divide(a,b):
    if type(a) == str and not a.isdigit():
        return "Invalid Input"

    if type(b) == str and not b.isdigit():
        return "Invalid Input"

    a = int(a)
    b = int(b)
    return a / b

if __name__ == "__main__":
    app.run()
