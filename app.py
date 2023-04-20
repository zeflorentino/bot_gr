from flask import Flask, request, render_template
import json
import requests
import os
from datetime import datetime, timedelta
import pandas as pd

from funtelegram import escreve

app = Flask(__name__)

@app.route('/')
def ficha():
  return render_template('index.html')

@app.route('/enviado', methods=['POST'])
def resultado():
  link = str(request.form['link'])
  escreve(link)
  return 'Enviado.'