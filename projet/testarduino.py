import serial
import time
print('hello')

ser=serial.Serial('COM3',9600)
ser.timeout=1

while True:
    i=input('input(on/off): ').strip()
    if i=='done':
        break
    ser.write(i.encode())
    time.sleep(0.5)
    print(ser.readline().decode('ascii'))
ser.close()
