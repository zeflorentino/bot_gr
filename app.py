from flask import Flask, request, render_template

from funtelegram import escreve

app = Flask(__name__)

@app.route('/')
def ficha():
  return render_template('index.html')

@app.route('/enviado', methods=['POST'])
def resultado():
  link = request.form['link']
  escreve(link)
  return 'Enviado.'
