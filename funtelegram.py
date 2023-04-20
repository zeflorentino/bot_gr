import gspread
import json
import requests
import os
from datetime import datetime, timedelta
from bs4 import BeautifulSoup as bs
from oauth2client.service_account import ServiceAccountCredentials

GOOGLE_SHEETS_CREDENTIALS = os.environ['GOOGLE_SHEETS_CREDENTIALS']
with open('credenciais.json', mode = "w") as arquivo:
 arquivo.write(GOOGLE_SHEETS_CREDENTIALS)
conta = ServiceAccountCredentials.from_json_keyfile_name('credenciais.json')
 
api = gspread.authorize(conta)
planilha = api.open_by_key("16sUMF5oixWfKfRAWzcvy_brPqgUanVwiHz_UGk72rQw")
registros = planilha.worksheet("registros")
cadastrados = planilha.worksheet("cadastrados")
token = os.environ["TELEGRAM_API_KEY"]

def escreve(link):
  requisicao = requests.get(link)
  html = bs(requisicao.content)
  titulo = html.findAll('h1',{'class':'content-head__title'})[0]
  titulo = titulo.text
  linhafina = html.findAll('p',{'class':'feed-post-body-resumo'})[0]
  linhafina = linhafina.text

  mensagem = f"""
  &#x1F331; <strong>{titulo}</strong><br><br>

  {linhafina}<br><br>

  &#x1F4F0; <a href = {link}><strong>LEIA AQUI.</strong></a>
  """
  lista_cadastros = cadastrados.get_all_values()

  for x in lista_cadastros:
    chat_id_resposta = x[3]
    nova_mensagem = {"chat_id": chat_id_resposta, "text": mensagem, "parse_mode" : 'HTML'}
    requests.post(f"https://api.telegram.org./bot{token}/sendMessage", data = nova_mensagem)
  return "Enviado."
