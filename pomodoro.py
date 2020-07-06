#!/usr/bin/python

"""
Fazer:
Colocar o alarme de mudança de status
Colocar o registro de numero de Pomodoros realizados(Pensar se vai ser diario ou por vezes sem parar)
"""

from datetime import datetime, timedelta
from sys import stdout
from time import sleep
import os

def cronometro(tempo, status):
    tempo = timedelta(seconds=tempo)
    while (str(tempo) != '0:00:00'):
        stdout.write("\r%s"%tempo)
        stdout.write(status)
        
        stdout.flush()
        tempo = tempo - timedelta(seconds=1)
        sleep(1)

    stdout.write("\r0:00:00")
    stdout.flush()

class Pomodoro:
    def __init__(self):
        print('\n')
        pomodoro = 1
        while True:
            try:
                os.system('clear')
                print('TESTE')
                if pomodoro == 1:
                    cronometro(10, " - Você está em Pomodoro\r")
                    pomodoro = 0
                else:
                    cronometro(5, " - Você está em Pausa\r")
                    pomodoro = 1
            except KeyboardInterrupt:
                os.system('clear')
                break

if __name__ == "__main__":
    pomo = Pomodoro()




