import pyautogui
import time
import random

# Lista de mensajes aleatorios
mensajes = [
    "Estoy abierto a recibir todo lo bueno que el universo tiene para ofrecerme."
    "Hoy es un día perfecto para manifestar tus sueños más grandes. 🌟✨",
    "Cada pensamiento positivo te acerca a lo que deseas. 💭💖",
    "La cadena de eventos positivos comienza con tu actitud. 🔗😊",
    "Estoy atrayendo abundancia y prosperidad en mi vida. 💰🍀",
    "Mis sueños se están haciendo realidad uno a uno. 🌠🎯",
    "Estoy alineado con el universo y su energía positiva. 🌌🔮",
    "Todo lo que deseo se manifiesta en mi vida con facilidad. 🌈🙏",
    "Cada día es una nueva oportunidad para atraer lo que merezco. ☀️🌸",
    "Estoy rodeado de amor y buenas vibraciones. ❤️✨",
    "La gratitud abre las puertas a la manifestación de mis sueños. 🚪🌠",
    "Confío en el proceso del universo para traerme lo mejor. 🌍💫",
    "Estoy en el camino correcto hacia mis metas. 🛤️🏆",
    "Mis pensamientos positivos crean mi realidad positiva. 💭🌟",
    "Estoy agradecido por todas las bendiciones que recibo. 🙏🍀",
    "Estoy en sintonía con la energía del éxito y la prosperidad. 🎯💸",
    "La cadena de eventos maravillosos comienza hoy. 🌈😊",
    "Creo en mi capacidad para atraer lo mejor a mi vida. 💪🌟",
    "Estoy creando una vida llena de felicidad y éxito. 🌞🏆",
    "Cada día me acerco más a mis objetivos. 📅🎯",
    "Estoy abierto a recibir todo lo bueno que el universo tiene para ofrecerme. 🌌✨",
    "Mi corazón está lleno de gratitud y alegría. 💖😊",
    "La abundancia fluye hacia mí de todas partes. 💵🌊",
    "El universo está conspirando a mi favor. 🌠🌍",
    "Estoy en armonía con el flujo de la vida. 🌊🔄",
    "Mis pensamientos y emociones son poderosos. 💭💪",
    "La energía positiva me rodea siempre. 🌟🔮",
    "Estoy viviendo la mejor versión de mi vida. 🌈🌟",
    "Mi vida está llena de amor y felicidad. ❤️😊",
    "Atraigo lo que pienso y siento. 💭💖",
    "Todo lo que deseo se manifiesta en el momento perfecto. ⏳🌠"
]

def enviar_mensaje_aleatorio():

    mensaje = random.choice(mensajes)

    pyautogui.write(mensaje)

    pyautogui.press('enter')

print("Tienes 5 segundos para seleccionar la caja de texto...")
time.sleep(5)

# coldown message
while True:
    enviar_mensaje_aleatorio()
    time.sleep(3)
