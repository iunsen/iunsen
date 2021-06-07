from machine import Pin, I2C
from time import sleep
import gfx
import dht 
import ssd1306

# ESP32 Pin assignment OLED screen
i2c = I2C(-1, scl=Pin(4), sda=Pin(5))
# ESP32 Pin assignment DHT22 sensor
sensor = dht.DHT22(Pin(14))
#sensor = dht.DHT11(Pin(14))
 
#Declaration de la taille de l'ecran
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
#En cas de besoin d'afficher des graphiques
graphics = gfx.GFX(oled_width, oled_height, oled.pixel)

#Partie principale du programme
while True:
 
  try:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    #hum_mod= hum / 2
    print('Temperature: %3.1f C' %temp)
    print('Humidity: %3.1f %%' %hum)
       #Affichage sur ecran oled
    oled.layout = 2
    oled.text('Temp = %3.1f C' %temp, 0, 0)
    oled.text('Hum = %3.1f %%' %hum, 0, 20)
    oled.show()
    sleep(1)
    oled.fill(0)
  except OSError as e:
    print('Failed to read sensor.')
    oled.text('Le capteur', 0, 0)
    oled.text('est debranche', 0, 20)
    oled.show()
    sleep(1)
    oled.fill(0) 


