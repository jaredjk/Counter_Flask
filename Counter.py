from flask import Flask, render_template, request, redirect, session, flash, url_for
                                          
app = Flask(__name__)
app.secret_key = 'secret'

                                          
@app.route('/')                                                                                 
def index():
    if "counter" in session:
        session['counter'] += 1
    else :
        session['counter'] = 1
    return render_template('index.html')
app.run(debug=True)