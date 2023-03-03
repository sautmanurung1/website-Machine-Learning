from app import app
from flask import Flask, render_template, url_for, redirect, session

@app.route('/')
def dashboard():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)