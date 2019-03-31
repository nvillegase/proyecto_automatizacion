import serial.tools.list_ports as ports
import serial

from pprint import pprint
from datetime import datetime

def serial_port_detect():

    pts = list(ports.comports())
    for p in pts:
        device = p.device
        return device

if __name__ == '__main__':

    device = serial_port_detect()
    arduino = serial.Serial(device, 115200, timeout=0.1)
    t_pasado = datetime.now()
    
    try:

        while True:
            
            t_actual = datetime.now()
            
            if arduino.in_waiting:
                recibido = arduino.readline()
                print("Mensaje recibido de Arduino: {}".format(recibido.decode('utf-8')))

            # Iterar cada 1s
            if (t_actual - t_pasado).total_seconds() >= 1.0:
                t_pasado = t_actual
                arduino.write('De Orange Pi a Arduino!'.encode('utf-8'))

    except KeyboardInterrupt:

        arduino.close()
        print("\nFin de la comunicación.")

    except Exception as e:

        print("Error\n{}\n\n\n".format(e))
