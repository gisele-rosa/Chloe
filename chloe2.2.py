import telegram
import telepot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Importar a classe Select
from selenium.webdriver.support.ui import Select
from telepot.namedtuple import ForceReply, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import requests
from bs4 import BeautifulSoup
import sys

bot=telepot.Bot("631366596:AAHW_HoLGDnOkKp2SmcIIoVr68J8d5t3-qo")

valor = 0

#-----------------limpando mensagens antigas do cache
updates = bot.getUpdates()

if updates:
    last_update_id = updates[-1]['update_id']
    bot.getUpdates(offset=last_update_id+1)

#msg inicial e msg com botoes
bot.sendMessage(477697050,"Olá, eu sou a Chloe faço conversões de moeda")
bot.sendMessage(477697050,"Entre com o valor que você deseja converter: ")

'''bot.sendMessage(477697050,"Em que posso ajudar?",reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
        [InlineKeyboardButton(text="Estados Unidos - Dólar Americano", callback_data='01')],
        [InlineKeyboardButton(text="Canadá - Dólar canadense", callback_data='02')],
        [InlineKeyboardButton(text="União Européia - Euro", callback_data='03')],
        [InlineKeyboardButton(text="Sair...", callback_data='04')]
        ]))'''


#INTERAÇÕES
def recebendoMsg(msg):
    #print(msg['text'])
    if('text' in msg):
        global valor
        valor = msg['text']
       
        bot.sendMessage(477697050,"Escolha para qual moeda vc deseja converter: ?",reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
        [InlineKeyboardButton(text="Estados Unidos - Dólar Americano", callback_data='01')],
        [InlineKeyboardButton(text="Canadá - Dólar canadense", callback_data='02')],
        [InlineKeyboardButton(text="União Européia - Euro", callback_data='03')],
        [InlineKeyboardButton(text="Sair...", callback_data='04')]
        ]))
    else:
        #----------------- opçao EUA dolar americano--------------------------
        if((msg["data"]=='01')):
            bot.sendMessage(477697050,"Certo, você escolheu Estados Unidos - Dólar Americano,")
            moeda = "Estados Unidos - Dólar Americano"
            conversao(moeda,valor)

        #-------------------opcao canada dolar---------------------------------
        if((msg["data"]=='02')):
            bot.sendMessage(477697050,"Certo, você escolheu Canadá - Dólar canadense")
            moeda = "Canadá - Dólar canadense"
            conversao(moeda,valor)
        #---------------------opcao uniao europeia-------------------------------
        if((msg["data"]=='03')):
            bot.sendMessage(477697050,"Certo, você escolheu União Européia - Euro")
            moeda = "União Européia - Euro"
            conversao(moeda,valor)  
        #---------------------opçao sair--------------------------------------
        if(msg["data"]== "04"):
                bot.sendMessage(477697050,"saindo...")
                global w
                w = False
                sys.exit(0)


        
def conversao(moeda,valor):        
        firefox = webdriver.Firefox()
        firefox.get('https://economia.uol.com.br/widgets/conversor-moedas/index.jhtm?first=conversor')

        # É preciso passar o elemento para a classe
        estados = Select(firefox.find_element_by_name('de'))

        # Selecionar a opção brasil
        estados.select_by_visible_text('Brasil - Real')

        # É preciso passar o elemento para a classe
        estados = Select(firefox.find_element_by_name('para'))

        # Selecionar a opção dollar
        estados.select_by_visible_text(moeda)

        # pegar o campo de conversao
        campo_busca = firefox.find_element_by_name('valor')

        # Digitar a quantia a ser convertida 
        campo_busca.send_keys(valor)

        # Simular que calcular seja precisonado
        consultar_btn = firefox.find_element_by_class_name("botao2")
        consultar_btn.click()

        #imprimir o resultado
        # armazenando a div que possui a tabela dentro da variavel dados
        dados = firefox.find_element_by_id("resultado")
        bot.sendMessage(477697050,"Resultado é :")
        bot.sendMessage(477697050,(dados.get_attribute('value')))
        
        


#ouvindo mensagens
bot.message_loop(recebendoMsg)
#bot.message_loop(conversao)

