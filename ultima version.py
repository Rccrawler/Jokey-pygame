import pygame, sys
import os
pygame.init()
os.system("cls")
rt = 0

#Obtiene los datos de ancho y largo y largo para usarlos como resolucion en cualquier dispositivo
info = pygame.display.Info()
ancho_actual = info.current_w
largo_actual = info.current_h
resolucion_actual=(ancho_actual,largo_actual)
screen=pygame.display.set_mode((ancho_actual,largo_actual))
pygame.mixer.init()

#carga la musica
sonido_inpacto = pygame.mixer.Sound("I:\\Samsung\\programacion\\Ejercicios python clase\\pygame\\juego grupo\\audio inpacto.mp3")
#sonido_inpacto.set_volume(1.0)

sonido_fondo = pygame.mixer.Sound("I:\\Samsung\\programacion\\Ejercicios python clase\\pygame\\juego grupo\\musica juego.mp3")
#sonido_fondo.set_volume(0.2)

#Metemos un fondo de pantalla ajustable
cor_fon_x=0
cor_fon_y=0
fondo_juego=pygame.image.load("I:\\Samsung\\programacion\\Ejercicios python clase\\pygame\\juego grupo\\mesa_hokey.png").convert_alpha()
tamaño_fondo_juego=pygame.transform.scale(fondo_juego,(ancho_actual,largo_actual))

#Metemos ficha
ficha=pygame.image.load("I:\\Samsung\\programacion\\Ejercicios python clase\\pygame\\juego grupo\\ficha.png").convert_alpha()
tamaño_ficha=pygame.transform.scale(ficha,(120,120))
ficha_rect=tamaño_ficha.get_rect()

#Metemos golpeadores
golpeador_1=pygame.image.load("I:\\Samsung\\programacion\\Ejercicios python clase\\pygame\\juego grupo\\jugador berde con raton.png").convert_alpha()
tamaño_golpeador_1=pygame.transform.scale(golpeador_1,(180,180))
golpeador_1_rect=tamaño_golpeador_1.get_rect()

golpeador_2=pygame.image.load("I:\\Samsung\\programacion\\Ejercicios python clase\\pygame\\juego grupo\\jugador berde con raton.png").convert_alpha()
tamaño_golpeador_2=pygame.transform.scale(golpeador_2,(180,180))
golpeador_2_rect=tamaño_golpeador_2.get_rect()

#Velocidad ficha [1,1] --> x,y
velocidad_ficha_recto=[2,0]
velocidad_ficha_diagonal_abajo=[2,2]
#Colocacion ficha y golpeadores 1 y 2
golpeador_1_rect.center = (ancho_actual/2-ancho_actual/4.5, largo_actual/2)
golpeador_2_rect.center = (ancho_actual/2+ancho_actual/4.5, largo_actual/2)
ficha_rect.center = (ancho_actual/2.5, largo_actual/2)

stop = True
x = 0
y = 0
negro = (0, 0, 0)
rojo = (255, 0, 0)
azul = (119, 220, 177)
blanco = (255, 255, 255)

controlador = 0
#texto puntuacion
controlador1=0
controlador2=0

tamaño_fuente_1 = int(resolucion_actual[1] / 6.7)
fuente_1 = pygame.font.SysFont("Impact", tamaño_fuente_1)
contador1 = fuente_1.render(f"Puntos: {controlador1}", True, (0, 0, 0))
contador2 = fuente_1.render(f"Puntos: {controlador2}", True, (0, 0, 0))
#Controlador y bucle principal

run=True
while run:
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    while controlador==0:

        stop = True
        menu = True
        cor_fon_X=0
        cor_fon_y=0
        x = 0
        y = 0
        negro = (0,0,0)
        rojo = (255,0,0)
        azul = (119,220,177)
        blanco = (255,255,255)

        pygame.init()
        pygame.mixer.init()

        #testo botones

        # Cargando la fuente desde el archivo "myfont.ttf"
        font = pygame.font.Font("I:\\Samsung\\programacion\\Ejercicios python clase\\pygame\\juego grupo\\fuentes\\Super Mario 64.ttf", 36)

        # Crea una superficie de texto utilizando la fuente cargada
        #text = font.render("Hola, mundo!", True, (255, 255, 255))

        #font = pygame.font.Font(None, 36)
        text = font.render("PLAY", True, negro)
        text2 = font.render("OPCIONES", True, negro)
        text3 = font.render("X", True, blanco)

        #crea el rectangulo del boton
        button_rect = pygame.Rect(1000, 120, 200, 50)
        button_rect2 = pygame.Rect(200, 690, 200, 50)

        button_rect3 = pygame.Rect(1360, 0, 200, 50)

        info = pygame.display.Info()
        ancho_actual = info.current_w
        largo_actual = info.current_h
        resolucion_actual=(ancho_actual,largo_actual)
        #screen=pygame.display.set_mode((ancho_actual,largo_actual))
        screen = pygame.display.set_mode(resolucion_actual)

        # Carga las imágenes del gif
        images = []
        i = 1
        for i in range(1, 92):
            image = pygame.image.load(f"I:\\Samsung\\programacion\\Ejercicios python clase\\pygame\\juego grupo\\frame-{str(i).zfill(3)}.gif").convert_alpha()#zfill(3) es para añadirle tres cifras enbez de 1 que sea 001
            imagee = pygame.transform.scale(image, resolucion_actual)
            ancho_actual = imagee.get_width()
            largo_actual = imagee.get_height()
            images.append(imagee)

        # Carga la canción
        #pygame.mixer.music.load("I:\\Samsung\\programacion\\Ejercicios python clase\\pygame\\juego grupo\\audio menu.mp3")
        sonido_menu = pygame.mixer.Sound("I:\\Samsung\\programacion\\Ejercicios python clase\\pygame\\juego grupo\\audio_menu.mp3")
        # Empieza la música
        #pygame.mixer.music.play(-1)
        sonido_menu.play(-1)

        while stop:

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        print("El botón play fue presionado.")
                        controlador = 1
                        stop = False
                        menu = False
                        sonido_menu.stop()

                    if button_rect2.collidepoint(event.pos):
                        print("El botón2 fue presionado.")
                    if button_rect3.collidepoint(event.pos):
                            print("El botón3 fue presionado.")
                            pygame.mixer.music.stop()
                            sonido_menu.stop()
                            pygame.quit()
                            stop == False

            if menu == True and stop == True:
                for image in images:
                    screen.blit(image, (cor_fon_X, cor_fon_y))

                    pygame.draw.rect(screen, azul, button_rect)
                    screen.blit(text, [button_rect.x + 47, button_rect.y + 10])

                    pygame.draw.rect(screen, azul, button_rect2)
                    screen.blit(text2, [button_rect2.x + 2, button_rect2.y + 10])

                    pygame.draw.rect(screen, rojo, button_rect3)
                    screen.blit(text3, [button_rect3.x + 13, button_rect3.y + 10])

                    pygame.display.flip()
                    pygame.time.wait(100)

            pygame.display.flip()

    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    while controlador==1:
        #Evento salida
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                controlador = 0
                stop = True
                menu = True
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            controlador = 0
            stop = True
            menu = True
            sonido_fondo.stop()
        if menu != True:
            sonido_fondo.play(-1)
        #Movimiento golpeador 1
        Keys = pygame.key.get_pressed()
        
        if rt > 1:
            rt = rt -1
            print (rt)
            
        if Keys[pygame.K_a] and golpeador_1_rect.x > ancho_actual/20:
            golpeador_1_rect.x = golpeador_1_rect.x-6
            if golpeador_1_rect.colliderect(ficha_rect):
                rt = 1000
        if Keys[pygame.K_d] and golpeador_1_rect.x < ancho_actual/2.5:
            golpeador_1_rect.x = golpeador_1_rect.x+6
            if golpeador_1_rect.colliderect(ficha_rect):
                rt = 1000
        if Keys[pygame.K_w] and golpeador_1_rect.y > largo_actual/16:
            golpeador_1_rect.y = golpeador_1_rect.y-6
            if golpeador_1_rect.colliderect(ficha_rect):
                rt = 1000
        if Keys[pygame.K_s] and golpeador_1_rect.y < largo_actual-180-largo_actual/18:
            golpeador_1_rect.y = golpeador_1_rect.y+6
            if golpeador_1_rect.colliderect(ficha_rect):
                rt = 1000
        
        if rt > 1:
            rt = rt -1
            print (rt)
            
        #Movimiento golpeador 2
        Keys = pygame.key.get_pressed()
        if rt > 1:
            rt = rt -1
            print (rt)
            
        if Keys[pygame.K_LEFT] and golpeador_2_rect.x > ancho_actual/1.96:
            golpeador_2_rect.x = golpeador_2_rect.x - 6
            if golpeador_2_rect.colliderect(ficha_rect):
                rt = 1000
        if Keys[pygame.K_RIGHT] and golpeador_2_rect.x < ancho_actual-180-largo_actual/12:
            golpeador_2_rect.x = golpeador_2_rect.x + 6
            if golpeador_2_rect.colliderect(ficha_rect):
                rt = 1000
        if Keys[pygame.K_UP] and golpeador_2_rect.y > largo_actual/16:
            golpeador_2_rect.y = golpeador_2_rect.y - 6
            if golpeador_2_rect.colliderect(ficha_rect):
                rt = 1000
        if Keys[pygame.K_DOWN] and golpeador_2_rect.y < largo_actual-180-largo_actual/18:
            golpeador_2_rect.y = golpeador_2_rect.y + 6
            if golpeador_2_rect.colliderect(ficha_rect):
                rt = 1000
        if rt > 1:
            rt = rt -1
            print (rt)

        #Movimiento ficha
        if golpeador_1_rect.colliderect(ficha_rect) or rt > 1:
            ficha_rect = ficha_rect.move(velocidad_ficha_diagonal_abajo)
        ficha_rect.move_ip(velocidad_ficha_recto)

        # Mueve la ficha
        ficha_rect.move_ip(velocidad_ficha_recto)
        # Verifica si la ficha choca con los golpeadores
        if ficha_rect.colliderect(golpeador_1_rect) or ficha_rect.colliderect(golpeador_2_rect):
            sonido_inpacto.play()
            velocidad_ficha_recto[0] = -velocidad_ficha_recto[0]
        # Verifica si la ficha choca con los límites de la mesa

        if ficha_rect.left < 0 or ficha_rect.right > ancho_actual:
            sonido_inpacto.play()
            velocidad_ficha_recto[0] = -velocidad_ficha_recto[0]

        if ficha_rect.top < 0 or ficha_rect.bottom > largo_actual:
            sonido_inpacto.play()
            velocidad_ficha_recto[1] = -velocidad_ficha_recto[1]
        #Condicion limites
        if golpeador_1_rect.colliderect(ficha_rect) or golpeador_2_rect.colliderect(ficha_rect) or rt > 1:
            ficha_rect = ficha_rect.move(velocidad_ficha_diagonal_abajo)
            #Limites ficha derecha e izquierda
            if ficha_rect.left < ancho_actual/20 or ficha_rect.right > ancho_actual-70:
                velocidad_ficha_diagonal_abajo[0] = -velocidad_ficha_diagonal_abajo[0]
                sonido_inpacto.play(1)
            #Limites ficha arriba y abajo
            if ficha_rect.top < largo_actual/16 or ficha_rect.bottom > largo_actual-120/2:
                velocidad_ficha_diagonal_abajo[1] = -velocidad_ficha_diagonal_abajo[1]
                sonido_inpacto.play(1)

            #Porteria
            if ficha_rect == largo_actual / 2 and ficha_rect == ancho_actual-ancho_actual+30:
            #if ficha_rect == 0 and ficha_rect > largo_actual / 3 and ficha_rect < largo_actual - largo_actual / 3:
            #if ficha_rect == ancho_actual and ficha_rect > largo_actual / 3 and ficha_rect < largo_actual-largo_actual/ 3:
                controlador1 += 1
                print("puntuacion1", controlador1)
            if ficha_rect == largo_actual / 2 and ficha_rect == ancho_actual-30:
            #if ficha_rect == ancho_actual - ancho_actual and ficha_rect > largo_actual / 3 and ficha_rect < largo_actual - largo_actual / 3:
            #if ficha_rect == ancho_actual-ancho_actual and ficha_rect > largo_actual / 3 and ficha_rect < largo_actual - largo_actual / 3:
                controlador2 += 1
                print("puntuacion2", controlador2)

        #Imprimir por pantalla creada
        screen.blit(tamaño_fondo_juego, (cor_fon_x, cor_fon_y))
        screen.blit(tamaño_golpeador_1, golpeador_1_rect)
        screen.blit(tamaño_golpeador_2, golpeador_2_rect)
        screen.blit(tamaño_ficha, ficha_rect)

        contador1 = fuente_1.render(f"Puntos: {controlador1}", True, (0, 0, 0))
        contador2 = fuente_1.render(f"Puntos: {controlador2}", True, (0, 0, 0))
        screen.blit(contador1, [ancho_actual/10, largo_actual-largo_actual])
        screen.blit(contador2, [ancho_actual-ancho_actual/2.5, largo_actual-largo_actual])
        pygame.display.flip()
pygame.quit()