from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return f"{celsius} degrees Celsius = {fahrenheit} degrees Fahrenheit"


@app.route('/f')
@app.route('/f/<celsius>')
def f(celsius=float()):
    return str(convert_celsius_to_fahrenheit(float(celsius)))


if __name__ == '__main__':
    app.run()
