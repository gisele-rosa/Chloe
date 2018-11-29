import time
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
bot.sendMessage(477697050,"Olá, eu sou a Chloe e posso te ajudar a planejar sua viagem")
bot.sendMessage(477697050,"Escolha a operação",reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
        [InlineKeyboardButton(text="Conversão", callback_data='01')],
        [InlineKeyboardButton(text="Passagem Aerea", callback_data='02')],
        [InlineKeyboardButton(text="Sair...", callback_data='04')]
        ]))
bot.sendMessage(477697050,"Para conversão já digite o valor")

#INTERAÇÕES
#-----------------------recebendo msg-------------------------------------------------------
def recebendoMsg(msg):
 
    if('text' in msg):
        #----------------levantamento de exceções----------------------------------------------------------
        bot.sendMessage(477697050,"ok")
        global valor
        valor = msg['text']
        
    else:
        print(msg["data"])
        #----------------- opçao EUA dolar americano--------------------------
        if((msg["data"]=='01')):
            bot.sendMessage(477697050,"Escolha para qual moeda vc deseja converter: ?",reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
            [InlineKeyboardButton(text="Estados Unidos - Dólar Americano", callback_data='21')],
            [InlineKeyboardButton(text="Canadá - Dólar canadense", callback_data='22')],
            [InlineKeyboardButton(text="União Européia - Euro", callback_data='23')],
            [InlineKeyboardButton(text="Sair...", callback_data='24')]
            ]))
        else:  
        #---------------------opcao Estados Unidos-------------------------------
            if((msg["data"]=='21')):
                bot.sendMessage(477697050,"Certo, você escolheu Estados Unidos - Dólar Americano")
                moeda = "Estados Unidos - Dólar Americano"
                conversao(moeda,valor) 
       #---------------------opcao Canadá----------------------------------------     
            if((msg["data"]=='22')):
                bot.sendMessage(477697050,"Certo, você escolheu Canadá - Dólar canadense")
                moeda = "Canadá - Dólar canadense"
                conversao(moeda,valor)
        #---------------------opcao uniao europeia-------------------------------
            if((msg["data"]=='23')):
                bot.sendMessage(477697050,"Certo, você escolheu União Européia - Euro")
                moeda = "União Européia - Euro"
                conversao(moeda,valor)  
        #---------------------opçao sair--------------------------------------
            if(msg["data"]== "24"):
                bot.sendMessage(477697050,"saindo...")
                global w
                w = False
                sys.exit(0)

        #-------------------opcao canada dolar---------------------------------
        if((msg["data"]=='02')):
            bot.sendMessage(477697050,"Escolha para qual país viajar: ?",reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
            [InlineKeyboardButton(text="Estados Unidos", callback_data='31')],
            [InlineKeyboardButton(text="Canadá ", callback_data='32')],
            [InlineKeyboardButton(text="Europa", callback_data='33')],
            [InlineKeyboardButton(text="Sair...", callback_data='34')]
            ]))
        else:
      #---------------------opcao EUA----------------------------------------  
            if((msg["data"]=='31')):
                bot.sendMessage(477697050,"O preço da sua passagem para o EUA :")
                firefox = webdriver.Firefox()
                firefox.get('https://www.latam.com/pt_br/apps/personas/booking?fecha1_dia=31&fecha1_anomes=2018-12&auAvailability=1&ida_vuelta=ida&vuelos_origen=S%C3%A3o%20Paulo&from_city1=GRU&vuelos_destino=Nova%20York&to_city1=NYC&flex=1&vuelos_fecha_salida_ddmmaaaa=31/12/2018&cabina=Y&nadults=1&nchildren=0&ninfants=0')

                # o Sleep abaixo e para aguardar o carregamento da pagina
                time.sleep(5)

                #imprimir o resultado
                # armazenando a div que possui a tabela dentro da variavel dados

                dados = firefox.find_element_by_class_name('value')
                #print(dados)
                html = dados.get_attribute("innerHTML")
                soup = BeautifulSoup(html, 'html.parser')
                span = soup.find("span")

                bot.sendMessage(477697050,span.text) 
       #---------------------opcao Canadá----------------------------------------     
            if((msg["data"]=='32')):
                bot.sendMessage(477697050,"O preço da sua passagem para o Canadá :")
                firefox = webdriver.Firefox()
                firefox.get('https://www.latam.com/pt_br/apps/personas/booking?fecha1_dia=31&fecha1_anomes=2018-12&auAvailability=1&ida_vuelta=ida&vuelos_origen=S%C3%A3o%20Paulo&from_city1=GRU&vuelos_destino=Winnipeg&to_city1=YWG&flex=1&vuelos_fecha_salida_ddmmaaaa=31/12/2018&cabina=Y&nadults=1&nchildren=0&ninfants=0')

                # o Sleep abaixo e para aguardar o carregamento da pagina
                time.sleep(5)

                #imprimir o resultado
                # armazenando a div que possui a tabela dentro da variavel dados

                dados = firefox.find_element_by_class_name('value')
                #print(dados)
                html = dados.get_attribute("innerHTML")
                soup = BeautifulSoup(html, 'html.parser')
                span = soup.find("span")

                bot.sendMessage(477697050,span.text)
        #---------------------opcao uniao europeia-------------------------------
            if((msg["data"]=='33')):
                bot.sendMessage(477697050,"O preço da sua passagem para a União Européia")
                moeda = "União Européia - Euro"
                conversao(moeda,valor)
        #---------------------opcao uniao europeia-------------------------------
        if((msg["data"]=='34')):
            bot.sendMessage(477697050,"Certo, você escolheu União Européia - Euro")
            moeda = "União Européia - Euro"
            conversao(moeda,valor)  
    



        
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

