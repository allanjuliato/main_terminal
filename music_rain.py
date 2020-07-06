import pygame
from pygame import mixer
from pygame import font
from pygame.locals import *
from time import sleep

class Chuva:
      
    def running(self):
        # initialize game engine
        pygame.init()
        mixer.init()

        mixer.music.load('./sound/chuva.mp3')
        mixer.music.play()

        #Tamanho da Tela
        window_width=1100
        window_height=700

        # Open a window
        size = (window_width, window_height)
        screen = pygame.display.set_mode(size)

        # Set title to the window
        pygame.display.set_caption("Music Rain")

        rain_image0 = pygame.image.load('./imagens/frame_00_delay.jpg')
        rain_image1 = pygame.image.load('./imagens/frame_01_delay.jpg')
        rain_image2 = pygame.image.load('./imagens/frame_02_delay.jpg')
        rain_image3 = pygame.image.load('./imagens/frame_03_delay.jpg')
        rain_image4 = pygame.image.load('./imagens/frame_04_delay.jpg')
        rain_image5 = pygame.image.load('./imagens/frame_05_delay.jpg')
        rain_image6 = pygame.image.load('./imagens/frame_06_delay.jpg')
        rain_image7 = pygame.image.load('./imagens/frame_07_delay.jpg')
        rain_image8 = pygame.image.load('./imagens/frame_08_delay.jpg')
        rain_image9 = pygame.image.load('./imagens/frame_09_delay.jpg')
        rain_image10 = pygame.image.load('./imagens/frame_10_delay.jpg')
        rain_image11 = pygame.image.load('./imagens/frame_11_delay.jpg')
        rain_image12 = pygame.image.load('./imagens/frame_12_delay.jpg')
        rain_image13 = pygame.image.load('./imagens/frame_13_delay.jpg')
        rain_image14 = pygame.image.load('./imagens/frame_14_delay.jpg')
        rain_image15 = pygame.image.load('./imagens/frame_15_delay.jpg')
        rain_image16 = pygame.image.load('./imagens/frame_16_delay.jpg')
        rain_image17 = pygame.image.load('./imagens/frame_17_delay.jpg')
        rain_image18 = pygame.image.load('./imagens/frame_18_delay.jpg')
        rain_image19 = pygame.image.load('./imagens/frame_19_delay.jpg')
        rain_image20 = pygame.image.load('./imagens/frame_20_delay.jpg')
        rain_image21 = pygame.image.load('./imagens/frame_21_delay.jpg')
        rain_image22 = pygame.image.load('./imagens/frame_22_delay.jpg')
        rain_image23 = pygame.image.load('./imagens/frame_23_delay.jpg')
        rain_image24 = pygame.image.load('./imagens/frame_24_delay.jpg')
        rain_image25 = pygame.image.load('./imagens/frame_25_delay.jpg')
        rain_image26 = pygame.image.load('./imagens/frame_26_delay.jpg')
        rain_image27 = pygame.image.load('./imagens/frame_27_delay.jpg')
        rain_image28 = pygame.image.load('./imagens/frame_28_delay.jpg')
        rain_image29 = pygame.image.load('./imagens/frame_29_delay.jpg')
        rain_image30 = pygame.image.load('./imagens/frame_30_delay.jpg')
        rain_image31 = pygame.image.load('./imagens/frame_31_delay.jpg')
        rain_image32 = pygame.image.load('./imagens/frame_32_delay.jpg')
        rain_image33 = pygame.image.load('./imagens/frame_33_delay.jpg')
        rain_image34 = pygame.image.load('./imagens/frame_34_delay.jpg')
        rain_image35 = pygame.image.load('./imagens/frame_35_delay.jpg')
        rain_image36 = pygame.image.load('./imagens/frame_36_delay.jpg')
        rain_image37 = pygame.image.load('./imagens/frame_37_delay.jpg')
        rain_image38 = pygame.image.load('./imagens/frame_38_delay.jpg')
        rain_image39 = pygame.image.load('./imagens/frame_38_delay.jpg')
        rain_image40 = pygame.image.load('./imagens/frame_40_delay.jpg')
        rain_image41 = pygame.image.load('./imagens/frame_41_delay.jpg')
        rain_image42 = pygame.image.load('./imagens/frame_42_delay.jpg')
        rain_image43 = pygame.image.load('./imagens/frame_43_delay.jpg')
        rain_image44 = pygame.image.load('./imagens/frame_44_delay.jpg')
        rain_image45 = pygame.image.load('./imagens/frame_45_delay.jpg')
        rain_image46 = pygame.image.load('./imagens/frame_46_delay.jpg')
        rain_image47 = pygame.image.load('./imagens/frame_47_delay.jpg')

        imageCurrent = 0

        running = True
        while running:
            if (imageCurrent==0):
                screen.blit(rain_image0, (0,0))
            if (imageCurrent==1):
                screen.blit(rain_image1, (00,0))
            if (imageCurrent==2):
                screen.blit(rain_image2, (00,0))
            if (imageCurrent==3):
                screen.blit(rain_image3, (00,0))
            if (imageCurrent==4):
                screen.blit(rain_image4, (00,0))
            if (imageCurrent==5):
                screen.blit(rain_image5, (00,0))
            if (imageCurrent==6):
                screen.blit(rain_image6, (00,0))
            if (imageCurrent==7):
                screen.blit(rain_image7, (00,0))
            if (imageCurrent==8):
                screen.blit(rain_image8, (00,0))
            if (imageCurrent==9):
                screen.blit(rain_image9, (00,0))
            if (imageCurrent==10):
                screen.blit(rain_image10, (00,0))
            if (imageCurrent==11):
                screen.blit(rain_image11, (00,0))
            if (imageCurrent==12):
                screen.blit(rain_image12, (00,0))
            if (imageCurrent==13):
                screen.blit(rain_image13, (00,0))
            if (imageCurrent==14):
                screen.blit(rain_image14, (00,0))
            if (imageCurrent==15):
                screen.blit(rain_image15, (00,0))
            if (imageCurrent==16):
                screen.blit(rain_image16, (00,0))
            if (imageCurrent==17):
                screen.blit(rain_image17, (00,0))
            if (imageCurrent==18):
                screen.blit(rain_image18, (00,0))
            if (imageCurrent==19):
                screen.blit(rain_image19, (00,0))
            if (imageCurrent==20):
                screen.blit(rain_image20, (00,0))
            if (imageCurrent==21):
                screen.blit(rain_image21, (00,0))
            if (imageCurrent==22):
                screen.blit(rain_image22, (00,0))
            if (imageCurrent==23):
                screen.blit(rain_image23, (00,0))
            if (imageCurrent==24):
                screen.blit(rain_image24, (00,0))
            if (imageCurrent==25):
                screen.blit(rain_image25, (00,0))
            if (imageCurrent==26):
                screen.blit(rain_image26, (00,0))    
            if (imageCurrent==27):
                screen.blit(rain_image27, (00,0))
            if (imageCurrent==28):
                screen.blit(rain_image28, (00,0))
            if (imageCurrent==29):
                screen.blit(rain_image29, (00,0))
            if (imageCurrent==30):
                screen.blit(rain_image30, (00,0))
            if (imageCurrent==31):
                screen.blit(rain_image31, (00,0))
            if (imageCurrent==32):
                screen.blit(rain_image32, (00,0))
            if (imageCurrent==33):
                screen.blit(rain_image33, (00,0))
            if (imageCurrent==34):
                screen.blit(rain_image34, (00,0))
            if (imageCurrent==35):
                screen.blit(rain_image35, (00,0))
            if (imageCurrent==36):
                screen.blit(rain_image36, (00,0))
            if (imageCurrent==37):
                screen.blit(rain_image37, (00,0))
            if (imageCurrent==38):
                screen.blit(rain_image38, (00,0))
            if (imageCurrent==39):
                screen.blit(rain_image39, (00,0))
            if (imageCurrent==40):
                screen.blit(rain_image40, (00,0))
            if (imageCurrent==41):
                screen.blit(rain_image41, (00,0))
            if (imageCurrent==42):
                screen.blit(rain_image42, (00,0))
            if (imageCurrent==43):
                screen.blit(rain_image43, (00,0))
            if (imageCurrent==44):
                screen.blit(rain_image44, (00,0))
            if (imageCurrent==45):
                screen.blit(rain_image45, (00,0))
            if (imageCurrent==46):
                screen.blit(rain_image46, (00,0))
            if (imageCurrent==47):
                screen.blit(rain_image47, (00,0))
            
            if (imageCurrent==47):
                imageCurrent = 0
                sleep(0.02)
            else:
                imageCurrent += 1
                sleep(0.02)

            
            pygame.font.init()                                                          ##### inicia font
            fonte=pygame.font.get_default_font()                                        ##### carrega com a fonte padrão
            fontesys=pygame.font.SysFont(fonte, 30)                                     ##### usa a fonte padrão
            txttela = fontesys.render('Pressione "q" para sair', 1, (255,255,255))      ##### renderiza o texto na cor desejada
            screen.blit(txttela,(450, 600))                                             ##### coloca na posição (tela FHD)
            pygame.display.update()    
            
            pygame.font.init()                                                          ##### inicia font
            fonte=pygame.font.get_default_font()                                        ##### carrega com a fonte padrão
            fontesys=pygame.font.SysFont(fonte, 30)                                     ##### usa a fonte padrão
            txttela = fontesys.render('Pressione "r" para retornar', 1, (255,255,255))  ##### renderiza o texto na cor desejada
            screen.blit(txttela,(450, 630))                                             ##### coloca na posição (tela FHD)
            pygame.display.update()    
            
            pygame.font.init()                                                          ##### inicia font
            fonte=pygame.font.get_default_font()                                        ##### carrega com a fonte padrão
            fontesys=pygame.font.SysFont(fonte, 30)                                     ##### usa a fonte padrão
            txttela = fontesys.render('Pressione "p" para pausar', 1, (255,255,255))  ##### renderiza o texto na cor desejada
            screen.blit(txttela,(450, 660))                                             ##### coloca na posição (tela FHD)
            pygame.display.update()    
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == pygame.K_r:
                        mixer.music.unpause()
                    if event.key == pygame.K_p:
                        mixer.music.pause()
                    if event.key == K_q:
                        running = False
                        pygame.quit()

if __name__ == "__main__":
    chuva = Chuva()
    chuva.running()
