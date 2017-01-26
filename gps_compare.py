import serial
import pynmea2
import pifacecad
import time

def parseGPS(str):
    if str.find('GGA') > 0:
        msg = pynmea2.parse(str)
        cad.lcd.clear
        #print "Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Altitude: %s %s" % (msg.timestamp,msg.lat,msg.lat_dir,msg.lon,msg.lon_dir,msg.altitude,msg.altitude_units)
        printString = "Lat:" + msg.lat + "\nLon:" + msg.lon + "\n" 
        cad.lcd.write(printString)
        cad.lcd.home()
 
usbFile = open("usbGpsData.txt","w")

cad = pifacecad.PiFaceCAD()
cad.lcd.backlight_on()
cad.lcd.write("NMEA Monitor")
time.sleep(2)
cad.lcd.clear()

try:
    serialPort = serial.Serial("/dev/ttyUSB0", 4800, timeout=0.5)
except IOError:
    print "failed to open serial port, try sudo.\n"

while True:
    str = serialPort.readline()
    usbFile.write(str)
    parseGPS(str)
