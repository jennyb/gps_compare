# gps_compare

GPS compare currently takes in two GPS streams, one from a USB puck and another from a Bluetooth GPS dongle and saves both NMEA streams into separate text files for debug. 

To connect a Bluetooth GPS module ( The GT-750 in my case ) to a Raspberry Pi, try the following commands :

sudo hcitool scan
bluetoothctl 
>
agent on
pairable on
scan on
scan off
pair xx:xx:xx:xx:xx:xx
[agent]PIN code: 0000
exit

sudo rfcomm bind /dev/rfcomm1 00:1B:F6:A0:07:22
 
