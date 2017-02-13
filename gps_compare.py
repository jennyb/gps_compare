#!/usr/bin/python

import serial
import pynmea2
import pifacecad
import time
import os

def parseGPS(str):
    if str.find('GGA') > 0:
        msg = pynmea2.parse(str)
        cad.lcd.clear
        #print "Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Altitude: %s %s" % (msg.timestamp,msg.lat,msg.lat_dir,msg.lon,msg.lon_dir,msg.altitude,msg.altitude_units)
        printString = "Lat:" + msg.lat + "\nLon:" + msg.lon + "\n" 
        cad.lcd.write(printString)
        cad.lcd.home()
 

cad = pifacecad.PiFaceCAD()
cad.lcd.backlight_on()
cad.lcd.write("NMEA Monitor")
time.sleep(2)
cad.lcd.clear()

#Bluetooth serial port
btSerial = serial.Serial(
    port = "/dev/rfcomm1", 
    baudrate = 4800,
    timeout = 0.5,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS
)


#try:
#    btSerial.isopen()
#except Exception, e:
#    cad.lcd.clear()
#    print "failed to open Bluetooth port: " + str(e)
#    cad.lcd.write ("BT port fail")
#    exit()



#USB serial port
serialPort = serial.Serial(
    port = "/dev/ttyACM0", 
    baudrate = 4800,
    timeout = 0.5,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS
)


#try:
#    serialPort.isopen()
#except Exception, e:
#    cad.lcd.clear()
#    print "failed to open USB port: " + str(e)
#    cad.lcd.write ("USB port fail")
#    exit()

while True:
    if cad.switches[4].value :
        cad.lcd.clear()
        cad.lcd.write("Shutting Down")
        os.system('shutdown -h now')
    
    if cad.switches[2].value :
        cad.lcd.clear()
        cad.lcd.write("Manual\nRefresh")
        time.sleep(2)
        cad.lcd.clear()

    usbStr = serialPort.readline()
    usbFile = open("/home/pi/usbGpsData.txt","w")
    usbFile.write(usbStr)
    usbFile.close()
    if usbStr.find('GGA') > 0:
        msg = pynmea2.parse(usbStr)
        cad.lcd.set_cursor(0,0)
        printString = "USB Fx:" + str(msg.gps_qual) + " Sats:" + str(msg.num_sats) + "\n"
        cad.lcd.write(printString)

    btStr = btSerial.readline()
    btFile = open("/home/pi/btGpsData.txt","w")
    btFile.write(btStr)
    btFile.close()
    if btStr.find('GGA') > 0:
        msg = pynmea2.parse(btStr)
        cad.lcd.set_cursor(0,1)
        printString = "BlT Fx:" + str(msg.gps_qual) + " Sats:" + str(msg.num_sats) + "\n"
        cad.lcd.write(printString)
    
