from flask import Flask, render_template, request
import flaskwebgui
# import sqlite3
# import time
# from datetime import datetime

app = Flask(__name__)

gui = flaskwebgui.FlaskUI(app=app, fullscreen=False, server="flask")
@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
        gui.run()