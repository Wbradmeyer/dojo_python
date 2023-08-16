from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def say_dojo():
    return 'Dojo!'

@app.route('/say/<string:title>')
def say_hi(title):
    caps_first_letter = title.capitalize()
    return f'Hi {caps_first_letter}!'

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    return f"{word * num}!"


if __name__=="__main__":
    app.run(debug=True)