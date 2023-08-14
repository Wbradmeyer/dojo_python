from flask import Flask, render_template
app = Flask(__name__)

# This was a method presented during office hours tonight. I used it to guide this solution.

@app.route('/play', defaults = {'num' : 3, 'color' : 'light sky blue'})
@app.route('/play/<int:num>', defaults = {'color' : 'light sky blue'})
@app.route('/play/<int:num>/<string:color>')
def create_boxes(num, color):
    return render_template('index.html', num=num, color=color)


if __name__=="__main__":
    app.run(debug=True)