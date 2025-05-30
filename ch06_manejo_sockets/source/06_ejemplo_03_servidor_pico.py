ssid='pilotAcademic'
claveSSID = 'C85261810761'

import network
import utime
import usocket

## CONEXION A LA RED

wf = network.WLAN(network.STA_IF)
wf.active(True)

wf.connect(ssid, claveSSID)

# la conexión puede demorar unos segundos,
# Creamos un ciclo que termina cuando se ha realizado la conexión
while not wf.isconnected():
    print(".")
    utime.sleep(1) # cada segundo se imprime un punto

# al salir, imprimimos
print("Conectado al WiFi")
print(wf.ifconfig())

## CREACION DEL SERVIDOR
s=usocket.socket()

s.bind(("192.168.2.164", 2025))
s.listen(10)
print("Socket creado, esperando conexiones...")
(sc,addr)=s.accept()
print("Cliente conectado, IP:", addr)
continuar=True

while continuar:
    dato = sc.recv(32).decode() # se decodifica para pasarlo a string
    print(dato)
    if dato == "z":
        continuar=False
     
print("Fin del programa")
sc.close()
s.close()



