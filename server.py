from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'Totallysecretkey'

@app.route('/')

def index():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 1
    return render_template('index.html')

@app.route('/increment', methods=['POST'])

def increment():
    session['count'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])

def reset():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)