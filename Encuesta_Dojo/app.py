from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['country'] = request.form['country']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']

        return redirect(url_for('result'))

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
