import logging
from typing import List
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
logging.basicConfig(level=logging.INFO)
bot = ChatBot('Bot')

conv: List[str] = (['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 'Você gosta de programar?', 'Sim, eu programo em Python'])

bot.set_trainer(ListTrainer)
bot.train(conv)

while True:
        pergunta = input("Usuário: ")
        resposta = bot.get_response(pergunta)
        if float(resposta.confidence) > 0.5:
                print("TW Bot: ", resposta)
        else:
                print('TW Bot: Ainda não sei responder esta pergunta')