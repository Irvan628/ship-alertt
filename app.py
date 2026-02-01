from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def landing():
    # Menggantikan view('landing') di Laravel
    return render_template('landing.html')

@app.route('/dashboard')
def dashboard():
    # Menggantikan view('dashboard') di Laravel
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)