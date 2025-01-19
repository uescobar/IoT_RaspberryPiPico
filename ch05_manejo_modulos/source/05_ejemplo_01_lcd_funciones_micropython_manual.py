from machine import I2C, Pin

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

# probamos con la direccion que encontramos previamente
# res = i2c.writeto(39, b'hola') # enviando la data en bytes
# print(res)

direccion=255

for dire in range(128):
    try:
        res = i2c.writeto(dire, b'hola') # enviando la data en bytes
        direccion=dire
    except:
        a=0
        print("excepcion")
print(direccion)
