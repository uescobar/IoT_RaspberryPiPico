import network
import utime


wf = network.WLAN(network.STA_IF)
wf.active(True)

#wf.connect('IZZI-0761', 'C85261810761')
wf.connect('pilotAcademic', 'C85261810761')

# la conexión puede demorar unos segundos,
# Creamos un ciclo que termina cuando se ha realizado la conexión
while not wf.isconnected():
    print(".")
    utime.sleep(1) # cada segundo se imprime un punto

# al salir, imprimimos
print("Conectado al WiFi")
print(wf.ifconfig())


