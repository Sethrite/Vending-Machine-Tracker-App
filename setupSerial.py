import serial
import subprocess
import time
import serial.tools.list_ports

# Configure the serial port (update 'COM3' with your actual port and baud rate)

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

port = input("select Port: COM")

for x in range(0,len(portList)):
    if portList[x].startswith("COM" + str(port)):
        portVar = "COM" + str(port)
        print(portList[x])

SERIAL_PORT = portVar  # or '/dev/ttyUSB0' on Linux
BAUD_RATE = 9600

def trigger_decrement(snack_id):
    # Command to run the decrement_snack_by_id management command
    command = f'python manage.py demonstration {snack_id}'
    subprocess.run(command, shell=True)

def main():
    # Open the serial port
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
        print("Listening for serial data...")

        while True:
            if ser.in_waiting > 0:  # Check if there's data to read
                data = ser.readline().decode('utf-8').strip()  # Read a line from the serial port
                print(f"Received: {data}")

                if data == '0':
                    # Trigger decrement for snack with ID 1 (you can change this ID)
                    if prevdata == '1':
                        trigger_decrement(2)
                        print("Activated")
                prevdata = data

            
                time.sleep(0.1)  # Small delay to prevent high CPU usage

if __name__ == "__main__":
    main()
