import serial, time

arduino = serial.Serial('COM3', 9600)
time.sleep(1)

while True:
    rawString = arduino.readline()
    temp = float(rawString.decode())
    tempC = (1.1*temp* 100)/1024
    print(round(tempC, 2))
    time.sleep(3)

arduino.close()
