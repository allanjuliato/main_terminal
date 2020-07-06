# # import music_rain as music

# # def print_teste():
# #     print('Dentro')

# # class Teste_1:

# #     def __init__(self):
# #         print('123')
# #         print_teste()

# # seila = 0

# # if __name__ == "__main__":
# #     teste = Teste_1()
# #     # chuva1 = music.Chuva()
# #     # chuva1.running()
# #     if seila == 1:
# #         chuva1 = music.Chuva()
# #         chuva1.running()

# import datetime

# seila = 100

# pr = str(datetime.timedelta(seconds=seila))

# print(pr)

# def hms(seconds):
#     m = seconds % 3600 // 60
#     s = seconds % 3600 % 60
#     return f'{m:02d}:{s:02d}'

# print(hms(100))  # Should print 02h05m00s

# for i in range(10):
#     pass
# else:
#     print(1)


#Código adaptado para Python 3

#!/usr/bin/python

from datetime import datetime, timedelta
from sys import stdout
from time import sleep

print(' Cronometro regressivo | programador => mmxm')
segundos = int(input('Digite a quantidade de segundos: '))
tempo = timedelta(seconds=segundos)
print('\n')

while (str(tempo) != '0:00:00'):
    stdout.write("\r%s"%tempo)
    stdout.flush()
    tempo = tempo - timedelta(seconds=1)
    sleep(1)

stdout.write("\r0:00:00")
stdout.flush()

print('\a') # => sinal sonoro , pelo menos comigo funcionou '-'
