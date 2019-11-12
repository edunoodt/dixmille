import random
def evaluadordeJuego(jugadorenTurno, puntosobtenidos):
    terminaeljuego=False
    if jugadorenTurno[1] == True:
        if puntosobtenidos + jugadorenTurno[2] == 10000:
            baja(30)
            print('====================================')
            print('====================================')
            print('          ', jugadorenTurno[0])
            print('          GANO!!!!!')
            print('====================================')
            print('====================================')
            jugadorenTurno[2] = puntosobtenidos + jugadorenTurno[2]
            terminaeljuego = True
        elif puntosobtenidos + jugadorenTurno[2] < 10000:
            jugadorenTurno[2] = puntosobtenidos + jugadorenTurno[2]
        else:
            print('Se paso. Conserva los puntos de la jugada anterior')

        print('Usted tiene', jugadorenTurno[2], ' puntos')
        #input('presione enter para continuar')
    elif puntosobtenidos >= 450:
        jugadorenTurno[1] = True
        print(jugadorenTurno[0], 'Ahora esta habilitado para sumar puntos')
    else:
        print('no consiguió suficientes puntos para entrar al juego')
    return terminaeljuego
def bienvenida():
    baja(20)
    print ('             Bienvenido al juego de los 10.000')
    baja(2)
    print('    DDDDDDD     III  XX      XX     MM        MM  III  LLL       LLL       EEEEEEEE')
    print('    DD   DDD    III   XX    XX      MMM      MMM  III  LLL       LLL       EEEEEEEE')
    print('    DD    DDD   III    XX  XX       MMMM    MMMM  III  LLL       LLL       EEE')
    print('    DD     DDD  III     XXXX        MM MM  MM MM  III  LLL       LLL       EEEEE')
    print('    DD     DDD  III      XX         MM  MMMM  MM  III  LLL       LLL       EEEEE')
    print('    DD     DDD  III     XXXX        MM   MM   MM  III  LLL       LLL       EEE')
    print('    DD    DDD   III    XX  XX       MM        MM  III  LLL       LLL       EEE')
    print('    DD   DDD    III   XX    XX      MM        MM  III  LLLLLLLLL LLLLLLLLL EEEEEEEEE')
    print('    DDDDDDD     III  XX      XX     MM        MM  III  LLLLLLLLL LLLLLLLLL EEEEEEEEE')
def baja(lineas):
    for i in range (lineas):print()
"""def muestrainfo(texto,info,veces):
    for i in range (veces):print('=================================')
    print('  ',texto,':', info)
    for i in range(veces):print('=================================')"""
def instrucciones():
    baja(10)
    respuesta = input('Ingrese "i" para conocer las intrucciones del juego >  ')
    respuesta = respuesta.upper()
    if respuesta == 'I':
        print('==============================================================================================')
        print("""
        El objetivo del juego es llegar a los 10.000 puntos exactos.
        En el caso que jugador se exceda en puntos, estos no serán considerados y
        finaliza su turno conservando los puntos que tenía antes de iniciar.

        Se considera ganador al primer jugador que obtenga los 10.000 puntos.

        Los jugadores por turno tiran cinco dados, tratando de que salgan unos (cada uno vale 100
        puntos), cincos (cada uno vale 50 puntos), y/o tres iguales (valen 100 veces el número que
        sale, por ejemplo: 2-2-2 = 200, etc.,

        Si en el primer tiro del turno del jugador salen tres unos (1-1-1) se computarán como 1.000 puntos o
        si sale escalera servida(1-2-3-4-5) en el primer tiro, se computará como 1500 puntos.

        Un jugador, después de contar los puntos, puede terminar y agregar todos los puntos de ese
        turno a su puntaje total, deberá tirar otra vez usando los dados que no le sirven, tratando de
        hacer puntos adicionales.

        El jugador debe sacar como mínimo 450 puntos para entrar al juego, para luego empezar a
        sumar puntos desde su proximo turno.

        El turno del jugador finaliza Únicamente cuando hace un tiro sin combinaciones que den
        puntos (Ningún 1 o 5 o ninguna combinación) . Si un jugador hace puntos con todos los
        dados que le quedan, se debe guardar el puntaje acumulado y continuar tirando los cinco
        dados otra vez.
        Una vez que el tiro arroje una tirada sin puntos, se sumarán los puntos obtenidos hasta ese
        momento.
        Luego se mostrará el resultado parcial de todos los participantes y continuará el siguiente
        jugador.


        """)
        print('==============================================================================================')
def tiralosdados(dados):
    jugada = []
    for i in range(dados):
        dado = random.randint(1, 6)
        jugada.append(dado)
    return jugada
def evaluajugada(jugada,primerTiro,cantidadDados):
    puntajeJugada=0
    retirar=0
    jugada.sort()
    if jugada==[1, 2, 3, 4, 5] and primerTiro:
        puntajeJugada+=1500
        retirar=5
    else:
        dados = [0, 0, 0, 0, 0, 0]
        for i in range (6):
            dados[i] = jugada.count(i+1)
       # print(dados)
        for i in (1,2,3,5):
            if dados[i]==3:
                puntajeJugada+=(i+1)*100
                retirar=3
        if dados[0]==3:
            retirar=3
            if primerTiro:
                puntajeJugada+=1000
            else:
                puntajeJugada=300
        else:
            puntajeJugada+=dados[0]*100
            retirar+=dados[0]
        puntajeJugada+=dados[4]*50
        retirar+=dados[4]
    cantidadDadosaTirar=cantidadDados-retirar
    if cantidadDadosaTirar==0:cantidadDadosaTirar=5
    return puntajeJugada,cantidadDadosaTirar
def ingresoJugadores():
    listaJugadores=[]
    nombre= ''
    while nombre!= '*':

        baja(2)
        print('==============================================================================================')
        nombre=input('ingrese nombre (o asterisco para terminar) > ')
        while nombre=='':
            nombre = input('No puede ingresar un espacio vacío, ingrese nombre (o asterisco para terminar) > ')
        if nombre!='*':
            jugador=[nombre, False, 0]
            listaJugadores.append(jugador)
        print('==============================================================================================')
    return listaJugadores
def encabezadoturno(JugadorenTurno):
    baja(10)
    print('Juega', JugadorenTurno[0])
    if JugadorenTurno[1] == True:
        print('Usted tiene:', JugadorenTurno[2], ' puntos')
    else:
        print('Debe sumar 450 puntos o mas par comenzar a sumar puntos')
    input('Presione cualquier tecla para continuar ')
