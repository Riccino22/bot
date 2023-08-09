import telebot
from bs4 import BeautifulSoup
import requests
import numpy as np




r = requests.get("http://monitordolarvenezuela.com/")
soup = BeautifulSoup(r.text, "html.parser")
price = soup.find_all("p")

imgs = soup.find_all("img")
img = "http://monitordolarvenezuela.com/" + imgs[24]["src"]
print(img)
v = 0
for i in imgs:
    print(v)
    print(i["src"])
    v += 1
response = requests.get(img)
open('image.jpg', 'wb').write(response.content)


dolarBCV = price[1].text.replace("Bs = ", "")
dolarBCV = float(dolarBCV.replace(",", "."))
dolarParalelo3 = price[2].text.replace("Bs = ", "")
dolarParalelo3 = float(dolarParalelo3.replace(",", "."))
dolarToday = price[3].text.replace("Bs = ", "")
dolarToday = float(dolarToday.replace(",", "."))
dolarMonitor = price[4].text.replace("Bs = ", "")
dolarMonitor = float(dolarMonitor.replace(",", "."))
dolarParaleloVip = price[5].text.replace("Bs = ", "")
dolarParaleloVip = float(dolarParaleloVip.replace(",", "."))
dolarBinance = price[6].text.replace("Bs = ", "")
dolarBinance = float(dolarBinance.replace(",", "."))
money = [
    dolarBCV,
    dolarParalelo3,
    dolarToday,
    dolarMonitor,
    dolarParaleloVip,
    dolarBinance
]


def moneyValues():

    r = requests.get("http://monitordolarvenezuela.com/")
    soup = BeautifulSoup(r.text, "html.parser")
    price = soup.find_all("p")

    dolarBCV = price[1].text.replace("Bs = ", "")
    dolarBCV = float(dolarBCV.replace(",", "."))

    dolarParalelo3 = price[2].text.replace("Bs = ", "")
    dolarParalelo3 = float(dolarParalelo3.replace(",", "."))

    dolarToday = price[3].text.replace("Bs = ", "")
    dolarToday = float(dolarToday.replace(",", "."))

    dolarMonitor = price[4].text.replace("Bs = ", "")
    dolarMonitor = float(dolarMonitor.replace(",", "."))

    dolarParaleloVip = price[5].text.replace("Bs = ", "")
    dolarParaleloVip = float(dolarParaleloVip.replace(",", "."))

    dolarBinance = price[6].text.replace("Bs = ", "")
    dolarBinance = float(dolarBinance.replace(",", "."))

    imgs = soup.find_all("img")
    img = "http://monitordolarvenezuela.com/" + imgs[24]["src"]
    response = requests.get(img)
    open('image.jpg', 'wb').write(response.content)

    money = [
        dolarParalelo3,
        dolarToday,
        dolarMonitor,
        dolarParaleloVip,
        dolarBinance
    ]


# print(price[2:7])


def env(msg, dolar):
    bot.reply_to(msg, str(float(msg.text) / dolar) + "$")


def rec(msg, command, dolar, dolarType):
    if msg.text == "/" + command:
        bot.reply_to(msg, "El " + dolarType + " se encuentra en *" +
                     str(dolar) + "$*", parse_mode="Markdown")
    else:
        bot.reply_to(msg, (msg.text.replace("/" + command, "") + " Bs. equivale a *" + str(float(
            (msg.text.replace("/" + command, ""))) / dolar) + "$* por el " + dolarType), parse_mode="Markdown")


def config(msg, dType, d):
    print()


dolarSelect = {}

bot = telebot.TeleBot("6199806449:AAFqHu25WaeLwZEznQyvjT52fAJSnEKdJ3E")


@bot.message_handler(commands=["start"])
def enviar(msg):
    moneyValues()
    chat_id = msg.chat.id
    # print("- @" + msg.from_user.username)
    # print(chat_id)
    photo = open('image.jpg', 'rb')
    bot.send_photo(chat_id, photo)
    bot.reply_to(
        msg,
        f"""

        Bienvenido a Bolivares Bot by @ricc_ino

- Conversion a Dolar BCV ( -- {dolarBCV} Bs. -- ): /bcv + El monto en Bs.

- Conversion a paralelo 3 ( -- {dolarParalelo3} Bs. -- ): /p3 + El monto en Bs.

- Conversion a Dolar Paralelo VIP ( -- {dolarParaleloVip} Bs. -- ): /pvip + el monto en Bs. 

- Conversion a binance ( -- {dolarBinance} Bs. -- ): /bin + El monto en Bs.

- Conversion a Dolar Today ( -- {dolarToday} Bs. -- ): /dtoday + el monto en Bs.  

- Conversion a Monitor Dolar ( -- {dolarMonitor} Bs. -- ): /md + el monto en Bs.    
        """
    )


def send_msg(c, d, dType):
    @bot.message_handler(commands=[c])
    def enviarBin(msg):
        chat_id = msg.chat.id
        rec(msg=msg, command=c, dolar=d, dolarType=dType)


send_msg(dType="Dolar BCV", c="bcv", d=dolarBCV)
send_msg(dType="Dolar Binance", c="bin", d=dolarBinance)
send_msg(dType="Dolar Paralelo 3", c="p3", d=dolarParalelo3)
send_msg(dType="Dolar Paralelo VIP", c="pvip", d=dolarParaleloVip)
send_msg(dType="Dolar Today", c="dtoday", d=dolarToday)
send_msg(dType="Monitor Dolar", c="md", d=dolarMonitor)


# Define una función que se ejecuta cuando el usuario envía el comando "/price"
@bot.message_handler(commands=["price"])
def env(msg):
    # Crea una lista vacía para almacenar los precios
    prices = []
    # Realiza una solicitud GET a la URL de Mercado Libre que se proporciona en el mensaje del usuario
    r = requests.get("http://listado.mercadolibre.com.ve/" +
                     msg.text.replace("/price ", ""))
    # Analiza el HTML de la página utilizando la biblioteca BeautifulSoup
    soup = BeautifulSoup(r.text, "html.parser")
    # Encuentra todos los elementos HTML que tienen la clase CSS "price-tag-fraction"
    priceML = soup.find_all("span", {'class': 'price-tag-fraction'})
    # Inicializa un contador para imprimir los precios en la consola
    a = 0
    # Itera sobre cada elemento HTML encontrado y extrae el precio
    for item in priceML:
        # Imprime el precio en la consola
        print("\n--- " + str(a) + ":")
        print(item.text)
        # Incrementa el contador
        a += 1
        # Agrega el precio a la lista de precios
        prices.append(int(item.text.replace(".", "")))
    # Imprime la lista de precios en la consola

    print("http://listado.mercadolibre.com.ve/" +
          msg.text.replace("/price ", ""))
    # Envía la lista de precios como respuesta al usuario
    a = 1
    listaPreciosStr = ""

    for item in prices:
        listaPreciosStr += str(a) + "-- " + str(item) + "$ \n"
        a += 1

    promedio = round((sum(prices) / len(prices)), 2)
    # listaPreciosStr += "\nPromedio: " + str(promedio) + "$"
    bot.reply_to(msg, "\nPromedio: " + str(promedio) + "$")

# Define una función que se ejecuta cuando el usuario envía el comando "/price"


@bot.message_handler(commands=["list"])
def env(msg):
    # Crea una lista vacía para almacenar los precios
    prices = []
    # Realiza una solicitud GET a la URL de Mercado Libre que se proporciona en el mensaje del usuario
    r = requests.get("http://listado.mercadolibre.com.ve/" +
                     msg.text.replace("/list ", ""))
    # Analiza el HTML de la página utilizando la biblioteca BeautifulSoup
    soup = BeautifulSoup(r.text, "html.parser")
    # Encuentra todos los elementos HTML que tienen la clase CSS "price-tag-fraction"
    priceML = soup.find_all("span", {'class': 'price-tag-fraction'})
    # Inicializa un contador para imprimir los precios en la consola
    a = 0
    # Itera sobre cada elemento HTML encontrado y extrae el precio
    for item in priceML:
        # Imprime el precio en la consola
        print("\n--- " + str(a) + ":")
        print(item.text)
        # Incrementa el contador
        a += 1
        # Agrega el precio a la lista de precios
        prices.append(int(item.text.replace(".", "")))
    # Imprime la lista de precios en la consola

    print("http://listado.mercadolibre.com.ve/" +
          msg.text.replace("/list ", ""))
    # Envía la lista de precios como respuesta al usuario
    a = 1
    listaPreciosStr = ""

    for item in prices:
        listaPreciosStr += str(a) + "-- " + str(item) + "$ \n"
        a += 1

    promedio = round((sum(prices) / len(prices)), 2)
    # listaPreciosStr += "\nPromedio: " + str(promedio) + "$"
    bot.reply_to(msg, listaPreciosStr)


bot.polling()
