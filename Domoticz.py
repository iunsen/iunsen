# Domoticz JSON API documentation https://www.domoticz.com/wiki/Domoticz_API
# Code adaptated from orignial Ralph script 
# Code adapté du script original de Ralph publié sur le forum MicroPython
# https://forum.pycom.io/topic/240/example-project-pir-sensor-and-domoticz-api
# projetsdiy.fr - diyprojects.io (dec. 2017)

import socket
class Domoticz:
    def __init__(self, ip, port,  basic):
        self.basic = basic
        self.ip = ip
        self.port = port

    def setLight(self, idx, command):
        return self.sendRequest("type=command&param=switchlight&idx="+idx+"&switchcmd="+command)
    
    def setTemperature(self, idx, value):
        return self.sendRequest("type=command&param=udevice&idx="+idx+"&nvalue=0&svalue="+value) 
    
    def setHumidity(self, idx, value, hum_stat):
        # hum_stat: 0=Normal, 1=Comfortable, 2=Dry, 3=Wet
        return self.sendRequest("type=command&param=udevice&idx="+idx+"&nvalue="+value+"&svalue="+hum_stat)
        
    def setBarometer(self, idx, value, bar_for):
        # bar_for (forecast): 0 = Stable, 1 = Sunny, 2 = Cloudy, 3 = Unstable, 4 = Thunderstorm
        return self.sendRequest("type=command&param=udevice&idx="+idx+"&nvalue=0&svalue="+value+";"+bar_for)
    
    def setTemperatureHumidity(self, idx, temp, hum, hum_stat):
        # hum_stat: 0=Normal, 1=Comfortable, 2=Dry, 3=Wet
        return self.sendRequest("type=command&param=udevice&idx="+idx+"&nvalue=0&svalue="+temp+";"+hum+";"+hum_stat)
    
    def setTemperatureHumidityBarometer(self, idx, temp, hum, hum_stat, bar, bar_for):
        # hum_stat: 0=Normal, 1=Comfortable, 2=Dry, 3=Wet
        # bar_for (barometer forecast): 0 = No Info, 1 = Sunny, 2 = Paryly Cloudy, 3 = Cloudy, 4 = Rain
        return self.sendRequest("type=command&param=udevice&idx="+idx+"&nvalue=0&svalue="+temp+";"+hum+";"+hum_stat+";"+bar+";"+bar_for)
    
    def setTemperatureBarometer(self, idx, temp, bar, bar_for, altitude):
        # hum_stat: 0=Normal, 1=Comfortable, 2=Dry, 3=Wet
        # bar_for (barometer forecast): 0 = No Info, 1 = Sunny, 2 = Paryly Cloudy, 3 = Cloudy, 4 = Rain
        return self.sendRequest("type=command&param=udevice&idx="+idx+"&nvalue=0&svalue="+temp+";"+bar+";"+bar_for+";"+altitude)
    
    def setAirQuality(self, idx, ppm):
        return self.sendRequest("type=command&param=udevice&idx="+idx+"&nvalue="+ppm)   

    def setVariable(self, name, value):
        return self.sendRequest("type=command&param=updateuservariable&vtype=0&vname="+name+"&vvalue="+value)

    def sendRequest(self, path):
        try:
            s = socket.socket()
            s.connect((self.ip,self.port))
            s.send(b"GET /json.htm?"+path+" HTTP/1.1\r\nHost: pycom.io\r\nAuthorization: Basic "+self.basic+"\r\n\r\n")
            status = str(s.readline(), 'utf8')
            code = status.split(" ")[1]
            s.close()
            return code

        except Exception:
            print("HTTP request failed")
            return 0
