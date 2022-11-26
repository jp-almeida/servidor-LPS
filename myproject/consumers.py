import json
from channels.generic.websocket import WebsocketConsumer

class TableConsumer(WebsocketConsumer):
  def connect(self):
    self.accept()

    self.send(text_data=json.dumps({
      'type':'connection_estabilished',
      'message':'Conectou!'
    }))
  
  def receive(self, text_data):
    text_data_json = json.loads(text_data)
    valor = text_data_json['valor']

    print('valor: ', valor)

    self.send(text_data=json.dumps({
      'type':'lance',
      'valor': valor
    }))