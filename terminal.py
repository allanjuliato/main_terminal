import os
import music_rain
import pomodoro



def chama_ana():
    os.system('clear')
    print("""
    __    _  _    __      ___  ___   _   ___ 
   /__\  ( \( )  /__\    (__ )(__ ) / ) | __)
  /(__)\  )  (  /(__)\    (_ \ (_ \/ _ \|__ \ 
 (__)(__)(_)\_)(__)(__)  (___/(___/\___/(___/
""")

while True:
    chama_ana()
    command = input('> ')

    if command.lower() == 'chuva':
        chuva = music_rain.Chuva()
        chuva.running()
    if command.lower() == 'pomodoro':
        pomo = pomodoro.Pomodoro()
    if command.lower() == 'exit' or command.lower() == 'quit':
        os.system('clear')
        break