import random
import soporte as sop

sop.baja(20)
sop.bienvenida()
sop.instrucciones()
gamers=sop.ingresoJugadores()
ganoAlguien=False
respuesta=''
while not ganoAlguien and respuesta!='SALIR':
    turno=0
    while turno<len(gamers) and not ganoAlguien and respuesta!='SALIR':
        estaJugando=gamers[turno]
        primerTiro=True
        puntajeTiro=1
        nuevotiro=5
        puntajeJugada=0
        #if primerTiro:
        sop.encabezadoturno(estaJugando)
        while puntajeTiro!=0 and respuesta!='SALIR':
            #primerTiro, nuevotiro, puntajeJugada=sop.juego(primerTiro,nuevotiro,puntajeJugada)
            tiroActual = sop.tiralosdados(nuevotiro)
            sop.baja(2)
            print('     ',tiroActual)
            sop.baja(2)

            puntajeTiro,nuevotiro=sop.evaluajugada(tiroActual, primerTiro, nuevotiro)
            puntajeJugada+=puntajeTiro
            print('====> En este tiro hizo:',puntajeTiro)

            print('====> Suma:', puntajeJugada)
            if puntajeTiro==0:
                print('====>  ','Termino')
            else:
                primerTiro=False
                print('Tira: ',nuevotiro)
            respuesta=input('Presione cualquier tecla para continuar o ingrese "Salir" para terminar el juego> ').upper()
        if respuesta!='SALIR':ganoAlguien=sop.evaluadordeJuego(estaJugando,puntajeJugada)
        turno+=1