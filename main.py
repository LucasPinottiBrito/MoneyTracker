from flask import Flask, render_template, request
import flaskwebgui
import sqlite3
# import time
# from datetime import datetime

app = Flask(__name__)

def getSaldo():
      db = sqlite3.connect('moneySpend.db')
      print(db)
      cr = db.cursor()
      cr.execute("SELECT saldo FROM money_status WHERE credito=0")
      saldo = cr.fetchone()[0]
      saldo = str(saldo)
      print("saldo: ", saldo)
      cr.close()
      return saldo
 

gui = flaskwebgui.FlaskUI(app=app, fullscreen=False, server="flask")
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/saldo')
def saldo():
      return getSaldo()
      

if __name__ == '__main__':
        gui.run()