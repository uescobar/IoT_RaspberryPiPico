import network

wf = network.WLAN(network.STA_IF)
wf.active(True)
lista=wf.scan()

for k in lista:
    print(k) # mac, ,nivel de señal, ,