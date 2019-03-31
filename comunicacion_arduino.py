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
    arduino = serial.Serial(device, 115200)
    t_pasado = datetime.now()
    
    try:

        while True:
            
            t_actual = datetime.now()
        
            # Iterar cada 50ms
            if (t_actual - t_pasado).total_seconds() > 0.05:
                t_pasado = t_actual
                recibido = arduino.readline()
                print(recibido)

    except KeyboardInterrupt:

        arduino.close()
        print("\nFin de la comunicación.")

    except Exception as e:

        print("Error\n{}\n\n\n".format(e))
