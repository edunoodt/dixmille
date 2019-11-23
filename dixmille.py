import soporte as sop
import os

sop.baja(20)
sop.bienvenida()
sop.instrucciones()
gamers=sop.ingresoJugadores()
ganoAlguien=False
respuesta=''
if gamers==[]:respuesta='SALIR'
while not ganoAlguien and respuesta!='SALIR':
    turno=0
    while turno<len(gamers) and not ganoAlguien and respuesta!='SALIR':
        estaJugando=gamers[turno]
        primerTiro=True
        puntajeTiro=1
        nuevotiro=5
        puntajeJugada=0
        controldeHabilitación=True
        os.system('cls')
        sop.encabezadoturno(estaJugando)
        while puntajeTiro!=0 and respuesta!='SALIR' and controldeHabilitación:
            #primerTiro, nuevotiro, puntajeJugada=sop.juego(primerTiro,nuevotiro,puntajeJugada)
            tiroActual = sop.tiralosdados(nuevotiro)
            sop.baja(2)
            os.system('cls')
            print('=====================================')
            print('|||||||||||||||||||||||||||||||||||||')
            print('     ',tiroActual)
            print('|||||||||||||||||||||||||||||||||||||')
            print('=====================================')
            sop.baja(2)

            puntajeTiro,nuevotiro=sop.evaluajugada(tiroActual, primerTiro, nuevotiro)
            puntajeJugada+=puntajeTiro
            print('====> En este tiro hizo:',puntajeTiro)

            print('====> En esta ronda suma:', puntajeJugada)
            if estaJugando[2]==False and puntajeJugada>=450:
                controldeHabilitación=False
            elif puntajeTiro!=0:
                primerTiro = False
                sop.baja(2)
                print('Usted tira ahora: ', nuevotiro,' dados')
                sop.baja(2)
            else:
                sop.baja(2)
                print('====>  ', 'Termino su turno. Pasa al siguiente jugador')
            respuesta=input('Presione cualquier tecla para continuar o ingrese "Salir" para terminar el juego> ').upper()
        if respuesta!='SALIR':ganoAlguien=sop.evaluadordeJuego(estaJugando,puntajeJugada)
        #respuesta = input('Presione cualquier tecla para continuar o ingrese "Salir" para terminar el juego> ').upper()
        if respuesta!='SALIR':
            sop.baja(5)
            os.system('cls')
            print('=========================================================')
            print('               PUNTUACION GENERAL')
            print('=========================================================')
            for variable in gamers:
                print('   ',variable[0],'puntos: ',variable[2])
            turno+=1
            respuesta = input('Presione cualquier tecla para continuar o ingrese "Salir" para terminar el juego> ').upper()
