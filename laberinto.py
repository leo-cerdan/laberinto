import pygame
pygame.init()

# Medidas pantalla
ANCHO = 1280
ALTO = 720

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
MARRON = (77, 38, 0)
AZUL = (0, 0, 255)

# Ventana
ventana = pygame.display.set_mode((ANCHO,ALTO))
reloj = pygame.time.Clock()

mapa1 = [
	" XXXXXXXXXXXXXXX",
	"  XXXXX         ",
	"X   XXX XXXX XX ",
	"X X XX  XXXX XX ",
	"X X    X     XX ",
	"X XXXXXXXXXXXXX ",
	"X  X           X",
	"XX   XXX XXXXX  ",
	"XXXX     XXXXXXX"
]

mapa2 = [
	"X XXXXXXXXXXXXXX",
	"X              X",
	"X XXXXXX XXXXXXX",
	"X X            X",
	"X XXXX XXXXXXX X",
	"X X    X       X",
	"XXXX XXXXX XXXXX",
	"X     X         ",
	"XXXXXXXXXXXXXXX "
]

mapa3 = [
	"X       XXXXXXXX",
	"XX XXXX X     X ",
	"        X XXX X ",
	"XXXXXXX X XXX   ",
	"X     X   XXX XX",
	"XXXXX XXXXXXX XX",
	"X   X         XX",
	"XXX XXXX XX XXXX",
	"XXX      XX     "
]

# Funciones
def dibujar_muros(superficie,rectangulo):
    pygame.draw.rect(superficie, MARRON, rectangulo)

def construir_mapa(mapa):
    muros = []
    x = 0
    y = 0
    for fila in mapa:
        for muro in fila:
            if muro == "X":
                muros.append(pygame.Rect(x,y,80,80))
            x += 80
        x = 0
        y += 80
    return muros

def dibujar_mapa(superficie, muros):
    for muro in muros:
        dibujar_muros(superficie,muro)

def llegada(x,y,color):
    pygame.draw.rect(ventana, color, (x,y,80,80))

# Imágenes jugador
player00 = pygame.image.load("par_0.png").convert_alpha()
playe1_izq = pygame.image.load("izq_1.png").convert_alpha()
playe2_izq = pygame.image.load("izq_2.png").convert_alpha()
playe3_izq = pygame.image.load("izq_3.png").convert_alpha()
playe4_izq = pygame.image.load("izq_4.png").convert_alpha()
playe1_der = pygame.image.load("der_1.png").convert_alpha()
playe2_der = pygame.image.load("der_2.png").convert_alpha()
playe3_der = pygame.image.load("der_3.png").convert_alpha()
playe4_der = pygame.image.load("der_4.png").convert_alpha()
playe1_arr = pygame.image.load("arr_1.png").convert_alpha()
playe2_arr = pygame.image.load("arr_2.png").convert_alpha()
playe3_arr = pygame.image.load("arr_3.png").convert_alpha()
playe4_arr = pygame.image.load("arr_4.png").convert_alpha()
playe1_aba = pygame.image.load("baj_1.png").convert_alpha()
playe2_aba = pygame.image.load("baj_2.png").convert_alpha()
playe3_aba = pygame.image.load("baj_3.png").convert_alpha()
playe4_aba = pygame.image.load("baj_4.png").convert_alpha()
final = pygame.image.load("final.png").convert_alpha()

player_ini = player00

# Datos
laberinto1 = construir_mapa(mapa1)
laberinto2 = construir_mapa(mapa2)
laberinto3 = construir_mapa(mapa3)

#laberinto = laberinto1

player_rect = player_ini.get_rect()
player_velocidad_x = 80
player_velocidad_y = 0
frames_jugador = 0

# Bucle principal
jugando = True
while jugando:
    player_rect.x = 0
    player_rect.y = 0
    nivel = 0
    empezar = True

    while empezar:
        reloj.tick(60)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                empezar = False
                jugando = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    empezar = False
                    jugando = False
                
        movimiento_derecha = False
        movimiento_izquierda = False
        movimiento_arriba = False
        movimiento_abajo = False

        player_velocidad_x = 0
        player_velocidad_y = 0

        pulsacion = pygame.key.get_pressed()

        if pulsacion [pygame.K_UP]:
            player_velocidad_y = -3
            movimiento_arriba = True
        if pulsacion[pygame.K_DOWN]:
            player_velocidad_y = 3
            movimiento_abajo = True
        if pulsacion[pygame.K_LEFT]:
            player_velocidad_x = -3
            movimiento_izquierda = True
        if pulsacion[pygame.K_RIGHT]:
            player_velocidad_x = 3
            movimiento_derecha = True

        player_rect.x += player_velocidad_x
        player_rect.y += player_velocidad_y

        # Limites pantalla
        if player_rect.x > ANCHO - 60:
            player_rect.x = ANCHO - 60
        if player_rect.x < 0:
            player_rect.x = 0
        if player_rect.y > ALTO - 60:
            player_rect.y = ALTO - 60
        if player_rect.y < 0:
            player_rect.y = 0

        # Graficos
        ventana.fill(NEGRO)
        if nivel == 0:
            llegada(1200,560,BLANCO)
            dibujar_mapa(ventana, laberinto1)
            # Colisión laberinto
            for i in laberinto1:
                if player_rect.colliderect(i):
                    player_rect.x -= player_velocidad_x
                    player_rect.y -= player_velocidad_y
            if player_rect.x > 1200 and player_rect.y > 560:
                player_rect.x = 80
                player_rect.y = 0
                nivel = 1
        if nivel == 1:
            llegada(1200,640,VERDE)
            dibujar_mapa(ventana, laberinto2)
            # Colisión laberinto
            for i in laberinto2:
                if player_rect.colliderect(i):
                    player_rect.x -= player_velocidad_x
                    player_rect.y -= player_velocidad_y
                if player_rect.x > 1200 and player_rect.y > 640:
                    player_rect.x = 80
                    player_rect.y = 0
                    nivel = 2
        if nivel == 2:
            llegada(1200,640,AZUL)
            dibujar_mapa(ventana, laberinto3)
            # Colisión laberinto
            for i in laberinto3:
                if player_rect.colliderect(i):
                    player_rect.x -= player_velocidad_x
                    player_rect.y -= player_velocidad_y
                if player_rect.x > 1200 and player_rect.y > 640:
                    ventana.fill(NEGRO)
                    ventana.blit(final,(240,20))
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_s:
                                empezar = False
                                jugando = False
                            if event.key == pygame.K_RETURN:
                                empezar = False
                                jugando = True

        # Movimientos jugador
        if movimiento_derecha:
            frames_jugador += 1
            if frames_jugador >= 21:
                frames_jugador = 1
            if frames_jugador < 6:
                player_init = playe1_der
            elif frames_jugador < 11:
                player_ini = playe2_der
            elif frames_jugador < 16:
                player_ini = playe3_der
            elif frames_jugador < 21:
                player_ini = playe4_der
            ventana.blit(player_ini, player_rect)

        elif movimiento_izquierda:
            frames_jugador += 1
            if frames_jugador >= 21:
                frames_jugador = 1
            if frames_jugador < 6:
                player_init = playe1_izq
            elif frames_jugador < 11:
                player_ini = playe2_izq
            elif frames_jugador < 16:
                player_ini = playe3_izq
            elif frames_jugador < 21:
                player_ini = playe4_izq
            ventana.blit(player_ini, player_rect)

        elif movimiento_abajo:
            frames_jugador += 1
            if frames_jugador >= 21:
                frames_jugador = 1
            if frames_jugador < 6:
                player_init = playe1_aba
            elif frames_jugador < 11:
                player_ini = playe2_aba
            elif frames_jugador < 16:
                player_ini = playe3_aba
            elif frames_jugador < 21:
                player_ini = playe4_aba
            ventana.blit(player_ini, player_rect)

        elif movimiento_arriba:
            frames_jugador += 1
            if frames_jugador >= 21:
                frames_jugador = 1
            if frames_jugador < 6:
                player_init = playe1_arr
            elif frames_jugador < 11:
                player_ini = playe2_arr
            elif frames_jugador < 16:
                player_ini = playe3_arr
            elif frames_jugador < 21:
                player_ini = playe4_arr
            ventana.blit(player_ini, player_rect)

        else:
            player_ini = player00
            ventana.blit(player_ini, player_rect)
        
        # Actualizar
        pygame.display.update()

# Salir
pygame.quit()